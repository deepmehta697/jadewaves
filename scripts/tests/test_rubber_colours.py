"""Rubber colour references remain distinct from grade/performance evidence."""
import json
from pathlib import Path
import re
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
import generate_site as site
from templates import rubber_granules
from test_bentonite_media import Tags


class RubberColourTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = rubber_granules.catalogue()
        cls.html = site.render_product_page(site.PRODUCTS_BY_SLUG['rubber-granules'])
        cls.tags = Tags(cls.html).tags

    def test_black_first_then_all_22_printed_chart_references_in_order(self):
        self.assertEqual(len(self.entries), 23)
        self.assertEqual(self.entries[0]['id'], 'black')
        self.assertIsNone(self.entries[0]['ral'])
        self.assertEqual([e['source_code'] for e in self.entries[1:]], [str(i).zfill(3) for i in range(20,42)])
        self.assertEqual([e['ral'] for e in self.entries[1:]],
                         ['9010','1015','1014','1002','1012','6017','6021','6005','5018','5012','5015','5010','4003','4005','2008','3017','3016','8024','8025','7038','7037','7011'])
        self.assertEqual(len({e['id'] for e in self.entries}), 23)

    def test_one_server_rendered_photo_with_native_manual_accessible_controls(self):
        photos = [a for t,a in self.tags if t == 'img' and 'data-rubber-photo' in a]
        self.assertEqual(len(photos), 1)
        self.assertEqual(photos[0]['src'], 'assets/rubber-granules/black.webp')
        self.assertEqual((photos[0]['width'], photos[0]['height']), ('300', '300'))
        self.assertEqual(photos[0]['loading'], 'lazy')
        carousel = next(a for t,a in self.tags if 'data-rubber-carousel' in a)
        self.assertEqual(carousel['aria-roledescription'], 'carousel')
        self.assertEqual(carousel['tabindex'], '0')
        self.assertEqual(len([1 for t,a in self.tags if 'data-rubber-prev' in a or 'data-rubber-next' in a]), 2)
        self.assertIn('noscript', [t for t,a in self.tags])

    def test_assets_are_local_bounded_and_keep_their_real_intrinsic_sizes(self):
        for entry in self.entries:
            data = (ROOT/entry['src']).read_bytes()
            self.assertEqual(data[:4], b'RIFF')
            self.assertEqual(data[8:12], b'WEBP')
            self.assertGreater(entry['width'], 100)
            self.assertGreater(entry['height'], 100)
            self.assertLess(len(data), 150_000)
        self.assertLess(sum((ROOT/e['src']).stat().st_size for e in self.entries), 1_500_000)

    def test_no_grade_price_or_ral_certification_is_invented(self):
        section = self.html.split('id="colour-range"', 1)[1].split('</section>', 1)[0]
        self.assertIn('Chart references only.', section)
        self.assertIn('Confirm material type, grading and shade with a sample.', section)
        self.assertNotRegex(section, r'(?i)certified|epdm|guaranteed|price|RAL 9005')
        self.assertNotIn('<video ', section)
        self.assertIn('id="technical-documents"', self.html)
        self.assertIn('Request grade and specification details', self.html)
        self.assertIn('google.com/recaptcha/api.js', self.html)
        self.assertIn('data-inquiry-form', self.html)

    def test_schema_and_image_sitemap_include_hero_and_all_23_references(self):
        schemas = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', self.html, re.S).group(1))
        product = next(s for s in schemas if s['@type'] == 'Product')
        self.assertEqual(len(product['image']), 24)
        self.assertEqual(product['image'][1:], [site.BASE_URL+'/'+e['src'] for e in self.entries])
        self.assertEqual(product['color'], [e['name'] for e in self.entries])
        self.assertEqual(site.product_sitemap_images('/products/rubber-granules/'), product['image'])
        self.assertFalse(any(s['@type'] == 'VideoObject' for s in schemas))

    def test_carousel_is_exclusive_to_rubber_and_preserves_other_pages(self):
        for product in site.CATALOGUE_PRODUCTS:
            if product['slug'] == 'rubber-granules': continue
            html = site.render_product_page(product)
            self.assertNotIn('data-rubber-carousel', html)
            self.assertNotIn('rubber-granules/carousel.js', html)
        self.assertEqual(len(site.PRODUCTS), 11)
        self.assertEqual(len(site.CATALOGUE_PRODUCTS), 16)

    def test_styles_contain_images_and_support_reduced_motion_and_mobile(self):
        css = (ROOT/'assets/rubber-granules/carousel.css').read_text()
        self.assertIn('object-fit: contain', css)
        self.assertIn('touch-action: pan-y', css)
        self.assertIn('prefers-reduced-motion: reduce', css)
        self.assertIn('min-width: 44px; min-height: 44px', css)


if __name__ == '__main__': unittest.main()
