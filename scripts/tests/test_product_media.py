"""Product footage contracts, without a build-time media encoder dependency."""
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
import generate_site as site
from test_bentonite_media import Tags, boxes


class ProductMediaTests(unittest.TestCase):
    def test_no_product_page_retains_the_plant_photo(self):
        for product in site.CATALOGUE_PRODUCTS:
            with self.subTest(slug=product['slug']):
                html = site.render_product_page(product)
                self.assertNotIn('packing-area', html)
                self.assertNotIn('Silent clip. Visual reference', html)
                self.assertNotIn('IMG_3390', html)
                self.assertNotIn('/Users/', html)

    def test_only_three_core_pages_have_their_assigned_video_beside_documents(self):
        assigned = {'bentonite': 'bentonite/bentonite-clip',
                    'feldspar': 'feldspar/feldspar-footage',
                    'quartz-sand-for-ceramics': 'product-handling/material-handling'}
        for product in site.PRODUCTS:
            with self.subTest(slug=product['slug']):
                html = site.render_product_page(product)
                tags = Tags(html).tags
                videos = [a for t, a in tags if t == 'video']
                if product['slug'] not in assigned:
                    self.assertEqual(videos, [])
                    self.assertNotIn('product-handling/material-handling', html)
                    self.assertIn('ml-document-layout--documents-only', html)
                    continue
                self.assertEqual(len(videos), 1)
                video = videos[0]
                for attr in ('controls', 'muted', 'playsinline'):
                    self.assertIn(attr, video)
                for attr in ('autoplay', 'loop'):
                    self.assertNotIn(attr, video)
                self.assertEqual(video['preload'], 'none')
                section = html.split('id="technical-documents"', 1)[1].split('</section>', 1)[0]
                self.assertIn('<video ', section)
                stem = assigned[product['slug']]
                sources = [a for t, a in tags if t == 'source']
                self.assertEqual([a['src'] for a in sources],
                                 [f'assets/{stem}.mp4', f'assets/{stem}.webm'])
                self.assertEqual([a['type'] for a in sources], ['video/mp4', 'video/webm'])
                for path in [video['poster'], *(a['src'] for a in sources)]:
                    self.assertTrue((ROOT/path).is_file(), path)
                if product['slug'] != 'bentonite':
                    self.assertEqual((video['width'], video['height']), ('540', '960'))
                    self.assertIn('ml-product-video--portrait', html)
                self.assertEqual(site.page_lastmod(f"/products/{product['slug']}/"), '2026-10-20')

    def test_img_3350_is_exclusive_to_quartz_across_all_product_pages(self):
        for product in site.CATALOGUE_PRODUCTS:
            html = site.render_product_page(product)
            self.assertEqual('product-handling/material-handling' in html,
                             product['slug'] == 'quartz-sand-for-ceramics', product['slug'])

    def test_decorative_carousels_are_not_given_extra_videos(self):
        for product in site.CATALOGUE_PRODUCTS:
            if product['slug'] in site.PRODUCTS_BY_SLUG:
                continue
            html = site.render_product_page(product)
            self.assertNotIn('<video ', html)

    def test_export_market_photo_and_existing_bentonite_clip_are_kept(self):
        self.assertNotIn('packing-area', site.render_homepage())
        self.assertIn('packing-area', site.render_export_markets_page())
        html = site.render_product_page(site.PRODUCTS_BY_SLUG['bentonite'])
        self.assertIn('>Bentonite yard footage</figcaption>', html)
        self.assertNotIn('feldspar-footage', html)
        self.assertNotIn('material-handling', html)

    def test_new_mp4s_are_fast_start_with_one_video_track_only(self):
        for stem, budget in [('product-handling/material-handling', 3_600_000),
                             ('feldspar/feldspar-footage', 1_900_000)]:
            with self.subTest(stem=stem):
                data = (ROOT/f'assets/{stem}.mp4').read_bytes()
                self.assertLess(len(data), budget)
                top = list(boxes(data))
                kinds = [kind for kind, _, _ in top]
                self.assertLess(kinds.index(b'moov'), kinds.index(b'mdat'))
                _, start, end = next(b for b in top if b[0] == b'moov')
                handlers = []
                for kind, ts, te in boxes(data, start, end):
                    if kind != b'trak': continue
                    for kind, ms, me in boxes(data, ts, te):
                        if kind != b'mdia': continue
                        for kind, hs, _ in boxes(data, ms, me):
                            if kind == b'hdlr': handlers.append(data[hs+8:hs+12])
                self.assertEqual(handlers, [b'vide'])
                self.assertIn(b'avc1', data)
                for tag in (b'com.apple.quicktime.location', b'com.apple.quicktime.make',
                            b'com.apple.quicktime.model', b'\xa9xyz'):
                    self.assertNotIn(tag, data)
                webm = (ROOT/f'assets/{stem}.webm').read_bytes()
                self.assertEqual(webm[:4], b'\x1aE\xdf\xa3')
                self.assertIn(b'V_VP9', webm)
                self.assertNotIn(b'A_OPUS', webm)

    def test_portrait_layout_preserves_full_frame_with_bounded_height(self):
        css = (ROOT/'templates/material-ledger.css').read_text()
        self.assertIn('.ml-evidence.ml-product-video video {', css)
        self.assertIn('aspect-ratio: 848 / 480; object-fit: contain;', css)
        self.assertIn('.ml-evidence.ml-product-video--portrait video { height: min(480px, 70svh); aspect-ratio: auto; }', css)


if __name__ == '__main__': unittest.main()
