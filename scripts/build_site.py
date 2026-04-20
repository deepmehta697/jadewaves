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
    "blog",
    "blogs",
    "bentonite",
    "contact-1",
    "copper-slag",
    "export-markets",
    "feldspar",
    "fly-ash",
    "hear-from-ceo",
    "industrial-minerals-exporter-india",
    "kaolin--china-clay",
    "operations",
    "privacy-policy",
    "products",
    "quartz-sand-for-ceramics",
    "salt",
    "silica-flour",
    "silica-sand",
    "talc",
    "terms-disclaimer",
]


def generated_redirect_dirs() -> list[str]:
    sys.path.insert(0, str(ROOT))
    import generate_site

    dirs = {product["slug"] for product in generate_site.PRODUCTS}
    dirs.update(Path(redirect["path"]).parts[0] for redirect in generate_site.all_redirects())
    return sorted(dirs)


def site_dirs() -> list[str]:
    return sorted({*SITE_DIRS, *generated_redirect_dirs()})


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
    for name in ROOT_FILES + site_dirs():
        if not (ROOT / name).exists():
            missing.append(name)
    return missing


def build_site() -> None:
    if BUILD_DIR.exists():
        shutil.rmtree(BUILD_DIR)
    BUILD_DIR.mkdir(parents=True, exist_ok=True)

    dirs = site_dirs()
    for name in ROOT_FILES + OPTIONAL_FILES + dirs:
        source = ROOT / name
        if source.exists():
            copy_path(source, BUILD_DIR / name)

    expected = [BUILD_DIR / name for name in ROOT_FILES + dirs]
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
