"""Salt gallery and client-approved iodine wording remain factual and scoped."""
import json
from pathlib import Path
import re
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
import generate_site as site
from templates import salt_gallery
from test_bentonite_media import Tags


class SaltGalleryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = salt_gallery.catalogue()
        cls.html = site.render_product_page(site.PRODUCTS_BY_SLUG['salt'])
        cls.tags = Tags(cls.html).tags

    def test_all_five_supplied_photos_keep_their_order_and_label_names(self):
        self.assertEqual(len(self.entries), 5)
        self.assertEqual([e['id'] for e in self.entries], ['view-1','view-2','view-3','view-4','view-5'])
        self.assertEqual([e['name'] for e in self.entries],
                         ['Non-iodized salt','Raw salt','Iodized salt','Oversized salt','Industrial salt'])
        self.assertTrue(all((e['width'],e['height']) == (1200,1600) for e in self.entries))

    def test_iodine_customization_is_visible_without_changing_published_grade_values(self):
        gallery = self.html.split('id="salt-gallery"', 1)[1].split('</section>', 1)[0]
        self.assertIn(salt_gallery.IODINE_NOTE, gallery)
        self.assertIn('25-30 PPM for edible grades', self.html)
        self.assertIn('Iodine NIL for non-consumption grades', self.html)
        self.assertIn('Confirm the required grade and iodine level with your enquiry.', gallery)
        self.assertNotRegex(gallery, r'(?i)certified|guaranteed|pharmaceutical|health benefit')
        self.assertIn('customizable to client requirements', site.PRODUCTS_BY_SLUG['salt']['meta_description'])

    def test_one_full_photo_and_manual_accessible_controls_are_server_rendered(self):
        photos = [a for t,a in self.tags if t == 'img' and 'data-salt-photo' in a]
        self.assertEqual(len(photos), 1)
        self.assertEqual(photos[0]['src'], 'assets/salt/salt-view-1.webp')
        self.assertEqual(photos[0]['loading'], 'lazy')
        carousel = next(a for t,a in self.tags if 'data-salt-carousel' in a)
        self.assertEqual(carousel['role'], 'region')
        self.assertEqual(carousel['aria-roledescription'], 'carousel')
        self.assertEqual(carousel['tabindex'], '0')
        self.assertEqual(len([1 for t,a in self.tags if 'data-salt-prev' in a or 'data-salt-next' in a]), 2)
        self.assertEqual(len([1 for t,a in self.tags if t == 'select' and 'data-salt-select' in a]), 1)
        self.assertIn('<noscript>', self.html)

    def test_converted_images_are_small_webp_without_exif_or_xmp_chunks(self):
        total = 0
        for entry in self.entries:
            data = (ROOT/entry['src']).read_bytes(); total += len(data)
            self.assertEqual(data[:4], b'RIFF'); self.assertEqual(data[8:12], b'WEBP')
            self.assertLess(len(data), 300_000)
            offset, chunks = 12, []
            while offset+8 <= len(data):
                size = int.from_bytes(data[offset+4:offset+8], 'little')
                chunks.append(data[offset:offset+4]); offset += 8+size+(size % 2)
            self.assertNotIn(b'EXIF', chunks); self.assertNotIn(b'XMP ', chunks)
        self.assertLess(total, 1_200_000)

    def test_schema_and_sitemap_cover_the_hero_and_five_actual_photos(self):
        schemas = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', self.html, re.S).group(1))
        product = next(s for s in schemas if s['@type'] == 'Product')
        self.assertEqual(product['image'], [site.BASE_URL+site.PRODUCT_VISUALS['salt']['hero']] + [site.BASE_URL+'/'+e['src'] for e in self.entries])
        self.assertEqual(site.product_sitemap_images('/products/salt/'), product['image'])
        self.assertEqual(product['additionalProperty'], [{'@type':'PropertyValue','name':'Iodine content','value':'Customizable as per client requirements'}])
        self.assertEqual(site.page_lastmod('/products/salt/'), '2026-10-21')
        for field in ('offers','aggregateRating','review'): self.assertNotIn(field, product)

    def test_the_gallery_does_not_replace_documents_or_leak_to_other_products(self):
        self.assertIn('assets/tds/salt-technical-data-sheet.pdf', self.html)
        self.assertIn('assets/coas/salt-sample-coa.pdf', self.html)
        self.assertIn('data-inquiry-form', self.html)
        self.assertIn('google.com/recaptcha/api.js', self.html)
        for product in site.CATALOGUE_PRODUCTS:
            if product['slug'] == 'salt': continue
            html = site.render_product_page(product)
            self.assertNotIn('data-salt-carousel', html)
            self.assertNotIn('salt/carousel.js', html)
        self.assertNotIn('IMG_3497', self.html); self.assertNotIn('.HEIC', self.html)
        self.assertNotIn('/Users/', self.html)

    def test_photo_fitting_and_mobile_controls_remain_restrained(self):
        css = (ROOT/'assets/salt/carousel.css').read_text()
        self.assertIn('object-fit: contain', css)
        self.assertIn('aspect-ratio: 3 / 4', css)
        self.assertIn('touch-action: pan-y', css)
        self.assertIn('.salt-controls[hidden] { display: none; }', css)
        self.assertIn('min-width: 44px; min-height: 44px', css)
        self.assertIn('prefers-reduced-motion: reduce', css)


if __name__ == '__main__': unittest.main()
