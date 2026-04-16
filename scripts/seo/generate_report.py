from __future__ import annotations

import json
import re
import socket
from collections import Counter
from dataclasses import dataclass
from datetime import date
from html import unescape
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from config import ROOT, load_config


IGNORE_DIRS = {".git", "_site", "tmp", "output", "__pycache__"}
TAG_RE = re.compile(r"<[^>]+>")


@dataclass
class PageAudit:
    path: str
    file_path: str
    title: str
    meta_description: str
    robots: str
    canonical: str
    h1_count: int
    json_ld_count: int


def is_indexable(page: PageAudit) -> bool:
    return "noindex" not in page.robots.lower()


def url_path_for_file(path: Path) -> str:
    rel = path.relative_to(ROOT)
    if rel.name != "index.html":
        return f"/{rel.as_posix()}"
    parent = rel.parent.as_posix()
    return "/" if parent == "." else f"/{parent}/"


def extract_text(markup: str) -> str:
    stripped = TAG_RE.sub(" ", markup)
    return re.sub(r"\s+", " ", unescape(stripped)).strip()


def match_group(pattern: str, markup: str) -> str:
    match = re.search(pattern, markup, re.IGNORECASE | re.DOTALL)
    return unescape(match.group(1).strip()) if match else ""


def collect_pages() -> list[PageAudit]:
    pages: list[PageAudit] = []
    for path in sorted(ROOT.rglob("index.html")):
        if any(part in IGNORE_DIRS for part in path.parts):
            continue
        markup = path.read_text(encoding="utf-8")
        pages.append(
            PageAudit(
                path=url_path_for_file(path),
                file_path=str(path.relative_to(ROOT)),
                title=match_group(r"<title>(.*?)</title>", markup),
                meta_description=match_group(
                    r'<meta\s+name="description"\s+content="([^"]*)"', markup
                ),
                robots=match_group(r'<meta\s+name="robots"\s+content="([^"]*)"', markup),
                canonical=match_group(r'<link\s+rel="canonical"\s+href="([^"]*)"', markup),
                h1_count=len(re.findall(r"<h1\b", markup, re.IGNORECASE)),
                json_ld_count=len(
                    re.findall(
                        r'<script\s+type="application/ld\+json">', markup, re.IGNORECASE
                    )
                ),
            )
        )
    return pages


def read_sitemap_metrics() -> dict[str, Any]:
    sitemap_path = ROOT / "sitemap.xml"
    if not sitemap_path.exists():
        return {"exists": False, "url_count": 0}
    xml = sitemap_path.read_text(encoding="utf-8")
    return {"exists": True, "url_count": len(re.findall(r"<url>", xml))}


def detect_tracking(config: dict[str, Any], pages: list[PageAudit]) -> dict[str, Any]:
    html_blob = "\n".join((ROOT / page.file_path).read_text(encoding="utf-8") for page in pages)
    script_path = ROOT / "script.js"
    script_blob = script_path.read_text(encoding="utf-8") if script_path.exists() else ""
    has_gtag = any(marker in html_blob or marker in script_blob for marker in ("gtag(", "G-"))
    has_gtm = "googletagmanager.com" in html_blob or "GTM-" in html_blob
    has_datalayer = "dataLayer" in html_blob or "dataLayer" in script_blob
    measurement_id = config.get("analytics", {}).get("measurement_id", "").strip()
    return {
        "has_gtag": has_gtag,
        "has_gtm": has_gtm,
        "has_datalayer": has_datalayer,
        "measurement_id_configured": bool(measurement_id),
    }


def check_live_endpoint(url: str) -> dict[str, Any]:
    request = Request(
        url,
        headers={"User-Agent": "JadewavesSEOAudit/1.0 (+https://jadewavesenterprise.com)"},
    )
    try:
        with urlopen(request, timeout=10) as response:
            return {"ok": True, "status": getattr(response, "status", 200)}
    except HTTPError as exc:
        return {"ok": False, "status": exc.code, "error": f"HTTP {exc.code}"}
    except URLError as exc:
        reason = exc.reason
        if isinstance(reason, socket.timeout):
            return {"ok": False, "status": None, "error": "Timed out"}
        return {"ok": False, "status": None, "error": str(reason)}


def google_clients_available() -> tuple[bool, str]:
    try:
        import google.oauth2.service_account  # noqa: F401
        import googleapiclient.discovery  # noqa: F401
    except ModuleNotFoundError:
        return False, "Python Google API client libraries are not installed."
    return True, ""


def trends_client_available() -> tuple[bool, str]:
    try:
        import pytrends.request  # noqa: F401
    except ModuleNotFoundError:
        return False, "Python Google Trends client library is not installed."
    return True, ""


def google_reporting_window(config: dict[str, Any]) -> tuple[date, date]:
    end_date = date.today() - date.resolution
    start_date_raw = config.get("google_reporting_start_date", "").strip()
    if start_date_raw:
        try:
            start_date = date.fromisoformat(start_date_raw)
        except ValueError:
            start_date = end_date
    else:
        start_date = end_date

    if start_date > end_date:
        start_date = end_date
    return start_date, end_date


def configured_trend_targets(config: dict[str, Any]) -> list[str]:
    trends_config = config.get("trends", {})
    explicit_targets = [item.strip() for item in trends_config.get("targets", []) if item.strip()]
    if explicit_targets:
        return explicit_targets[: max(1, int(trends_config.get("max_terms", 8)))]

    seen: set[str] = set()
    targets: list[str] = []
    max_terms = max(1, int(trends_config.get("max_terms", 8)))
    for keyword_target in config.get("keyword_targets", []):
        for term in [keyword_target.get("primary", ""), *keyword_target.get("secondary", [])]:
            normalized = term.strip().lower()
            if not normalized or normalized in seen:
                continue
            seen.add(normalized)
            targets.append(term.strip())
            if len(targets) >= max_terms:
                return targets
    return targets


def fetch_trends_data(config: dict[str, Any]) -> tuple[dict[str, Any] | None, list[str]]:
    trends_config = config.get("trends", {})
    if not trends_config.get("enabled", False):
        return None, []

    available, library_message = trends_client_available()
    notes: list[str] = []
    if not available:
        notes.append(
            library_message + " Install it with `python3 -m pip install -r requirements-seo.txt`."
        )
        return None, notes

    targets = configured_trend_targets(config)
    if not targets:
        notes.append("No Google Trends target keywords are configured.")
        return None, notes

    seed_keyword = trends_config.get("seed_keyword", "").strip() or targets[0]
    timeframe = trends_config.get("timeframe", "today 3-m").strip() or "today 3-m"
    geo = trends_config.get("geo", "").strip()

    try:
        from pytrends.request import TrendReq
    except ModuleNotFoundError:
        notes.append(
            "Python Google Trends client library is not installed. Install it with "
            "`python3 -m pip install -r requirements-seo.txt`."
        )
        return None, notes

    try:
        client = TrendReq(hl="en-US", tz=330)
    except Exception as exc:
        notes.append(f"Could not initialize the Google Trends client: {exc}")
        return None, notes

    results: list[dict[str, Any]] = []
    for term in targets:
        if term.lower() == seed_keyword.lower():
            continue
        try:
            client.build_payload([seed_keyword, term], timeframe=timeframe, geo=geo)
            interest = client.interest_over_time()
        except Exception as exc:
            notes.append(f"Google Trends lookup failed for `{term}`: {exc}")
            continue

        if interest.empty or term not in interest:
            notes.append(f"Google Trends returned no directional data for `{term}`.")
            continue

        series = interest[term].astype(int)
        results.append(
            {
                "term": term,
                "average_interest": round(float(series.mean()), 2),
                "latest_interest": int(series.iloc[-1]),
                "peak_interest": int(series.max()),
            }
        )

    if not results and not notes:
        notes.append("Google Trends returned no usable keyword-interest data.")
        return None, notes

    results.sort(key=lambda item: (-item["average_interest"], -item["latest_interest"], item["term"]))
    return {
        "seed_keyword": seed_keyword,
        "geo": geo or "global",
        "timeframe": timeframe,
        "targets": results,
    }, notes


def fetch_google_data(config: dict[str, Any]) -> tuple[dict[str, Any], list[str]]:
    result: dict[str, Any] = {"search_console": None, "ga4": None}
    blockers: list[str] = []
    available, library_message = google_clients_available()
    search_console_property = config.get("search_console_property", "").strip()
    ga4_property_id = config.get("ga4_property_id", "").strip()
    key_path = config.get("google_service_account_key_path", "").strip()
    missing_values = []
    if not search_console_property:
        missing_values.append("SEO_SEARCH_CONSOLE_PROPERTY")
    if not ga4_property_id:
        missing_values.append("SEO_GA4_PROPERTY_ID")
    if not key_path:
        missing_values.append("SEO_GOOGLE_SERVICE_ACCOUNT_KEY_PATH")
    if missing_values:
        blockers.append("Missing config values: " + ", ".join(missing_values) + ".")

    key_file = Path(key_path) if key_path else None
    if key_file and not key_file.exists():
        blockers.append(
            f"SEO_GOOGLE_SERVICE_ACCOUNT_KEY_PATH points to `{key_path}`, but that file does not exist."
        )

    if not available:
        blockers.append(
            library_message + " Install them with `python3 -m pip install -r requirements-seo.txt`."
        )
    if blockers:
        return result, blockers

    try:
        from google.oauth2 import service_account
        from googleapiclient.discovery import build
    except ModuleNotFoundError:
        blockers.append(
            "Python Google API client libraries are not installed. Install them with "
            "`python3 -m pip install -r requirements-seo.txt`."
        )
        return result, blockers

    scopes = [
        "https://www.googleapis.com/auth/webmasters.readonly",
        "https://www.googleapis.com/auth/analytics.readonly",
    ]

    try:
        credentials = service_account.Credentials.from_service_account_file(
            str(key_file), scopes=scopes
        )
    except Exception as exc:
        blockers.append(f"Could not load the service account JSON key: {exc}")
        return result, blockers

    start_date, end_date = google_reporting_window(config)

    try:
        search_console = build("searchconsole", "v1", credentials=credentials, cache_discovery=False)
    except Exception:
        search_console = None

    if search_console is None:
        try:
            search_console = build("webmasters", "v3", credentials=credentials, cache_discovery=False)
        except Exception as exc:
            blockers.append(f"Could not initialize the Search Console API client: {exc}")
    if search_console is not None:
        try:
            payload = {
                "startDate": start_date.isoformat(),
                "endDate": end_date.isoformat(),
                "dimensions": ["page"],
                "rowLimit": 10,
            }
            response = (
                search_console.searchanalytics()
                .query(siteUrl=search_console_property, body=payload)
                .execute()
            )
            rows = response.get("rows", [])
            result["search_console"] = {
                "date_range": [start_date.isoformat(), end_date.isoformat()],
                "clicks": round(sum(row.get("clicks", 0) for row in rows), 2),
                "impressions": round(sum(row.get("impressions", 0) for row in rows), 2),
                "top_pages": rows[:5],
            }
        except Exception as exc:
            blockers.append(
                "Search Console API access failed. Confirm the property value is correct and "
                f"the service account has access. Error: {exc}"
            )

    try:
        analytics = build("analyticsdata", "v1beta", credentials=credentials, cache_discovery=False)
        response = (
            analytics.properties()
            .runReport(
                property=f"properties/{ga4_property_id}",
                body={
                    "dateRanges": [
                        {
                            "startDate": start_date.isoformat(),
                            "endDate": end_date.isoformat(),
                        }
                    ],
                    "metrics": [{"name": "sessions"}, {"name": "totalUsers"}, {"name": "conversions"}],
                    "dimensions": [{"name": "eventName"}],
                    "limit": 10,
                },
            )
            .execute()
        )
        rows = response.get("rows", [])
        result["ga4"] = {
            "rows": rows[:10],
            "measurement_id_configured": bool(
                config.get("analytics", {}).get("measurement_id", "").strip()
            ),
        }
    except Exception as exc:
        blockers.append(
            "GA4 Data API access failed. Confirm the numeric property ID is correct, the "
            f"Analytics Data API is enabled, and the service account has property access. Error: {exc}"
        )

    return result, blockers


def keyword_opportunities(
    config: dict[str, Any],
    page_map: dict[str, PageAudit],
    trends_data: dict[str, Any] | None = None,
) -> list[str]:
    opportunities: list[str] = []
    trend_lookup = {
        item["term"].lower(): item
        for item in (trends_data or {}).get("targets", [])
    }
    min_average_interest = int(config.get("trends", {}).get("min_average_interest", 8))
    for target in config.get("keyword_targets", []):
        path = target["path"]
        page = page_map.get(path)
        if page is None:
            continue
        primary = target["primary"].lower()
        title = page.title.lower()
        description = page.meta_description.lower()
        problems: list[str] = []
        if primary not in title:
            problems.append("primary keyword missing from title")
        if primary not in description:
            problems.append("primary keyword missing from meta description")
        if problems:
            opportunities.append(
                f"`{path}`: {', '.join(problems)} for `{target['primary']}`."
            )
        if len(opportunities) >= 5:
            break
        title_and_description = f"{title} {description}"
        for related_term in target.get("secondary", []):
            trend = trend_lookup.get(related_term.lower())
            if not trend or trend["average_interest"] < min_average_interest:
                continue
            if related_term.lower() in title_and_description:
                continue
            opportunities.append(
                f"`{path}`: demand term `{related_term}` shows directional Google Trends interest "
                f"(avg {trend['average_interest']}) but is not present in title/meta."
            )
            break
        if len(opportunities) >= 5:
            break
    return opportunities


def previous_report_metrics(report_dir: Path, today: str) -> tuple[dict[str, Any] | None, str | None]:
    historical = sorted(
        path for path in report_dir.glob("????-??-??.md") if path.stem < today
    )
    if not historical:
        return None, None
    latest = historical[-1]
    text = latest.read_text(encoding="utf-8")
    match = re.search(r"<!-- SEO_REPORT_DATA:(.*?)-->", text)
    if not match:
        return None, latest.name
    return json.loads(match.group(1)), latest.name


def build_local_metrics(
    config: dict[str, Any],
    trends_data: dict[str, Any] | None = None,
) -> tuple[dict[str, Any], list[str], list[str], list[str]]:
    pages = collect_pages()
    indexable_pages = [page for page in pages if is_indexable(page)]
    page_map = {page.path: page for page in indexable_pages}
    sitemap_metrics = read_sitemap_metrics()
    tracking = detect_tracking(config, pages)

    duplicate_titles = [
        item
        for item, count in Counter(page.title for page in indexable_pages if page.title).items()
        if count > 1
    ]
    duplicate_descriptions = [
        item
        for item, count in Counter(
            page.meta_description for page in indexable_pages if page.meta_description
        ).items()
        if count > 1
    ]

    issues: list[str] = []
    if sitemap_metrics["url_count"] != len(indexable_pages):
        issues.append(
            f"Sitemap lists {sitemap_metrics['url_count']} URLs while the repo contains {len(indexable_pages)} indexable HTML pages."
        )
    if duplicate_titles:
        issues.append(f"Found {len(duplicate_titles)} duplicate title tag values across the site.")
    if duplicate_descriptions:
        issues.append(f"Found {len(duplicate_descriptions)} duplicate meta description values across the site.")

    opportunities = keyword_opportunities(config, page_map, trends_data=trends_data)
    if not tracking["has_gtag"] and not tracking["has_gtm"]:
        issues.append("No GA4 or GTM client-side tracking snippet is present in the site code.")

    actions: list[str] = []
    if not tracking["has_gtag"] and not tracking["has_gtm"]:
        actions.append(
            "Add GA4 or GTM tagging before expecting form submissions to appear as conversions."
        )
    if duplicate_titles:
        actions.append("Resolve duplicate titles in the shared templates before adding more pages.")
    if sitemap_metrics["url_count"] != len(indexable_pages):
        actions.append("Rebuild or refresh sitemap generation so published URLs match the repo pages.")
    if opportunities:
        actions.append("Refresh title and meta copy on the highest-priority pages missing their primary keyword.")

    metrics = {
        "page_count": len(indexable_pages),
        "total_html_page_count": len(pages),
        "noindex_page_count": len(pages) - len(indexable_pages),
        "sitemap_url_count": sitemap_metrics["url_count"],
        "pages_missing_meta_description": sum(
            1 for page in indexable_pages if not page.meta_description
        ),
        "pages_missing_h1": sum(1 for page in indexable_pages if page.h1_count == 0),
        "pages_with_multiple_h1": sum(1 for page in indexable_pages if page.h1_count > 1),
        "pages_with_json_ld": sum(1 for page in indexable_pages if page.json_ld_count > 0),
        "duplicate_title_count": len(duplicate_titles),
        "duplicate_meta_description_count": len(duplicate_descriptions),
        "tracking_has_gtag": tracking["has_gtag"],
        "tracking_has_gtm": tracking["has_gtm"],
        "tracking_has_datalayer": tracking["has_datalayer"],
        "tracking_measurement_id_configured": tracking["measurement_id_configured"],
    }
    return metrics, issues, opportunities, actions


def summarize_search_demand(
    google_data: dict[str, Any],
    google_blockers: list[str],
    trends_data: dict[str, Any] | None,
    trends_notes: list[str],
) -> list[str]:
    notes: list[str] = []
    if google_data.get("search_console"):
        start_date, end_date = google_data["search_console"]["date_range"]
        notes.append(
            f"Search Console clicks ({start_date} to {end_date}): "
            f"{google_data['search_console']['clicks']}, impressions: "
            f"{google_data['search_console']['impressions']}."
        )
    elif google_blockers:
        notes.append("Search Console demand data is unavailable until the Google blockers are cleared.")

    if trends_data and trends_data.get("targets"):
        top_terms = trends_data["targets"][:3]
        term_summary = ", ".join(
            f"`{item['term']}` (avg {item['average_interest']}, latest {item['latest_interest']})"
            for item in top_terms
        )
        notes.append(
            "Google Trends directional checks "
            f"({trends_data['timeframe']}, {trends_data['geo']}, compared against "
            f"`{trends_data['seed_keyword']}`) highlight: {term_summary}."
        )
    elif trends_notes:
        notes.extend(f"Google Trends note: {note}" for note in trends_notes[:3])

    return notes


def summarize_crawlability(
    live_checks: dict[str, dict[str, Any]],
    local_metrics: dict[str, Any],
    previous_metrics: dict[str, Any] | None,
) -> list[str]:
    notes = [
        f"Repo audit found {local_metrics['page_count']} HTML pages and {local_metrics['sitemap_url_count']} sitemap URLs.",
        (
            f"Live checks: homepage {live_checks['homepage'].get('status')}, robots.txt "
            f"{live_checks['robots'].get('status')}, sitemap.xml {live_checks['sitemap'].get('status')}."
        ),
    ]
    if previous_metrics:
        page_delta = local_metrics["page_count"] - previous_metrics.get("page_count", local_metrics["page_count"])
        sitemap_delta = local_metrics["sitemap_url_count"] - previous_metrics.get(
            "sitemap_url_count", local_metrics["sitemap_url_count"]
        )
        notes.append(
            f"Since the previous report, page count changed by {page_delta:+d} and sitemap URL count changed by {sitemap_delta:+d}."
        )
    return notes


def build_missing_google_checklist(config: dict[str, Any]) -> list[str]:
    site_domain = config.get("site_domain", "").strip() or "your-domain.com"
    service_account_path = config.get("google_service_account_key_path", "").strip() or "/absolute/path/to/google-seo-service-account.json"
    return [
        f"Search Console property value: create a Domain property for `{site_domain}` and set `SEO_SEARCH_CONSOLE_PROPERTY=sc-domain:{site_domain}`.",
        "GA4 property ID: in Google Analytics go to Admin > Property details and copy the numeric Property ID into `SEO_GA4_PROPERTY_ID`.",
        "Service account JSON key: in Google Cloud create a service account, create a JSON key, store it outside the repo, and set `SEO_GOOGLE_SERVICE_ACCOUNT_KEY_PATH` to its absolute path.",
        "Search Console access: add the service account email from the JSON key as a Full user on the Search Console property. Owner access is recommended if you want broader property administration.",
        "GA4 access: add the same service account email to the GA4 property with Viewer or Analyst access.",
        "Enable APIs in the Google Cloud project used by the service account: Search Console API and Google Analytics Data API.",
        f"Install the Python dependencies with `python3 -m pip install -r requirements-seo.txt` before expecting Google API fetches to work on this machine.",
        f"Suggested local key location: `{service_account_path}`.",
    ]


def render_report(config: dict[str, Any], reused: bool = False) -> str:
    today = date.today().isoformat()
    report_dir = Path(config["report_dir"])
    report_dir.mkdir(parents=True, exist_ok=True)

    previous_metrics, previous_name = previous_report_metrics(report_dir, today)
    live_checks = {
        "homepage": check_live_endpoint(config["site_url"]),
        "robots": check_live_endpoint(config["site_url"].rstrip("/") + "/robots.txt"),
        "sitemap": check_live_endpoint(config["site_url"].rstrip("/") + "/sitemap.xml"),
    }

    google_data, google_blockers = fetch_google_data(config)
    trends_data, trends_notes = fetch_trends_data(config)
    local_metrics, issues, opportunities, actions = build_local_metrics(config, trends_data=trends_data)
    live_blockers = [
        f"Could not reach {label} at `{url}`: {check.get('error', 'unknown error')}."
        for label, url, check in (
            ("the live homepage", config["site_url"], live_checks["homepage"]),
            ("robots.txt", config["site_url"].rstrip("/") + "/robots.txt", live_checks["robots"]),
            ("sitemap.xml", config["site_url"].rstrip("/") + "/sitemap.xml", live_checks["sitemap"]),
        )
        if not check["ok"]
    ]
    crawlability_notes = summarize_crawlability(live_checks, local_metrics, previous_metrics)
    metrics_snapshot = {
        **local_metrics,
        "live_homepage_ok": live_checks["homepage"]["ok"],
        "live_robots_ok": live_checks["robots"]["ok"],
        "live_sitemap_ok": live_checks["sitemap"]["ok"],
        "reused_existing_report": reused,
    }

    key_findings = []
    if issues:
        key_findings.extend(issues[:3])
    else:
        key_findings.append("Local crawlability and metadata checks passed without critical template issues.")
    if live_blockers:
        key_findings.append("Live site checks failed, so external crawlability validation is incomplete.")
    if google_blockers:
        key_findings.append("Google data is blocked until the missing credentials or libraries are supplied.")
    if trends_data and trends_data.get("targets"):
        key_findings.append("Search Console demand is now complemented with directional Google Trends keyword checks.")

    conversion_notes = []
    if local_metrics["tracking_has_gtag"] or local_metrics["tracking_has_gtm"]:
        conversion_notes.append("A client-side analytics container was detected in the codebase.")
    else:
        conversion_notes.append("No GA4 or GTM tag was detected in the shipped site code.")
    if local_metrics["tracking_measurement_id_configured"]:
        conversion_notes.append("A GA4 measurement ID is configured in repo settings.")
    else:
        conversion_notes.append("No GA4 measurement ID is configured in repo settings yet.")
    if google_data.get("ga4"):
        conversion_notes.append("GA4 Data API access succeeded for the configured property.")
    elif google_blockers:
        conversion_notes.append("GA4 conversion metrics were skipped because Google setup is incomplete.")

    highest_leverage_actions = actions[:5] or [
        "Expand country-specific export pages for priority markets and keep internal links pointed to the most relevant product pages."
    ]

    report_lines = [
        f"# SEO Report - {today}",
        "",
        "## Status",
        f"- Report mode: {'reused existing report' if reused else 'generated new report'}",
        f"- Site: `{config['site_url']}`",
        f"- Google Search Console configured: {'yes' if config.get('search_console_property') else 'no'}",
        f"- GA4 property configured: {'yes' if config.get('ga4_property_id') else 'no'}",
        "",
        "## Metrics Snapshot",
    ]
    for key, value in metrics_snapshot.items():
        report_lines.append(f"- {key}: {value}")

    report_lines.extend(["", "## Key SEO Findings"])
    report_lines.extend(f"- {item}" for item in key_findings)

    report_lines.extend(["", "## Indexing And Crawlability Changes"])
    report_lines.extend(f"- {item}" for item in crawlability_notes)
    if google_data.get("search_console"):
        report_lines.append("- Search Console demand data is available for this run.")
    elif google_blockers:
        report_lines.append("- Google indexing and query data is unavailable until the blockers below are cleared.")

    report_lines.extend(["", "## Search Demand Signals"])
    report_lines.extend(
        f"- {item}"
        for item in summarize_search_demand(google_data, google_blockers, trends_data, trends_notes)
    )

    report_lines.extend(["", "## Keyword Opportunities"])
    if opportunities:
        report_lines.extend(f"- {item}" for item in opportunities)
    else:
        report_lines.append("- No high-confidence keyword gaps were detected in the configured priority pages.")

    report_lines.extend(["", "## Conversion Tracking Status"])
    report_lines.extend(f"- {item}" for item in conversion_notes)

    report_lines.extend(["", "## Highest-Leverage Next Actions"])
    report_lines.extend(f"- {item}" for item in highest_leverage_actions)

    report_lines.extend(["", "## Blockers"])
    all_blockers = live_blockers + google_blockers
    if all_blockers:
        report_lines.extend(f"- {item}" for item in all_blockers)
    else:
        report_lines.append("- No blocking live-site, credential, or library issues were detected.")

    if all_blockers:
        report_lines.extend(["", "## Missing Google Setup Checklist"])
        report_lines.extend(f"- {item}" for item in build_missing_google_checklist(config))

    report_lines.extend(
        [
            "",
            f"<!-- SEO_REPORT_DATA:{json.dumps(metrics_snapshot, sort_keys=True, separators=(',', ':'))} -->",
        ]
    )
    if previous_name:
        report_lines.append(f"<!-- SEO_PREVIOUS_REPORT:{previous_name} -->")

    return "\n".join(report_lines) + "\n"


def main() -> int:
    config, _ = load_config()
    print(render_report(config))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
