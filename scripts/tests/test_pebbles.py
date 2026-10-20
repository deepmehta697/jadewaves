"""Production integration contracts for the approved decorative-stone addition."""
import json
from pathlib import Path
import re
import sys
import unittest
from html.parser import HTMLParser
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
import generate_site as site
from templates import pebbles


class Markup(HTMLParser):
    def __init__(self, html):
        super().__init__(); self.tags = []; self.feed(html)
    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))


class PebbleIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.html = pebbles.render(vars(site))
        self.tags = Markup(self.html).tags

    def test_core_products_remain_with_the_decorative_catalogue_pages(self):
        self.assertEqual(len(site.PRODUCTS), 11)
        self.assertEqual(len(site.CATALOGUE_PRODUCTS), 16)
        self.assertEqual(len({p['slug'] for p in site.CATALOGUE_PRODUCTS}), 16)
        self.assertIn('pebbles', site.CATALOGUE_BY_SLUG)
        for p in site.PRODUCTS:
            self.assertIn(p['slug'], site.CATALOGUE_BY_SLUG)

    def test_published_metadata_and_sitemap_are_not_preview_only(self):
        self.assertIn('https://jadewavesenterprise.com/products/pebbles/', self.html)
        self.assertIn('content="index,follow"', self.html)
        self.assertNotIn('noindex', self.html)
        self.assertIn('/products/pebbles/', site.render_sitemap())
        self.assertEqual(site.page_lastmod('/products/pebbles/'), '2026-10-20')
        self.assertEqual(site.page_lastmod('/products/feldspar/'), '2026-10-13')

    def test_discovery_from_home_and_material_portfolio(self):
        for html in (site.render_homepage(), site.render_products_index()):
            self.assertIn('href="products/pebbles/"', html)
            self.assertIn('Pebbles', html)
        self.assertIn('16 products', site.render_products_index())

    def test_one_photo_with_clean_data_and_all_local_assets(self):
        entries = pebbles.catalogue()
        self.assertEqual(len(entries), 31)
        self.assertEqual(len([a for t, a in self.tags if t == 'img' and 'data-photo' in a]), 1)
        self.assertEqual(len([a for t, a in self.tags if 'data-carousel' in a]), 1)
        for e in entries:
            self.assertTrue((ROOT / e['src']).is_file(), e['src'])
            self.assertTrue(e['width'] > 0 and e['height'] > 0)
            self.assertTrue(e['sizes'])
            self.assertTrue(all(s.endswith(' mm') for s in e['sizes']))
        for word in ('miracle', 'mmart', 'miraclemarble', '7069837933', '9825369637', 'Rs./kg'):
            self.assertNotIn(word.lower(), self.html.lower())
        self.assertNotRegex(self.html, r'(?i)\b(price|MOQ|GST|jurisdiction)\b')
        self.assertNotIn('.pdf', self.html)

    def test_shared_navigation_and_existing_email_enquiry(self):
        self.assertIn('data-menu-toggle', self.html)
        self.assertIn('data-mobile-menu', self.html)
        self.assertTrue(any(a.get('id') == 'contact' for _, a in self.tags))
        links = [a['href'] for t, a in self.tags if t == 'a' and 'data-email' in a]
        self.assertEqual(len(links), 1)
        self.assertTrue(links[0].startswith('mailto:' + site.CONTACT['sales_email'] + '?'))
        self.assertIn('data-inquiry-form', self.html)
        self.assertIn('data-decorative-form', self.html)

    def test_carousel_paths_follow_the_site_base(self):
        raw = re.search(r'<script type="application/json" id="pebble-data">(.*?)</script>', self.html, re.S).group(1)
        for e in json.loads(raw):
            self.assertEqual(e['src'], f'assets/pebbles/{e["id"]}.webp')
        self.assertIn('src="assets/pebbles/pebbles.js?', self.html)
        self.assertIn('href="assets/pebbles/pebbles.css?', self.html)
        self.assertNotIn('href="#', self.html)

    def test_schema_does_not_invent_manufacturer_offers_or_reviews(self):
        schemas = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', self.html, re.S).group(1))
        product = next(s for s in schemas if s['@type'] == 'Product')
        for key in ('manufacturer', 'offers', 'review', 'aggregateRating'):
            self.assertNotIn(key, product)

    def test_build_does_not_include_preview_or_pdf_extraction_sources(self):
        from scripts.build_site import publishable_root_dirs
        self.assertNotIn('previews', {p.name for p in publishable_root_dirs()})
        source = (ROOT / 'templates/pebbles.py').read_text()
        self.assertNotIn('PdfReader', source)
        self.assertNotIn('Downloads', source)
        self.assertEqual((ROOT / 'assets/pebbles/pebbles.js').read_text(), (ROOT / 'previews/pebbles/pebbles.js').read_text())


if __name__ == '__main__':
    unittest.main()
