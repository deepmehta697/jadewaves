"""Published pebble page, using approved cropped assets without PDF dependencies."""
import json
import re
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = '/products/pebbles/'
PRODUCT = {
    'slug': 'pebbles', 'name': 'Pebbles', 'family': 'Decorative Stone',
    'forms': ['Natural', 'Polished', 'Tumbled', 'Coated'],
    'industries': ['Decorative stone'],
    'applications': ['Colour and finish selection', 'Project-specific sizing'],
    'specs': ['31 colour and finish selections'],
    'summary_spec': 'Sizes vary by selection; compare the collection.',
    'seo_title': 'Pebbles: Colours, Finishes & Sizes | Jade Waves Enterprise',
    'meta_description': 'Explore 31 pebble selections, from natural and tumbled stone to polished colours. Compare sizes and packing references, then discuss a sample with Jade Waves.',
}


def catalogue():
    return json.loads((ROOT / 'assets/pebbles/catalogue.json').read_text())


def render(g):
    entries = catalogue()
    source = (ROOT / 'templates/pebbles-page.html').read_text()
    content = source.split('<main id="main-content" tabindex="-1">', 1)[1].split('</main>', 1)[0]
    options = []
    for finish in dict.fromkeys(e['finish'] for e in entries):
        options.append(f'<optgroup label="{escape(finish)}">')
        options.extend(f'<option value="{e["id"]}">{escape(e["name"])}</option>' for e in entries if e['finish'] == finish)
        options.append('</optgroup>')
    rows = ''.join(
        f'<tr><th scope="row">{escape(e["name"])}</th><td>{escape(e["finish"])}</td>'
        f'<td>{escape(" / ".join(e["sizes"]))}</td></tr>' for e in entries
    )
    replacements = {
        '{{COUNT}}': str(len(entries)), '{{OPTIONS}}': ''.join(options), '{{ROWS}}': rows,
        '{{FIRST_WIDTH}}': str(entries[0]['width']), '{{FIRST_HEIGHT}}': str(entries[0]['height']),
        'src="media/white-polished.webp"': 'src="/assets/pebbles/white-polished.webp"',
        'id="enquire"': 'id="contact"', 'href="#enquire"': 'href="#contact"',
    }
    for before, after in replacements.items():
        content = content.replace(before, after)
    assert not re.search(r'\{\{\w+\}\}', content)
    data = json.dumps(entries, ensure_ascii=False).replace('<', '\\u003c')
    body = (g['nav_html']() + '<main id="main-content" tabindex="-1">' + content + '</main>'
            + f'<script type="application/json" id="pebble-data">{data}</script>' + g['footer_html']())
    schema = [
        {'@context': 'https://schema.org', '@type': 'Product', 'name': 'Pebbles',
         'description': PRODUCT['meta_description'], 'category': 'Decorative stone',
         'brand': {'@type': 'Brand', 'name': g['CONTACT']['company']},
         'url': g['BASE_URL'] + PATH, 'image': g['BASE_URL'] + '/assets/pebbles/white-polished.webp'},
        {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': g['BASE_URL'] + '/'},
            {'@type': 'ListItem', 'position': 2, 'name': 'Products', 'item': g['BASE_URL'] + '/products/'},
            {'@type': 'ListItem', 'position': 3, 'name': 'Pebbles', 'item': g['BASE_URL'] + PATH},
        ]},
    ]
    markup = g['page_shell'](PRODUCT['seo_title'], PRODUCT['meta_description'], PATH, body, schema, 'pebble-page page-product page-ledger')
    assets = (f'<link rel="stylesheet" href="assets/pebbles/pebbles.css?v={g["BUILD_VERSION"]}" />'
              f'<script defer src="assets/pebbles/pebbles.js?v={g["BUILD_VERSION"]}"></script>')
    markup = markup.replace(g['BASE_URL'] + '/assets/jade-waves-logo-transparent.png',
                            g['BASE_URL'] + '/assets/pebbles/white-polished.webp')
    return markup.replace('</head>', assets + '</head>')
