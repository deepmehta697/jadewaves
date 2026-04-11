from __future__ import annotations

import json
import os
from copy import deepcopy
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CONFIG: dict[str, Any] = {
    "site_url": "https://jadewavesenterprise.com",
    "site_name": "Jade Waves Enterprise",
    "site_domain": "jadewavesenterprise.com",
    "github_repo": "deepmehta697/jadewaves",
    "report_dir": "reports/seo",
    "production_build_command": "python3 scripts/build_site.py",
    "regenerate_command": "python3 generate_site.py",
    "search_console_property": "",
    "ga4_property_id": "",
    "google_service_account_key_path": "",
    "analytics": {
        "measurement_id": "",
        "form_submit_event_name": "submit_lead_form",
        "lead_event_name": "generate_lead",
    },
    "trends": {
        "enabled": True,
        "geo": "",
        "timeframe": "today 3-m",
        "seed_keyword": "industrial minerals supplier",
        "max_terms": 8,
        "min_average_interest": 8,
        "targets": [],
    },
    "priority_pages": [
        "/",
        "/products/",
        "/products/quartz-sand-for-ceramics/",
        "/products/feldspar/",
        "/products/silica-sand/",
        "/products/salt/",
        "/products/bentonite/",
    ],
    "keyword_targets": [],
}

DEFAULT_SHARED_SERVICE_ACCOUNT_PATH = Path.home() / ".config" / "jadewaves" / "google-seo-service-account.json"

ENV_TO_PATH = {
    "SEO_SITE_URL": ("site_url",),
    "SEO_SITE_NAME": ("site_name",),
    "SEO_REPORT_DIR": ("report_dir",),
    "SEO_GITHUB_REPO": ("github_repo",),
    "SEO_SEARCH_CONSOLE_PROPERTY": ("search_console_property",),
    "SEO_GA4_PROPERTY_ID": ("ga4_property_id",),
    "SEO_GOOGLE_SERVICE_ACCOUNT_KEY_PATH": ("google_service_account_key_path",),
    "SEO_GA4_MEASUREMENT_ID": ("analytics", "measurement_id"),
    "SEO_ANALYTICS_FORM_SUBMIT_EVENT": ("analytics", "form_submit_event_name"),
    "SEO_ANALYTICS_LEAD_EVENT": ("analytics", "lead_event_name"),
}


def deep_merge(base: dict[str, Any], incoming: dict[str, Any]) -> dict[str, Any]:
    merged = deepcopy(base)
    for key, value in incoming.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = deep_merge(merged[key], value)
        else:
            merged[key] = value
    return merged


def set_nested(config: dict[str, Any], path: tuple[str, ...], value: str) -> None:
    current = config
    for key in path[:-1]:
        current = current.setdefault(key, {})
    current[path[-1]] = value


def load_config() -> tuple[dict[str, Any], Path]:
    config = deepcopy(DEFAULT_CONFIG)
    config_path = Path(os.environ.get("SEO_CONFIG_PATH", ROOT / "config" / "seo.config.json"))
    if config_path.exists():
        config = deep_merge(config, json.loads(config_path.read_text(encoding="utf-8")))

    local_config_path = config_path.with_name(f"{config_path.stem}.local{config_path.suffix}")
    if local_config_path.exists():
        config = deep_merge(config, json.loads(local_config_path.read_text(encoding="utf-8")))

    for env_name, path in ENV_TO_PATH.items():
        value = os.environ.get(env_name)
        if value:
            set_nested(config, path, value)

    report_dir = Path(config["report_dir"])
    config["report_dir"] = str(report_dir if report_dir.is_absolute() else ROOT / report_dir)

    key_path = config.get("google_service_account_key_path", "").strip()
    if not key_path and DEFAULT_SHARED_SERVICE_ACCOUNT_PATH.exists():
        key_path = str(DEFAULT_SHARED_SERVICE_ACCOUNT_PATH)
        config["google_service_account_key_path"] = key_path
    if key_path:
        service_account_path = Path(key_path)
        config["google_service_account_key_path"] = str(
            service_account_path
            if service_account_path.is_absolute()
            else (ROOT / service_account_path).resolve()
        )

    return config, config_path
