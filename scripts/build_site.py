from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUILD_DIR = ROOT / "_site"
ROOT_FILES = ["index.html", "styles.css", "script.js", "robots.txt", "sitemap.xml"]
OPTIONAL_FILES = ["CNAME"]
SITE_DIRS = [
    "assets",
    "export-markets",
    "industrial-minerals-exporter-india",
    "operations",
    "privacy-policy",
    "terms-disclaimer",
]
ACTIVE_PRODUCT_DIRS = [
    "silica-sand",
    "quartz-sand-for-ceramics",
    "feldspar",
    "silica-flour",
]
ACTIVE_BLOG_DIRS = [
    "quartz-sand-supplier-india-vietnam-buyers-guide",
    "potassium-vs-sodium-feldspar-import-buyer-guide",
    "silica-sand-import-checklist-glass-foundry-filtration",
    "potassium-feldspar-supplier-for-ceramic-tiles",
    "quartz-powder-supplier-for-engineered-stone",
    "silica-sand-exporter-from-india",
    "how-to-check-tds-and-sample-coa-before-mineral-import",
]


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


def validate_inputs() -> list[str]:
    missing: list[str] = []
    for name in ROOT_FILES + SITE_DIRS + ["blog/index.html", "products/index.html"]:
        if not (ROOT / name).exists():
            missing.append(name)
    for name in ACTIVE_BLOG_DIRS:
        if not (ROOT / "blog" / name / "index.html").exists():
            missing.append(f"blog/{name}/index.html")
    for name in ACTIVE_PRODUCT_DIRS:
        if not (ROOT / "products" / name / "index.html").exists():
            missing.append(f"products/{name}/index.html")
    return missing


def build_site() -> None:
    if BUILD_DIR.exists():
        shutil.rmtree(BUILD_DIR)
    BUILD_DIR.mkdir(parents=True, exist_ok=True)

    for name in ROOT_FILES + OPTIONAL_FILES + SITE_DIRS:
        source = ROOT / name
        if source.exists():
            copy_path(source, BUILD_DIR / name)

    copy_path(ROOT / "blog" / "index.html", BUILD_DIR / "blog" / "index.html")
    for slug in ACTIVE_BLOG_DIRS:
        copy_path(ROOT / "blog" / slug, BUILD_DIR / "blog" / slug)

    copy_path(ROOT / "products" / "index.html", BUILD_DIR / "products" / "index.html")
    for slug in ACTIVE_PRODUCT_DIRS:
        copy_path(ROOT / "products" / slug, BUILD_DIR / "products" / slug)

    expected = [BUILD_DIR / name for name in ROOT_FILES + SITE_DIRS]
    expected.extend([BUILD_DIR / "blog" / "index.html", BUILD_DIR / "products" / "index.html"])
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
