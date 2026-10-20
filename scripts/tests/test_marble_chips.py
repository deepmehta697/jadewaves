"""Marble catalogue evidence and clean-page contracts; no PDF runtime needed."""
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
import generate_site as site
from templates import decorative_products as decorative


class Tags(HTMLParser):
    def __init__(self, html):
        super().__init__(); self.tags = []; self.feed(html)
    def handle_starttag(self, tag, attrs): self.tags.append((tag, dict(attrs)))


class MarbleChipsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.product = site.CATALOGUE_BY_SLUG['marble-chips']
        cls.html = site.render_product_page(cls.product)
        cls.tags = Tags(cls.html).tags
        cls.catalogue = decorative.catalogue('marble-chips')

    def test_twelve_actual_marble_options_not_quartz_or_unidentified_gravels(self):
        expected = ['White', 'Red', 'Rojo pink', 'Pink wood', 'Green', 'Grey', 'Mocha',
                    'Brown', 'Black', 'Panther', 'Ivory cream', 'Mixed marble']
        self.assertEqual([e['name'] for e in self.catalogue], expected)
        data = json.loads(re.search(r'<script type="application/json" id="decorative-product-data">(.*?)</script>', self.html, re.S).group(1))
        self.assertEqual(data['entries'], self.catalogue)
        self.assertEqual(data['sizes'], ['0.5–1.5 mm', '1–3 mm', '3–6 mm', '6–9 mm', '9–12 mm'])
        self.assertEqual(data['choice_label'], 'Colour / blend')
        self.assertNotIn('Quartz chips', self.html)
        self.assertNotIn('Mix gravels', self.html)

    def test_one_photo_one_heading_and_one_collapsed_notes_panel(self):
        self.assertEqual(len([a for t, a in self.tags if 'data-product-photo' in a]), 1)
        self.assertEqual(len([a for t, a in self.tags if t == 'h1']), 1)
        notes = [a for t, a in self.tags if t == 'details']
        self.assertEqual(len(notes), 1); self.assertNotIn('open', notes[0])
        self.assertNotIn('buyer-question-list', self.html)
        self.assertNotIn('decorative-colour-grid', self.html)
        photo = next(a for t, a in self.tags if 'data-product-photo' in a)
        self.assertEqual(photo['fetchpriority'], 'high')
        self.assertEqual(photo['src'], 'assets/marble-chips/white.webp')

    def test_supplier_context_and_unverified_packing_do_not_leak(self):
        for term in ('miracle', 'mmart', '9825369637', 'miraclemarbleart', 'nagor', 'stockiest', '25 kg'):
            self.assertNotIn(term, self.html.lower())
        self.assertNotRegex(self.html, r'(?i)\b(price|MOQ|GST|manufacturer|certified)\b|Rs/kg|₹')
        self.assertNotIn('MARBLE CHIPS CATALOG.pdf', self.html)
        self.assertIn('Confirm grading and binder suitability', self.html)

    def test_only_clean_lossless_photos_and_public_metadata_are_dependencies(self):
        self.assertEqual(len(list((ROOT / 'assets/marble-chips').glob('*.webp'))), 12)
        for entry in self.catalogue:
            self.assertEqual(set(entry), {'id', 'name', 'src', 'width', 'height', 'alt'})
            raw = (ROOT / entry['src']).read_bytes()
            self.assertEqual(raw[:4], b'RIFF'); self.assertEqual(raw[8:12], b'WEBP')
            self.assertIn(b'VP8L', raw[:50])
            self.assertNotIn(b'EXIF', raw[:50]); self.assertNotIn(b'XMP ', raw[:50])
            self.assertGreater(entry['width'], 0); self.assertGreater(entry['height'], 0)
            self.assertTrue(entry['alt'].endswith('marble chips'))
        source = (ROOT / 'templates/decorative_products.py').read_text()
        for term in ('Downloads/', 'PdfReader', 'from PIL', 'tmp/pdfs'):
            self.assertNotIn(term, source)

    def test_discovery_metadata_and_schema_match_the_real_selection(self):
        for html in (site.render_homepage(), site.render_products_index()):
            self.assertIn('href="products/marble-chips/"', html)
            image = next(a for t, a in Tags(html).tags if t == 'img' and a.get('src') == 'assets/marble-chips/white.webp')
            self.assertEqual((image['width'], image['height']), ('717', '714'))
        self.assertIn('products/marble-chips/#collection', site.render_products_index())
        self.assertEqual(site.page_lastmod('/products/marble-chips/'), '2026-10-20')
        self.assertIn('content="index,follow"', self.html)
        self.assertIn('rel="canonical" href="https://jadewavesenterprise.com/products/marble-chips/"', self.html)
        schemas = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', self.html, re.S).group(1))
        product = next(s for s in schemas if s['@type'] == 'Product')
        self.assertEqual(product['size'], self.product['sizes'])
        self.assertEqual(len(product['image']), 12)
        for field in ('offers', 'manufacturer', 'aggregateRating', 'review'): self.assertNotIn(field, product)
        self.assertEqual(len(site.PRODUCTS), 11)
        self.assertEqual(len(site.CATALOGUE_PRODUCTS), 16)


if __name__ == '__main__': unittest.main()
