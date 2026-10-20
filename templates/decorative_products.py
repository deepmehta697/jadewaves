"""Decorative chip and filler pages, built only from clean local assets."""
from html import escape
import json
from pathlib import Path
import re
from templates import decorative_inquiry

ROOT = Path(__file__).resolve().parents[1]
CONFIG = json.loads((ROOT / 'templates/decorative-products.json').read_text())
PRODUCTS = [{**p, 'family': 'Decorative Range', 'industries': ['Decorative finishes'],
             'applications': [text for _, text in p['applications']],
             'summary_spec': ' / '.join(p['sizes']), 'specs': p['sizes']} for p in CONFIG]


def catalogue(slug):
    return json.loads((ROOT / 'assets' / slug / 'catalogue.json').read_text())


def colours(slug):
    path = ROOT / 'assets' / slug / 'colours.json'
    return json.loads(path.read_text()) if path.exists() else []


def add_styles(g, html):
    return html.replace('</head>', f'<link rel="stylesheet" href="assets/decorative-products/decorative-products.css?v={g["BUILD_VERSION"]}" /></head>')


def buyer_questions(slug):
    questions = json.loads((ROOT / 'templates/decorative-buyer-questions.json').read_text()).get(slug, [])
    if not questions:
        return ''
    rows = ''.join('<div><dt>' + escape(q['question']) + '</dt><dd>' + escape(q['answer']) + '</dd></div>' for q in questions)
    return '<div class="buyer-question-list"><h3>Before you order</h3><dl>' + rows + '</dl></div>'


def coated_applications():
    groups = json.loads((ROOT / 'templates/coated-applications.json').read_text())
    assert sum(len(group['items']) for group in groups) == 16
    items = ''.join('<div><h3>' + escape(group['name']) + '</h3><ul>'
                    + ''.join('<li>' + escape(item) + '</li>' for item in group['items'])
                    + '</ul></div>' for group in groups)
    return ('<section class="coated-full-applications" id="applications" aria-labelledby="applications-heading">'
            '<h2 id="applications-heading">Applications.</h2>'
            '<div class="coated-application-grid">' + items + '</div>'
            '<p class="decorative-colour-note">Select and validate the grade for the intended use. '
            'Aquarium decoration and children’s play gardens require specific suitability and safety verification; '
            'catalogue inclusion is not a safety certification.</p></section>')


def render(g, slug):
    product = next(p for p in CONFIG if p['slug'] == slug)
    photos, shades = catalogue(slug), colours(slug)
    first = photos[0]
    config = {key: product[key] for key in ('name', 'choice_label', 'size_label', 'sizes', 'enquiry_note')}
    config.update(entries=photos, colours=shades)
    related = ''.join(f'<a href="/products/{p["slug"]}/">Explore {escape(p["name"].lower())} ↗</a>'
                      for p in CONFIG if p['slug'] != slug)
    tokens = {
        'HEADING': escape(product['heading']), 'LEAD': escape(product['lead']), 'NAME': escape(product['name']),
        'COUNT': str(len(photos)), 'PADDED_COUNT': str(len(photos)).zfill(2),
        'FIRST_NAME': escape(first['name']), 'FIRST_SRC': escape(first['src']), 'FIRST_ALT': escape(first['alt']),
        'WIDTH': str(first['width']), 'HEIGHT': str(first['height']),
        'CHOICE_LABEL': escape(product['choice_label']), 'CHOICE_LOWER': escape(product['choice_label'].lower()),
        'SIZE_LABEL': escape(product['size_label']),
        'OPTIONS': ''.join(f'<option value="{e["id"]}">{escape(e["name"])}</option>' for e in photos),
        'SIZES': ''.join(f'<option value="{escape(s)}">{escape(s)}</option>' for s in product['sizes']),
        'APPLICATIONS': ''.join(f'<div><dt>{escape(label)}</dt><dd>{escape(copy)}</dd></div>' for label, copy in product['applications']),
        'CAPTION': escape(product['caption']), 'NOTES_TITLE': escape(product['notes_title']),
        'NOTES': ''.join(f'<p>{escape(note)}</p>' for note in product['notes']),
        'BUYER_QUESTIONS': buyer_questions(slug),
        'CHOICE_TEXT': escape(', '.join(e['name'] for e in photos)), 'SIZE_TEXT': escape(' / '.join(product['sizes'])),
        'DATA': json.dumps(config, ensure_ascii=False).replace('<', '\\u003c'),
        'RELATED': related + '<a href="/products/colour-coated-silica-sand/">Explore colour-coated silica sand ↗</a><a href="/products/pebbles/">Explore decorative pebbles ↗</a>',
        'SELECTED_COLOUR': '<p class="decorative-requested-colour">Requested colour: <strong data-product-selected-colour>' + escape(shades[0]['name']) + '</strong></p>' if shades else '',
        'COLOUR_PALETTE': '',
    }
    if shades:
        swatches = ''.join(
            '<label class="decorative-swatch"><input type="radio" name="requested-colour" '
            f'value="{e["id"]}" data-product-colour disabled' + (' checked' if i == 0 else '') + '>'
            f'<img src="{e["src"]}" alt="" width="{e["width"]}" height="{e["height"]}" loading="lazy">'
            f'<span>{escape(e["name"])}</span></label>' for i, e in enumerate(shades))
        tokens['COLOUR_PALETTE'] = (
            '<section class="decorative-colours" id="available-colours" aria-labelledby="colours-heading">'
            '<h2 id="colours-heading">Available colours.</h2>'
            '<p>25 catalogue shades. Custom colours available on request.</p>'
            '<fieldset class="decorative-colour-field"><legend>Choose a colour for your enquiry</legend>'
            '<div class="decorative-colour-grid">' + swatches + '</div></fieldset>'
            '<p class="decorative-colour-note">Chart references only, not individual product photos. '
            'Confirm the actual shade with a sample; the carousel shows assorted sample shades.</p>'
            f'<a class="ml-text-link" href="#contact" data-decorative-enquire>Request this colour ↗</a></section>')
    section = (ROOT / 'templates/decorative-product.html').read_text()
    for key, value in tokens.items():
        section = section.replace('{{' + key + '}}', value)
    assert not re.search(r'\{\{\w+\}\}', section)
    selection = product['choice_label'] + ': ' + first['name'] + '\n' + product['size_label'] + ': ' + product['sizes'][0]
    if shades:
        selection += '\nRequested colour: ' + shades[0]['name']
    email_attributes = 'data-product-email' + (' data-product-colour-email' if shades else '')
    enquiry = decorative_inquiry.render(g, product['name'], selection, email_attributes)
    body = decorative_inquiry.navigation(g) + '<main id="main-content" tabindex="-1">' + section + enquiry + '</main>' + g['footer_html']()
    base, path = g['BASE_URL'], '/products/' + slug + '/'
    schema = [
        {'@context': 'https://schema.org', '@type': 'Product', 'name': product['name'],
         'description': product['meta_description'], 'category': 'Decorative Range',
         'brand': {'@type': 'Brand', 'name': g['CONTACT']['company']},
         'url': base + path, 'image': [base + '/' + photo['src'] for photo in photos],
         'size': product['sizes']},
        {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Materials', 'item': base + '/products/'},
            {'@type': 'ListItem', 'position': 2, 'name': 'Decorative Range', 'item': base + '/products/#decorative-range'},
            {'@type': 'ListItem', 'position': 3, 'name': product['name'], 'item': base + path},
        ]},
    ]
    html = g['page_shell'](product['seo_title'], product['meta_description'],
                           path, body, schema, 'page-product page-ledger page-coated-sand page-' + slug)
    html = html.replace('<meta property="og:image" content="' + base + '/assets/jade-waves-logo-transparent.png"',
                        '<meta property="og:image" content="' + base + '/' + first['src'] + '"')
    html = html.replace('</head>', f'<link rel="stylesheet" href="assets/colour-coated-sand/coated-sand.css?v={g["BUILD_VERSION"]}" /></head>')
    html = add_styles(g, html)
    html = html.replace('</head>', f'<script defer src="assets/decorative-products/carousel.js?v={g["BUILD_VERSION"]}"></script></head>')
    return decorative_inquiry.add_assets(g, html)
