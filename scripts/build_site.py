from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
BUILD_DIR = ROOT / "_site"
ROOT_FILES = ["index.html", "styles.css", "script.js", "robots.txt", "sitemap.xml"]
OPTIONAL_FILES = ["CNAME"]
SITE_DIRS = [
    "assets",
    "blog",
    "export-markets",
    "hear-from-ceo",
    "industrial-minerals-exporter-india",
    "operations",
    "privacy-policy",
    "products",
    "terms-disclaimer",
]
EXCLUDED_TOP_LEVEL_DIRS = {
    ".git",
    ".github",
    "_site",
    "__pycache__",
    "config",
    "docs",
    "reports",
    "scripts",
    "tmp",
}


def run_regeneration() -> None:
    result = subprocess.run([sys.executable, "generate_site.py"], cwd=ROOT)
    if result.returncode != 0:
        raise SystemExit(result.returncode)


def copy_path(source: Path, target: Path) -> None:
    if source.is_dir():
        shutil.copytree(source, target, dirs_exist_ok=True)
    else:
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)


def publishable_root_dirs() -> list[Path]:
    dirs: list[Path] = []
    for path in ROOT.iterdir():
        if not path.is_dir():
            continue
        if path.name.startswith(".") or path.name in EXCLUDED_TOP_LEVEL_DIRS:
            continue
        if path.name in SITE_DIRS:
            dirs.append(path)
            continue
        if any(child.name == "index.html" for child in path.rglob("index.html")):
            dirs.append(path)
    return sorted(dirs, key=lambda item: item.name)


def validate_inputs() -> list[str]:
    missing: list[str] = []
    for name in ROOT_FILES:
        if not (ROOT / name).exists():
            missing.append(name)
    for path in publishable_root_dirs():
        if not path.exists():
            missing.append(path.name)
    return missing


def sitemap_output_targets() -> list[Path]:
    sitemap_path = ROOT / "sitemap.xml"
    if not sitemap_path.exists():
        return []

    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    root = ET.fromstring(sitemap_path.read_text(encoding="utf-8"))
    targets: list[Path] = []

    for loc in root.findall("sm:url/sm:loc", ns):
        if not loc.text:
            continue
        parsed = urlparse(loc.text)
        path = parsed.path.rstrip("/")
        if not path:
            targets.append(BUILD_DIR / "index.html")
            continue
        segments = [segment for segment in path.split("/") if segment]
        targets.append(BUILD_DIR.joinpath(*segments) / "index.html")

    return targets


def build_site() -> None:
    if BUILD_DIR.exists():
        shutil.rmtree(BUILD_DIR)
    BUILD_DIR.mkdir(parents=True, exist_ok=True)

    for name in ROOT_FILES + OPTIONAL_FILES:
        source = ROOT / name
        if source.exists():
            copy_path(source, BUILD_DIR / name)

    for source in publishable_root_dirs():
        copy_path(source, BUILD_DIR / source.name)

    expected = [BUILD_DIR / name for name in ROOT_FILES]
    expected.extend(BUILD_DIR / path.name for path in publishable_root_dirs())
    expected.extend(sitemap_output_targets())
    missing_outputs = [str(path.relative_to(ROOT)) for path in expected if not path.exists()]
    if missing_outputs:
        raise SystemExit(
            "Build completed but missing output paths:\n- " + "\n- ".join(missing_outputs)
        )


def main() -> int:
    parser = argparse.ArgumentParser(description="Assemble the production Pages artifact.")
    parser.add_argument(
        "--regenerate",
        action="store_true",
        help="Regenerate site assets with generate_site.py before assembling _site.",
    )
    args = parser.parse_args()

    if args.regenerate:
        run_regeneration()

    missing_inputs = validate_inputs()
    if missing_inputs:
        raise SystemExit("Missing required site inputs:\n- " + "\n- ".join(missing_inputs))

    build_site()
    print(f"Built static site artifact at {BUILD_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
