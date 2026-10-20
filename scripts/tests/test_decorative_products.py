"""Published contracts for Glass Chips, Grout Sand and full coated applications."""
from html import escape
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


class Markup(HTMLParser):
    def __init__(self, html):
        super().__init__(); self.tags = []; self.feed(html)
    def handle_starttag(self, tag, attrs): self.tags.append((tag, dict(attrs)))


class DecorativeProductTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pages = {p['slug']: decorative.render(vars(site), p['slug']) for p in decorative.PRODUCTS}
        cls.data = {slug: json.loads(re.search(r'<script type="application/json" id="decorative-product-data">(.*?)</script>', html, re.S).group(1)) for slug, html in cls.pages.items()}

    def test_core_eleven_preserved_with_four_decorative_catalogue_products(self):
        self.assertEqual(len(site.PRODUCTS), 11)
        self.assertEqual(len(site.CATALOGUE_PRODUCTS), 15)
        self.assertEqual(len({p['slug'] for p in site.CATALOGUE_PRODUCTS}), 15)
        family = next(f for f in site.PRODUCT_FAMILIES if f['id'] == 'decorative-range')
        self.assertEqual(family['products'], ['pebbles', 'colour-coated-silica-sand', 'glass-chips', 'grout-sand'])

    def test_home_and_materials_link_to_both_new_pages_without_bogus_tds(self):
        home, materials = site.render_homepage(), site.render_products_index()
        self.assertIn('15 products', materials)
        for slug in self.pages:
            self.assertIn('href="products/' + slug + '/"', home)
            self.assertIn('href="products/' + slug + '/#collection"', materials)
            self.assertNotIn('products/' + slug + '/#contact', materials)

    def test_indexable_metadata_structured_data_and_recorded_dates(self):
        for slug, html in self.pages.items():
            with self.subTest(slug=slug):
                path = '/products/' + slug + '/'
                self.assertIn('rel="canonical" href="' + site.BASE_URL + path + '"', html)
                self.assertIn('content="index,follow"', html); self.assertNotIn('noindex', html)
                self.assertIn(site.GA4_MEASUREMENT_ID, html)
                schemas = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', html, re.S).group(1))
                self.assertEqual({s['@type'] for s in schemas}, {'Product', 'BreadcrumbList'})
                product = next(s for s in schemas if s['@type'] == 'Product')
                self.assertEqual(product['url'], site.BASE_URL + path)
                self.assertIn('content="' + product['image'][0] + '"', html)
                for field in ('offers', 'review', 'aggregateRating', 'manufacturer'): self.assertNotIn(field, product)
                self.assertEqual(site.page_lastmod(path), '2026-10-20')

    def test_one_heading_one_carousel_and_collapsed_notes(self):
        for html in self.pages.values():
            tags = Markup(html).tags
            self.assertEqual(len([a for t, a in tags if t == 'h1']), 1)
            self.assertEqual(len([a for t, a in tags if 'data-product-carousel' in a]), 1)
            self.assertEqual(len([a for t, a in tags if 'data-product-photo' in a]), 1)
            self.assertEqual(len([a for t, a in tags if t == 'details']), 1)
            self.assertNotIn('open', next(a for t, a in tags if t == 'details'))
            ids = [a['id'] for _, a in tags if 'id' in a]
            self.assertEqual(len(ids), len(set(ids)))

    def test_glass_finishes_and_printed_grades_remain_sample_confirmed(self):
        glass = self.data['glass-chips']
        self.assertEqual([e['name'] for e in glass['entries']], ['Clear', 'Green', 'Brown', 'Cobalt blue', 'Mixed mirror', 'Sky blue'])
        self.assertEqual(glass['sizes'], ['1–3 mm', '3–6 mm', '6–9 mm'])
        self.assertIn('approved sample before ordering', self.pages['glass-chips'])

    def test_grout_has_two_sample_views_three_grades_and_all_25_colours(self):
        grout = self.data['grout-sand']
        self.assertEqual([e['name'] for e in grout['entries']], ['Colour range', 'Neutral shades'])
        self.assertEqual(grout['sizes'], ['0.5–1 mm', '100 mesh', '150 mesh'])
        expected = ['White', 'Ivory', 'Red oxide', 'Terracotta', 'Coffee brown', 'Copper brown', 'Burgundy', 'Red', 'Light pink', 'D Black', 'Light grey', 'Dark grey', 'Steel grey', 'Yellow', 'Dark brown', 'Blue', 'Alpen blue', 'Sky blue', 'Brown', 'Beige', 'Golden yellow', 'Green', 'Light green', 'Kesar', 'Mashroom']
        self.assertEqual([c['name'] for c in grout['colours']], expected)
        radios = [a for t, a in Markup(self.pages['grout-sand']).tags if 'data-product-colour' in a]
        self.assertEqual([r['value'] for r in radios], [c['id'] for c in grout['colours']])
        self.assertTrue(all(r['type'] == 'radio' for r in radios))
        self.assertEqual(len([r for r in radios if 'checked' in r]), 1)
        self.assertIn('not ready-to-use grout', self.pages['grout-sand'])
        self.assertIn('Chart references only, not individual product photos', self.pages['grout-sand'])
        self.assertIn('25 kg bags; 40 bags per 1,000 kg jumbo bag', self.pages['grout-sand'])

    def test_all_photos_and_chart_swatches_are_clean_local_assets_with_dimensions(self):
        for data in self.data.values():
            for e in data['entries'] + data['colours']:
                self.assertTrue((ROOT / e['src']).is_file(), e['src'])
                self.assertTrue(e['src'].startswith('assets/'))
                self.assertGreater(e['width'], 0); self.assertGreater(e['height'], 0)

    def test_coated_page_keeps_six_photos_and_includes_all_sixteen_applications(self):
        html = site.render_product_page(site.CATALOGUE_BY_SLUG['colour-coated-silica-sand'])
        section = re.search(r'<section class="coated-full-applications".*?</section>', html, re.S).group(0)
        groups = json.loads((ROOT / 'templates/coated-applications.json').read_text())
        items = [item for group in groups for item in group['items']]
        self.assertEqual(len(items), 16); self.assertEqual(section.count('<li>'), 16)
        for item in items: self.assertIn('<li>' + escape(item) + '</li>', section)
        self.assertIn('not a safety certification', section)
        self.assertIn('specific suitability and safety verification', section)
        self.assertIn('href="products/colour-coated-silica-sand/#applications"', html)
        self.assertEqual(len(json.loads(re.search(r'<script type="application/json" id="coated-sand-data">(.*?)</script>', html, re.S).group(1))), 6)

    def test_project_aware_base_and_approved_stylesheet_order_are_retained(self):
        for html in list(self.pages.values()) + [site.render_product_page(site.CATALOGUE_BY_SLUG['colour-coated-silica-sand'])]:
            self.assertIn("document.write('<base href=\"' + baseHref + '\">');", html)
            self.assertNotIn("document.write('<base href=\"https://", html)
            self.assertLess(html.index('assets/colour-coated-sand/coated-sand.css'), html.index('assets/decorative-products/decorative-products.css'))
            self.assertNotIn('preview.css', html); self.assertNotIn('previews/', html)

    def test_no_supplier_prices_or_unsupported_performance_promises(self):
        for html in self.pages.values():
            for term in ('miracle', 'mmart', '9825369637', '7069837933', 'waterproof', 'uv stable', 'solvent proof', 'non-toxic', 'recycled'):
                self.assertNotIn(term, html.lower())
            self.assertNotRegex(html, r'(?i)\b(price|MOQ|GST|certified)\b|₹|Rs/KG')

    def test_email_drafts_are_contextual_not_false_lead_submissions(self):
        for html in self.pages.values():
            self.assertIn('data-product-email', html)
            self.assertIn('mailto:' + site.CONTACT['sales_email'] + '?', html)
            self.assertNotIn('data-inquiry-form', html)
        source = (ROOT / 'assets/decorative-products/carousel.js').read_text()
        self.assertNotRegex(source, r'\bfetch\(|XMLHttpRequest|sendBeacon|gtag\(|setInterval|setTimeout')

    def test_builds_need_no_preview_supplier_pdf_or_image_processing_runtime(self):
        for name in ('templates/decorative_products.py', 'templates/decorative-product.html', 'templates/decorative-products.json', 'templates/coated-applications.json'):
            source = (ROOT / name).read_text()
            for term in ('previews/', 'Downloads/', 'PdfReader', 'from PIL'): self.assertNotIn(term, source)
        industrial = site.render_product_page(site.PRODUCTS_BY_SLUG['silica-sand'])
        for term in ('glass-chips/', 'grout-sand/', 'data-product-carousel', 'assets/decorative-products/'):
            self.assertNotIn(term, industrial)
        self.assertIn('data-inquiry-form', industrial)


if __name__ == '__main__': unittest.main()
