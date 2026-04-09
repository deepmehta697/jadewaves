from __future__ import annotations

import argparse
import shutil
from datetime import date
from pathlib import Path

from config import load_config
from generate_report import render_report


def sync_latest(today_report: Path, latest_report: Path) -> None:
    latest_report.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(today_report, latest_report)


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate or reuse today's SEO report.")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Regenerate today's report even if it already exists.",
    )
    args = parser.parse_args()

    config, _ = load_config()
    report_dir = Path(config["report_dir"])
    report_dir.mkdir(parents=True, exist_ok=True)

    today = date.today().isoformat()
    today_report = report_dir / f"{today}.md"
    latest_report = report_dir / "latest.md"

    if today_report.exists() and not args.force:
        sync_latest(today_report, latest_report)
        print(f"Reused existing report: {today_report}")
        print(f"Updated latest report symlink copy: {latest_report}")
        return 0

    report = render_report(config, reused=False)
    today_report.write_text(report, encoding="utf-8")
    sync_latest(today_report, latest_report)

    print(f"Generated report: {today_report}")
    print(f"Updated latest report copy: {latest_report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
