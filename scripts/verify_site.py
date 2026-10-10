"""Check generated routes, documents, semantics, and redesign invariants.

This is a source/build check; it does not replace browser visual review.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self, markup):
        super().__init__()
        self.tags = []
        self.ids = []
        self.headings = 0
        self.feed(markup)

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        self.tags.append((tag, attrs))
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'h1':
            self.headings += 1


def load_generator():
    import sys
    sys.path.insert(0, str(ROOT))
    spec = importlib.util.spec_from_file_location('site_generator', ROOT / 'generate_site.py')
    generator = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(generator)
    return generator


def verify(root):
    g = load_generator()
    routes = ['/', '/products/', '/blog/', '/operations/', '/export-markets/', '/hear-from-ceo/', '/industrial-minerals-exporter-india/', '/privacy-policy/', '/terms-disclaimer/']
    routes += [f'/products/{p["slug"]}/' for p in g.PRODUCTS]
    routes += [f'/blog/{p["slug"]}/' for p in g.BLOGS]
    errors = []
    documents = set()
    cached = {}
    sitemap = ET.parse(root / 'sitemap.xml')
    sitemap_routes = {urlsplit(node.text).path for node in sitemap.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')}
    if sitemap_routes != set(routes):
        errors.append(f'Sitemap differs from production pages: {sitemap_routes ^ set(routes)}')
    for route in routes:
        path = root / route.strip('/') / 'index.html'
        if not path.exists():
            errors.append(f'{route}: missing page')
            continue
        markup = path.read_text()
        page = Page(markup)
        cached[route] = page
        canonical = next((attrs.get('href') for tag, attrs in page.tags if tag == 'link' and attrs.get('rel') == 'canonical'), '')
        if canonical != g.BASE_URL + route:
            errors.append(f'{route}: wrong canonical {canonical}')
        if page.headings != 1:
            errors.append(f'{route}: expected one h1, found {page.headings}')
        if len(page.ids) != len(set(page.ids)):
            errors.append(f'{route}: duplicate element IDs')
        if 'main-content' not in page.ids:
            errors.append(f'{route}: no server-rendered skip target')
        schemas = []
        for raw in re.findall(r'<script type="application/ld\+json">(.*?)</script>', markup, re.S):
            try:
                schemas.extend(json.loads(raw))
            except (ValueError, TypeError):
                errors.append(f'{route}: invalid JSON-LD')
        if not schemas:
            errors.append(f'{route}: missing JSON-LD')
        schema_types = {item.get('@type') for item in schemas if isinstance(item, dict)}
        if route.startswith('/products/') and route != '/products/' and not {'Product', 'FAQPage', 'BreadcrumbList'} <= schema_types:
            errors.append(f'{route}: missing product schema')
        if route.startswith('/blog/') and route != '/blog/' and 'BlogPosting' not in schema_types:
            errors.append(f'{route}: missing article schema')
        if any(term in markup for term in ['data-route-network', '<canvas', 'data-parallax', 'autoplay']):
            errors.append(f'{route}: obsolete decorative motion or autoplay')
        forms = [attrs for tag, attrs in page.tags if tag == 'form' and 'data-inquiry-form' in attrs]
        if route.startswith('/products/') and route != '/products/' and not forms:
            errors.append(f'{route}: missing contextual form')
        if forms:
            names = {attrs.get('name') for tag, attrs in page.tags if tag in {'input', 'select', 'textarea'}}
            required = {'request_type', 'product', 'name', 'email', 'application', 'destination', 'volume', 'packing_size', 'notes', 'company_website'}
            if not required <= names:
                errors.append(f'{route}: missing inquiry fields {required - names}')
            if not all(attrs.get('data-inquiry-endpoint') for attrs in forms):
                errors.append(f'{route}: missing inquiry endpoint')
        for tag, attrs in page.tags:
            if tag == 'img' and ('alt' not in attrs or not attrs.get('width') or not attrs.get('height')):
                errors.append(f'{route}: image lacks alt or intrinsic dimensions {attrs.get("src")}')
            for key in ('href', 'src', 'poster'):
                reference = attrs.get(key)
                if not reference:
                    continue
                url = urlsplit(reference)
                if url.scheme or url.netloc:
                    continue
                # Generated base element points to /, including on deep routes.
                relative = unquote(url.path).lstrip('/')
                target = root / relative
                if url.path in ('', './'):
                    target = root
                if target.is_dir():
                    target /= 'index.html'
                if not target.exists():
                    errors.append(f'{route}: missing {key} target {reference}')
                elif url.fragment:
                    if target.suffix == '.html' and url.fragment not in Page(target.read_text()).ids:
                        errors.append(f'{route}: missing anchor {reference}')
                if target.suffix == '.pdf':
                    documents.add(str(target.relative_to(root)))
            if attrs.get('srcset'):
                for entry in attrs['srcset'].split(','):
                    if entry.strip().startswith('/'):
                        errors.append(f'{route}: responsive candidate ignores project base {entry.strip()}')
                    target = root / entry.strip().split()[0].lstrip('/')
                    if not target.exists():
                        errors.append(f'{route}: missing responsive image {target}')
    css = (root / 'styles.css').read_text()
    js = (root / 'script.js').read_text()
    for banned in ('backdrop-filter', 'radial-gradient', 'border-radius: 999', 'requestAnimationFrame', 'getContext("2d")'):
        if banned in css + js:
            errors.append(f'Design system retains {banned}')
    if ':focus-visible' not in css or 'prefers-reduced-motion' not in css:
        errors.append('Missing accessibility styling')
    if len(css.splitlines()) > 1600:
        errors.append('CSS has not been consolidated')
    for error in sorted(set(errors)):
        print('FAIL', error)
    if errors:
        raise SystemExit(1)
    print(f'PASS: {len(routes)} active pages; {len(documents)} linked technical documents; local links, anchors, images, forms, structured data, and design invariants.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', type=Path, default=ROOT)
    args = parser.parse_args()
    verify(args.root)
