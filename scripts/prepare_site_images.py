"""Create responsive WebP copies for images used by generated site pages."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

from PIL import Image, ImageOps


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'assets' / 'responsive'


def main():
    sources = set()
    manifest_path = OUTPUT / 'manifest.json'
    prior = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    originals = {variant['src'].lstrip('/'): source.lstrip('/') for source, info in prior.items() for variant in info.get('variants', [])}
    for page in [ROOT / 'index.html', *ROOT.glob('products/**/index.html'), *ROOT.glob('blog/**/index.html'), *[ROOT / name / 'index.html' for name in ['operations', 'hear-from-ceo', 'export-markets', 'industrial-minerals-exporter-india']]]:
        if not page.exists():
            continue
        for src in re.findall(r'<img\b[^>]*\bsrc="([^"]+)"', page.read_text()):
            relative = src.split('?', 1)[0].lstrip('/')
            relative = originals.get(relative, relative)
            if relative.startswith('assets/') and not relative.startswith('assets/responsive/'):
                sources.add(relative)
    manifest = {}
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for source in sorted(sources):
        with Image.open(ROOT / source) as original:
            im = ImageOps.exif_transpose(original)
            width, height = im.size
            record = {'width': width, 'height': height}
            if 'logo' not in source:
                key = Path(source).stem + '-' + hashlib.sha256(source.encode()).hexdigest()[:6]
                sizes = sorted(set(min(width, requested) for requested in [160, 480, 960, 1600]))
                variants = []
                for size in sizes:
                    scaled = im.convert('RGB' if im.mode != 'RGBA' else 'RGBA').resize((size, round(height * size / width)), Image.Resampling.LANCZOS)
                    filename = f'{key}-{size}.webp'
                    scaled.save(OUTPUT / filename, 'WEBP', quality=82, method=6)
                    variants.append({'src': '/assets/responsive/' + filename, 'width': size})
                record['variants'] = variants
            manifest['/' + source] = record
    manifest_path.write_text(json.dumps(manifest, indent=2) + '\n')
    print(f'Prepared responsive images for {len(manifest)} source assets.')


if __name__ == '__main__':
    main()
