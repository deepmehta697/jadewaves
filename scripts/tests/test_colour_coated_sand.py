"""Production contracts for the approved Decorative Range architecture."""
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
import unittest
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
import generate_site as site
from templates import colour_coated_sand as coated


class Markup(HTMLParser):
    def __init__(self, html):
        super().__init__(); self.tags = []; self.feed(html)
    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))


class ColourCoatedSandTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = coated.render(vars(site))
        cls.tags = Markup(cls.html).tags

    def test_decorative_family_preserves_core_catalogue_and_approved_additions(self):
        self.assertEqual(len(site.PRODUCTS), 11)
        self.assertEqual(len(site.CATALOGUE_PRODUCTS), 15)
        family = next(f for f in site.PRODUCT_FAMILIES if f['id'] == 'decorative-range')
        self.assertEqual(family['name'], 'Decorative Range')
        self.assertEqual(family['products'], ['pebbles', 'colour-coated-silica-sand', 'glass-chips', 'grout-sand'])
        self.assertIn('15 products', site.render_products_index())
        self.assertIn('id="decorative-stone"', site.render_products_index())

    def test_home_and_materials_both_link_to_the_new_page(self):
        for html in (site.render_homepage(), site.render_products_index()):
            self.assertIn('href="products/colour-coated-silica-sand/"', html)
            self.assertIn('href="products/pebbles/"', html)
        self.assertNotIn('products/colour-coated-silica-sand/#contact', site.render_products_index())

    def test_industrial_silica_has_one_quiet_link_and_no_colour_carousel(self):
        html = site.render_product_page(site.PRODUCTS_BY_SLUG['silica-sand'])
        for unwanted in ('data-sand-carousel', 'coated-sand-data', 'coated-sand.js', 'colour-coated-sand/red.webp'):
            self.assertNotIn(unwanted, html)
        links = [a['href'] for t, a in Markup(html).tags if t == 'a' and 'colour-coated-silica-sand' in a.get('href', '')]
        self.assertEqual(links, ['products/colour-coated-silica-sand/'])
        self.assertIn('data-inquiry-form', html)
        self.assertIn('name="product" value="Silica Sand"', html)

    def test_new_page_has_one_h1_and_one_six_colour_carousel(self):
        self.assertEqual(len([a for t, a in self.tags if t == 'h1']), 1)
        self.assertEqual(len([a for t, a in self.tags if 'data-sand-photo' in a]), 1)
        self.assertEqual(len(coated.catalogue()), 6)
        self.assertIn('href="products/#decorative-range"', self.html)
        ids = [a['id'] for _, a in self.tags if 'id' in a]
        self.assertEqual(len(ids), len(set(ids)))
        notes = next(a for t, a in self.tags if t == 'details' and a.get('class') == 'coated-sand-notes')
        self.assertNotIn('open', notes)

    def test_metadata_and_dates_are_published_not_preview_only(self):
        self.assertIn('content="index,follow"', self.html)
        self.assertNotIn('noindex', self.html)
        self.assertIn('rel="canonical" href="' + site.BASE_URL + coated.PATH + '"', self.html)
        self.assertIn(site.GA4_MEASUREMENT_ID, self.html)
        self.assertEqual(site.page_lastmod(coated.PATH), '2026-10-20')
        self.assertEqual(site.page_lastmod('/products/silica-sand/'), '2026-10-20')
        self.assertEqual(site.page_lastmod('/products/feldspar/'), '2026-10-13')

    def test_image_and_script_paths_follow_the_real_site_base(self):
        self.assertIn("document.write('<base href=\"' + baseHref + '\">');", self.html)
        self.assertNotIn("document.write('<base href=\"https://", self.html)
        for e in coated.catalogue():
            self.assertTrue((ROOT / e['src']).is_file())
            self.assertEqual(e['src'], 'assets/colour-coated-sand/' + e['id'] + '.webp')
            self.assertEqual(e['size'], '0.5–1 mm')
            self.assertGreater(e['width'], 0)
            self.assertGreater(e['height'], 0)
        self.assertIn('src="assets/colour-coated-sand/coated-sand.js?', self.html)
        self.assertIn('href="assets/colour-coated-sand/coated-sand.css?', self.html)

    def test_only_contextual_email_draft_not_false_lead_submission(self):
        links = [a['href'] for t, a in self.tags if t == 'a' and 'data-sand-email' in a]
        self.assertEqual(len(links), 1)
        self.assertEqual(urlsplit(links[0]).path, site.CONTACT['sales_email'])
        self.assertNotIn('data-inquiry-form', self.html)
        self.assertNotIn('data-preview-inquiry-form', self.html)

    def test_no_supplier_rates_or_invented_technical_claims(self):
        for term in ('miracle', 'mmart', 'miraclemarble', '9825369637', 'Rs./kg', 'waterproof certified'):
            self.assertNotIn(term.lower(), self.html.lower())
        self.assertNotRegex(self.html, r'(?i)\b(price|MOQ|GST|jurisdiction)\b')
        self.assertIn('do not certify this coated range', self.html)
        schemas = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', self.html, re.S).group(1))
        product = next(s for s in schemas if s['@type'] == 'Product')
        for key in ('offers', 'review', 'aggregateRating', 'manufacturer'):
            self.assertNotIn(key, product)

    def test_production_render_does_not_depend_on_preview_or_supplier_pdf(self):
        for source in (ROOT / 'templates/colour_coated_sand.py', ROOT / 'templates/colour-coated-sand.html'):
            for term in ('previews/', 'Downloads/', 'PdfReader', 'from PIL'):
                self.assertNotIn(term, source.read_text())


if __name__ == '__main__':
    unittest.main()
