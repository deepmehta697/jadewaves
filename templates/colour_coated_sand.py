"""Approved standalone decorative sand page; no preview/PDF/runtime dependencies."""
import json
from html import escape
from pathlib import Path
import re
from templates import decorative_products, decorative_inquiry

ROOT = Path(__file__).resolve().parents[1]
PATH = '/products/colour-coated-silica-sand/'
PRODUCT = {
    'slug': 'colour-coated-silica-sand', 'name': 'Colour-Coated Silica Sand',
    'family': 'Decorative Range', 'forms': ['Six colours', '0.5–1 mm'],
    'industries': ['Decorative finishes'],
    'applications': ['Flooring', 'Surface finishes', 'Decoration'],
    'specs': ['0.5–1 mm coated grain'],
    'summary_spec': 'Six colours · 0.5–1 mm · Sample-led shade approval',
    'seo_title': 'Colour-Coated Silica Sand Supplier | Jade Waves Enterprise',
    'meta_description': 'Source colour-coated silica sand from India in six colours and 0.5–1 mm grain size for flooring, coatings and decorative finishes. Request a shade sample.',
}


def catalogue():
    return json.loads((ROOT / 'assets/colour-coated-sand/catalogue.json').read_text())


def add_styles(g, html):
    return html.replace('</head>', f'<link rel="stylesheet" href="assets/colour-coated-sand/coated-sand.css?v={g["BUILD_VERSION"]}" /></head>')


def render(g):
    entries = catalogue()
    section = (ROOT / 'templates/colour-coated-sand.html').read_text()
    tokens = {
        '{{WIDTH}}': str(entries[0]['width']), '{{HEIGHT}}': str(entries[0]['height']),
        '{{OPTIONS}}': ''.join(f'<option value="{e["id"]}">{escape(e["name"])}</option>' for e in entries),
        '{{DATA}}': json.dumps(entries, ensure_ascii=False).replace('<', '\\u003c'),
        '{{APPLICATIONS}}': decorative_products.coated_applications(),
        '{{BUYER_QUESTIONS}}': decorative_products.buyer_questions('colour-coated-silica-sand'),
        '<p class="ml-eyebrow">Silica sand / Decorative range</p>': '<a class="ml-eyebrow coated-range-breadcrumb" href="/products/#decorative-range">Materials / Decorative Range ↗</a>',
        '<h2 id="coated-sand-heading">Colour-coated silica sand.</h2>': '<h1 id="coated-sand-heading">Colour-coated silica sand.</h1>',
        'Standard silica sand COA/TDS references': 'Industrial silica sand COA/TDS references',
    }
    for before, after in tokens.items():
        section = section.replace(before, after)
    assert not re.search(r'\{\{\w+\}\}', section)
    related = ('<nav class="ml-container coated-sand-related" aria-label="Related materials">'
               '<a href="/products/pebbles/">Explore pebbles ↗</a>'
               '<a href="/products/glass-chips/">Explore decorative glass chips ↗</a>'
               '<a href="/products/marble-chips/">Explore marble chips ↗</a>'
               '<a href="/products/grout-sand/">Explore coloured grout sand ↗</a>'
               '<a href="/products/silica-sand/">Looking for industrial silica sand? ↗</a></nav>')
    enquiry = decorative_inquiry.render(g, PRODUCT['name'], 'Colour: Red\nGrain size: 0.5–1 mm', 'data-sand-email')
    body = decorative_inquiry.navigation(g) + '<main id="main-content" tabindex="-1">' + section + related + enquiry + '</main>' + g['footer_html']()
    base = g['BASE_URL']
    schema = [
        {'@context': 'https://schema.org', '@type': 'Product', 'name': PRODUCT['name'],
         'description': PRODUCT['meta_description'], 'category': 'Decorative Range',
         'brand': {'@type': 'Brand', 'name': g['CONTACT']['company']},
         'url': base + PATH, 'image': [base + '/' + entry['src'] for entry in entries],
         'size': '0.5–1 mm', 'color': [entry['name'] for entry in entries]},
        {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Materials', 'item': base + '/products/'},
            {'@type': 'ListItem', 'position': 2, 'name': 'Decorative Range', 'item': base + '/products/#decorative-range'},
            {'@type': 'ListItem', 'position': 3, 'name': PRODUCT['name'], 'item': base + PATH},
        ]},
    ]
    html = g['page_shell'](PRODUCT['seo_title'], PRODUCT['meta_description'], PATH, body, schema, 'page-product page-ledger page-coated-sand')
    html = add_styles(g, html)
    html = decorative_products.add_styles(g, html)
    html = html.replace('</head>', f'<script defer src="assets/colour-coated-sand/coated-sand.js?v={g["BUILD_VERSION"]}"></script></head>')
    return decorative_inquiry.add_assets(g, html)
