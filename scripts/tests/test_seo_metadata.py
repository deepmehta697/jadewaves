"""Offline SEO regressions: dates, catalogue coverage, and route identity."""

from datetime import date
from pathlib import Path
import sys
import unittest
from unittest.mock import patch
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
import generate_site as site
from templates.product_guides import PRODUCT_GUIDES


class SEORegressionTests(unittest.TestCase):
    def test_eleven_products_retained(self):
        self.assertEqual(len(site.PRODUCTS), 11)
        self.assertEqual(len({p['slug'] for p in site.PRODUCTS}), 11)

    def test_eight_new_guides_cover_underserved_products(self):
        self.assertEqual(len(PRODUCT_GUIDES), 8)
        self.assertEqual({p['product_slug'] for p in PRODUCT_GUIDES}, {
            'silica-flour', 'bentonite', 'kaolin--china-clay', 'talc',
            'salt', 'fly-ash', 'copper-slag', 'rubber-granules',
        })
        self.assertEqual(len(site.BLOGS), 15)
        self.assertEqual(len({p['slug'] for p in site.BLOGS}), 15)
        self.assertEqual({p['product_slug'] for p in site.BLOGS}, set(site.PRODUCTS_BY_SLUG))

    def test_dates_do_not_follow_the_build_clock(self):
        expected_sitemap = site.render_sitemap()
        expected_dates = [site.article_dates(post) for post in site.BLOGS]
        # Catch reintroduction of the old TODAY/BUILD_VERSION date coupling.
        with patch.object(site, 'TODAY', '2099-12-31', create=True), patch.object(site, 'BUILD_VERSION', '20991231000000'):
            self.assertEqual(site.render_sitemap(), expected_sitemap)
            self.assertEqual([site.article_dates(post) for post in site.BLOGS], expected_dates)

    def test_dates_are_valid_and_not_inverted(self):
        for post in site.BLOGS:
            with self.subTest(post=post['slug']):
                dates = site.article_dates(post)
                for value in dates.values():
                    self.assertEqual(date.fromisoformat(value).isoformat(), value)
                if 'datePublished' in dates and 'dateModified' in dates:
                    self.assertLessEqual(dates['datePublished'], dates['dateModified'])

    def test_released_guides_retain_the_recorded_publication_date(self):
        for post in PRODUCT_GUIDES:
            with self.subTest(post=post['slug']):
                self.assertEqual(site.article_dates(post).get('datePublished'), '2026-10-13')
                self.assertEqual(site.article_dates(post).get('dateModified'), '2026-10-13')

    def test_unknown_dates_are_omitted(self):
        self.assertEqual(site.article_dates({'slug': 'not-a-published-guide'}), {})

    def test_invalid_dates_fail_instead_of_entering_schema(self):
        for post in [
            {'slug': 'test', 'date_modified': '2026-02-30'},
            {'slug': 'test', 'date_published': '2026-10-13', 'date_modified': '2026-10-12'},
        ]:
            with self.subTest(post=post), self.assertRaises(ValueError):
                site.article_dates(post)

    def test_sitemap_contains_only_active_routes(self):
        ns = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        sitemap = ET.fromstring(site.render_sitemap())
        urls = [n.text for n in sitemap.findall('s:url/s:loc', ns)]
        self.assertEqual(len(urls), 39)
        self.assertEqual(len(set(urls)), 39)
        self.assertIn(site.BASE_URL + '/products/glass-chips/', urls)
        self.assertIn(site.BASE_URL + '/products/grout-sand/', urls)
        self.assertIn(site.BASE_URL + '/products/colour-coated-silica-sand/', urls)
        self.assertIn(site.BASE_URL + '/products/pebbles/', urls)
        for post in site.BLOGS:
            self.assertIn(site.BASE_URL + '/blog/' + post['slug'] + '/', urls)
        for url in urls:
            self.assertNotIn('/blog/blog/', url)

    def test_no_active_page_is_overwritten_by_a_redirect(self):
        active = {f'products/{p["slug"]}' for p in site.CATALOGUE_PRODUCTS}
        active.update(f'blog/{p["slug"]}' for p in site.BLOGS)
        redirects = set(site.LEGACY_REDIRECTS)
        redirects.update(path for path, _, _ in site.malformed_redirect_entries())
        self.assertFalse(active & redirects)

    def test_search_snippets_are_natural_and_unique(self):
        posts = site.PRODUCTS + site.BLOGS
        titles = [p['seo_title'] for p in posts]
        descriptions = [p['meta_description'] for p in posts]
        self.assertEqual(len(titles), len(set(titles)))
        self.assertEqual(len(descriptions), len(set(descriptions)))
        for title, description in zip(titles, descriptions):
            self.assertTrue(title.strip())
            self.assertTrue(description.strip())
            self.assertNotRegex(title + description, r'<[^>]+>')


if __name__ == '__main__':
    unittest.main()
