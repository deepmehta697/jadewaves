"""Attach intrinsic sizes and responsive sources to authored image markup."""

import json
import re
from pathlib import Path


MANIFEST_PATH = Path(__file__).resolve().parents[1] / 'assets' / 'responsive' / 'manifest.json'


def enhance_images(markup):
    if not MANIFEST_PATH.exists():
        return markup
    manifest = json.loads(MANIFEST_PATH.read_text())

    def enhance(match):
        tag = match.group(0)
        source = re.search(r'\bsrc="([^"]+)"', tag)
        info = manifest.get('/' + source.group(1).lstrip('/')) if source else None
        if not info:
            return tag
        tag = re.sub(r'\s+(width|height|srcset|sizes|decoding)="[^"]*"', '', tag)
        attributes = f' width="{info["width"]}" height="{info["height"]}" decoding="async"'
        variants = info.get('variants')
        if variants:
            # Default to a practical desktop size; srcset serves a smaller copy
            # on mobile while the manifest retains original intrinsic ratio.
            default = next((item['src'] for item in variants if item['width'] >= 960), variants[-1]['src'])
            tag = re.sub(r'\bsrc="[^"]+"', f'src="{default}"', tag)
            srcset = ', '.join(f'{item["src"]} {item["width"]}w' for item in variants)
            full_bleed = 'ml-hero-media' in tag
            thumbnail = 'ml-thumbnail' in tag
            sizes = '(max-width: 640px) 64px, 80px' if thumbnail else ('100vw' if full_bleed else '(max-width: 640px) 100vw, (max-width: 960px) 70vw, 50vw')
            attributes += f' srcset="{srcset}" sizes="{sizes}"'
        return tag.rstrip(' />') + attributes + ' />'

    return re.sub(r'<img\b[^>]*>', enhance, markup)
