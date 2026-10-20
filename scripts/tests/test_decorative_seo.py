"""Targeted decorative-product discovery and metadata regression tests."""
from html import unescape
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
import unittest
from urllib.parse import urlsplit
from urllib.robotparser import RobotFileParser
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
import generate_site as site
from templates import decorative_products, colour_coated_sand, pebbles


class Tags(HTMLParser):
    def __init__(self, html):
        super().__init__(); self.tags = []; self.feed(html)
    def handle_starttag(self, t, a): self.tags.append((t, dict(a)))


class DecorativeSEOTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.slugs = ['glass-chips', 'grout-sand', 'colour-coated-silica-sand', 'marble-chips']
        cls.pages = {slug: site.render_product_page(site.CATALOGUE_BY_SLUG[slug]) for slug in cls.slugs}
        cls.schemas = {slug: next(s for s in json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', html, re.S).group(1)) if s['@type'] == 'Product') for slug, html in cls.pages.items()}
        cls.sitemap = ET.fromstring(site.render_sitemap())
        cls.ns = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9', 'i': 'http://www.google.com/schemas/sitemap-image/1.1'}

    def test_each_title_uses_a_specific_supplier_intent_and_preserves_the_brand(self):
        titles = []
        for slug, html in self.pages.items():
            title = unescape(re.search(r'<title>(.*?)</title>', html).group(1))
            titles.append(title)
            self.assertIn('Supplier', title); self.assertIn('Jade Waves Enterprise', title)
            self.assertEqual(title, site.CATALOGUE_BY_SLUG[slug]['seo_title'])
            self.assertLess(len(title), 90)
            self.assertIn('supplied from India', html)
        self.assertEqual(len(titles), len(set(titles)))

    def test_descriptions_are_distinct_and_fact_specific_not_keyword_lists(self):
        descriptions = [site.CATALOGUE_BY_SLUG[s]['meta_description'] for s in self.slugs]
        self.assertEqual(len(descriptions), len(set(descriptions)))
        self.assertIn('six finishes', descriptions[0]); self.assertIn('1–3', descriptions[0])
        self.assertIn('25 shades', descriptions[1]); self.assertIn('150 mesh', descriptions[1])
        self.assertIn('six colours', descriptions[2]); self.assertIn('0.5–1 mm', descriptions[2])
        for text in descriptions:
            self.assertIn('India', text); self.assertIn('sample', text)
            self.assertNotRegex(text, r'(?i)manufacturer|best price|certified|guaranteed')

    def test_structured_data_lists_all_carousel_photos_but_not_flat_chart_swatches(self):
        expected = {
            'glass-chips': decorative_products.catalogue('glass-chips'),
            'grout-sand': decorative_products.catalogue('grout-sand'),
            'colour-coated-silica-sand': colour_coated_sand.catalogue(),
            'marble-chips': decorative_products.catalogue('marble-chips'),
        }
        for slug, entries in expected.items():
            self.assertEqual(self.schemas[slug]['image'], [site.BASE_URL + '/' + e['src'] for e in entries])
            self.assertTrue(all('/swatches/' not in url for url in self.schemas[slug]['image']))
            self.assertIn('content="' + self.schemas[slug]['image'][0] + '"', self.pages[slug])

    def test_schema_size_and_colour_values_match_visible_options(self):
        for product in decorative_products.CONFIG:
            self.assertEqual(self.schemas[product['slug']]['size'], product['sizes'])
            for size in product['sizes']: self.assertIn('>' + size + '</option>', self.pages[product['slug']])
        coated = self.schemas['colour-coated-silica-sand']
        self.assertEqual(coated['size'], '0.5–1 mm')
        self.assertEqual(coated['color'], [e['name'] for e in colour_coated_sand.catalogue()])

    def test_new_products_have_reciprocal_crawlable_links_and_pebble_discovery(self):
        for slug, html in self.pages.items():
            links = {a.get('href') for t, a in Tags(html).tags if t == 'a'}
            for other in set(self.slugs) - {slug}:
                self.assertIn('products/' + other + '/', links)
            self.assertIn('products/pebbles/', links)
            self.assertIn('products/#decorative-range', links)

    def test_sitemap_has_40_pages_and_91_actual_product_photos(self):
        entries = self.sitemap.findall('s:url', self.ns)
        self.assertEqual(len(entries), 40)
        photos = self.sitemap.findall('s:url/i:image/i:loc', self.ns)
        self.assertEqual(len(photos), 91)
        self.assertEqual(len({n.text for n in photos}), 91)
        expected_counts = {'glass-chips': 6, 'grout-sand': 2, 'colour-coated-silica-sand': 6, 'pebbles': 31, 'marble-chips': 12}
        expected_counts.update({p['slug']: 1 for p in site.PRODUCTS})
        expected_counts['rubber-granules'] = 24
        for entry in entries:
            path = urlsplit(entry.findtext('s:loc', namespaces=self.ns)).path
            images = [n.text for n in entry.findall('i:image/i:loc', self.ns)]
            self.assertEqual(images, site.product_sitemap_images(path))
            slug = path.strip('/').split('/')[-1] if path.strip('/') else ''
            self.assertEqual(len(images), expected_counts.get(slug, 0))
        xml = site.render_sitemap()
        for obsolete in ('image:title', 'image:caption', 'image:license', 'image:geo_location'):
            self.assertNotIn('<' + obsolete, xml)

    def test_all_sitemap_photos_are_public_local_files_allowed_by_robots(self):
        robots = RobotFileParser(); robots.parse((ROOT / 'robots.txt').read_text().splitlines())
        for image in self.sitemap.findall('s:url/i:image/i:loc', self.ns):
            url = image.text
            self.assertTrue(url.startswith(site.BASE_URL + '/assets/'))
            self.assertTrue((ROOT / urlsplit(url).path.lstrip('/')).is_file())
            self.assertTrue(robots.can_fetch('Googlebot-Image', url))
            self.assertNotIn('?', url); self.assertNotIn('#', url)

    def test_seo_additions_keep_one_visible_carousel_photo_and_no_fake_rich_result_fields(self):
        for slug, html in self.pages.items():
            attr = 'data-sand-photo' if slug == 'colour-coated-silica-sand' else 'data-product-photo'
            self.assertEqual(len([a for t, a in Tags(html).tags if t == 'img' and attr in a]), 1)
            for field in ('offers', 'review', 'aggregateRating', 'manufacturer'):
                self.assertNotIn(field, self.schemas[slug])
            self.assertIn('content="index,follow"', html)
            self.assertIn('rel="canonical" href="' + site.BASE_URL + '/products/' + slug + '/"', html)
        self.assertEqual(len(site.PRODUCTS), 11); self.assertEqual(len(site.CATALOGUE_PRODUCTS), 16)


if __name__ == '__main__': unittest.main()
