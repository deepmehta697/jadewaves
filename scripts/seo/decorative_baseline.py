"""One-shot, read-only GSC/GA4 baseline. No schedules, writes or indexing requests."""
from __future__ import annotations

import argparse
from datetime import date, datetime, timedelta, timezone
import json
from pathlib import Path
import re
import sys
from urllib.parse import quote
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts/seo'))
from config import load_config

BASE = 'https://jadewavesenterprise.com'
SLUGS = ('glass-chips', 'grout-sand', 'colour-coated-silica-sand', 'pebbles')
PATHS = tuple('/products/' + slug + '/' for slug in SLUGS)
URLS = tuple(BASE + path for path in PATHS)
SCOPES = ('https://www.googleapis.com/auth/webmasters.readonly',
          'https://www.googleapis.com/auth/analytics.readonly')


def reporting_window(as_of: date):
    end = as_of - timedelta(days=1)
    return (end - timedelta(days=27)).isoformat(), end.isoformat()


def search_request(start, end, dimensions, export_only=False, targeted=True):
    filters = []
    if targeted:
        filters.append({'dimension': 'page', 'operator': 'includingRegex',
                        'expression': '^(' + '|'.join(re.escape(url) for url in URLS) + ')$'})
    if export_only:
        filters.append({'dimension': 'country', 'operator': 'notEquals', 'expression': 'ind'})
    body = {'startDate': start, 'endDate': end, 'dimensions': dimensions,
            'type': 'web', 'dataState': 'final', 'aggregationType': 'auto',
            'rowLimit': 1000 if targeted else 25, 'startRow': 0}
    if filters:
        body['dimensionFilterGroups'] = [{'groupType': 'and', 'filters': filters}]
    return body


def landing_request(start, end):
    return {'dateRanges': [{'startDate': start, 'endDate': end}],
            'dimensions': [{'name': 'landingPage'}, {'name': 'sessionDefaultChannelGroup'}],
            'metrics': [{'name': 'sessions'}, {'name': 'totalUsers'}],
            'dimensionFilter': {'andGroup': {'expressions': [
                {'filter': {'fieldName': 'hostName', 'stringFilter': {'matchType': 'EXACT', 'value': 'jadewavesenterprise.com'}}},
                {'filter': {'fieldName': 'landingPage', 'inListFilter': {'values': list(PATHS)}}},
                {'filter': {'fieldName': 'sessionDefaultChannelGroup', 'stringFilter': {'matchType': 'EXACT', 'value': 'Organic Search'}}},
            ]}}, 'limit': '1000'}


def summarize_pages(rows):
    by_url = {row['keys'][0]: row for row in rows}
    return [{'url': url, 'clicks': by_url.get(url, {}).get('clicks', 0),
             'impressions': by_url.get(url, {}).get('impressions', 0),
             'averagePosition': by_url.get(url, {}).get('position'),
             'hasReportedRow': url in by_url} for url in URLS]


def collect(session, site, ga4_property, as_of):
    assert site == BASE + '/', 'Unexpected Search Console property'
    assert str(ga4_property) == '527330659', 'Unexpected GA4 property'
    start, end = reporting_window(as_of)
    result = {'capturedAt': datetime.now(timezone.utc).isoformat(),
              'window': {'start': start, 'end': end, 'days': 28, 'gscTimezone': 'America/Los_Angeles', 'gscDataState': 'final'},
              'property': site, 'ga4Property': str(ga4_property), 'search': {}, 'inspection': [], 'errors': []}

    def request(label, endpoint, body):
        try:
            response = session.post(endpoint, json=body, timeout=30)
            if response.status_code != 200:
                result['errors'].append({'component': label, 'httpStatus': response.status_code})
                return None
            return response.json()
        except Exception as exc:
            result['errors'].append({'component': label, 'type': type(exc).__name__})
            return None

    endpoint = 'https://www.googleapis.com/webmasters/v3/sites/' + quote(site, safe='') + '/searchAnalytics/query'
    for label, dimensions, export_only, targeted in [
        ('allMarketsPages', ['page'], False, True),
        ('allMarketsQueries', ['page', 'query'], False, True),
        ('excludingIndiaPages', ['page'], True, True),
        ('excludingIndiaQueries', ['page', 'query'], True, True),
        ('sitewideQueriesContextOnly', ['query'], False, False),
    ]:
        data = request(label, endpoint, search_request(start, end, dimensions, export_only, targeted))
        result['search'][label] = data
        if data is None:
            break
    if result['search'].get('allMarketsPages') is not None:
        result['pageSummary'] = summarize_pages(result['search']['allMarketsPages'].get('rows', []))
    # A GSC failure ends that service's bounded batch, including inspections.
    for url in (() if result['errors'] else URLS):
        data = request('inspection:' + url, 'https://searchconsole.googleapis.com/v1/urlInspection/index:inspect',
                       {'inspectionUrl': url, 'siteUrl': site, 'languageCode': 'en-US'})
        if data is None:
            break  # No loops on quota, temporary errors or permission failures.
        status = data.get('inspectionResult', {}).get('indexStatusResult', {})
        result['inspection'].append({'url': url, **{key: status.get(key) for key in [
            'verdict', 'coverageState', 'lastCrawlTime', 'googleCanonical', 'userCanonical']}})
    result['organicLandings'] = request('organicLandings', 'https://analyticsdata.googleapis.com/v1beta/properties/' + str(ga4_property) + ':runReport', landing_request(start, end))
    result['limitations'] = [
        'GSC uses finalized Pacific-time dates; the newest days may not yet be available.',
        'Empty rows mean no reportable data, not a rank of zero or proof of zero demand.',
        'Query rows may omit anonymized/low-volume queries; top-row limits apply.',
        'All-markets and excluding-India views are separate; GA4 uses its property timezone.',
        'Sitewide query context is not evidence of rankings for the new pages.',
        'Organic landing sessions are not inquiries. Only server-confirmed forms emit generate_lead; opening email drafts does not.',
        'No causal ranking/performance lift can be inferred from this baseline.',
    ]
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--as-of', type=date.fromisoformat, default=datetime.now(ZoneInfo('America/Los_Angeles')).date())
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    config, _ = load_config()
    from google.oauth2 import service_account
    from google.auth.transport.requests import AuthorizedSession
    credentials = service_account.Credentials.from_service_account_file(config['google_service_account_key_path'], scopes=list(SCOPES))
    with AuthorizedSession(credentials) as session:
        result = collect(session, config['search_console_property'], config['ga4_property_id'], args.as_of)
    target = args.output or ROOT / 'tmp/seo-decorative-baseline' / (args.as_of.isoformat() + '.json')
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'saved': str(target), 'window': result['window'],
                      'pageSummary': result.get('pageSummary'), 'inspection': result['inspection'],
                      'organicLandingRows': (result.get('organicLandings') or {}).get('rowCount'),
                      'errors': result['errors']}, indent=2))
    return 1 if result['errors'] else 0


if __name__ == '__main__': raise SystemExit(main())
