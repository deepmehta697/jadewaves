"""Copper Slag clip is silent, web-ready and exclusive to its product page."""
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
import generate_site as site
from test_bentonite_media import Tags, boxes


class CopperSlagMediaTests(unittest.TestCase):
    def test_single_manual_video_beside_the_existing_technical_documents(self):
        html = site.render_product_page(site.PRODUCTS_BY_SLUG['copper-slag'])
        section = html.split('id="technical-documents"', 1)[1].split('</section>', 1)[0]
        tags = Tags(section).tags
        videos = [a for t,a in tags if t == 'video']
        self.assertEqual(len(videos), 1)
        video = videos[0]
        for attr in ('controls', 'muted', 'playsinline'): self.assertIn(attr, video)
        for attr in ('autoplay', 'loop'): self.assertNotIn(attr, video)
        self.assertEqual(video['preload'], 'none')
        self.assertEqual((video['width'], video['height']), ('540', '960'))
        self.assertEqual(video['poster'], 'assets/copper-slag/copper-slag-footage-poster.webp')
        self.assertEqual([a['type'] for t,a in tags if t == 'source'], ['video/mp4', 'video/webm'])
        self.assertIn('assets/tds/copper-slag-technical-data-sheet.pdf', section)
        self.assertIn('assets/coas/copper-slag-sample-coa.pdf', section)
        self.assertIn('>Copper slag footage</figcaption>', section)
        self.assertIn('ml-product-video--portrait', section)
        self.assertNotIn('packing-area', html)
        self.assertNotIn('Silent clip.', html)

    def test_video_is_not_added_to_other_product_pages_or_homepage(self):
        for p in site.CATALOGUE_PRODUCTS:
            if p['slug'] == 'copper-slag': continue
            self.assertNotIn('copper-slag-footage', site.render_product_page(p))
        self.assertNotIn('copper-slag-footage', site.render_homepage())

    def test_mp4_is_fast_start_h264_and_only_has_a_video_track(self):
        data = (ROOT/'assets/copper-slag/copper-slag-footage.mp4').read_bytes()
        self.assertLess(len(data), 4_000_000)
        top = list(boxes(data)); kinds = [k for k,_,_ in top]
        self.assertLess(kinds.index(b'moov'), kinds.index(b'mdat'))
        _,start,end = next(b for b in top if b[0] == b'moov')
        handlers = []
        for kind,ts,te in boxes(data,start,end):
            if kind != b'trak': continue
            for kind,ms,me in boxes(data,ts,te):
                if kind != b'mdia': continue
                for kind,hs,_ in boxes(data,ms,me):
                    if kind == b'hdlr': handlers.append(data[hs+8:hs+12])
        self.assertEqual(handlers, [b'vide'])
        self.assertIn(b'avc1', data)
        for tag in (b'com.apple.quicktime', b'\xa9xyz', b'IMG_1133'):
            self.assertNotIn(tag, data)

    def test_fallback_poster_and_recorded_modification_date(self):
        data = (ROOT/'assets/copper-slag/copper-slag-footage.webm').read_bytes()
        self.assertEqual(data[:4], b'\x1aE\xdf\xa3')
        self.assertIn(b'V_VP9', data)
        self.assertNotIn(b'A_OPUS', data)
        self.assertNotIn(b'com.apple.quicktime', data)
        poster = (ROOT/'assets/copper-slag/copper-slag-footage-poster.webp').read_bytes()
        self.assertEqual(poster[:4], b'RIFF')
        self.assertEqual(poster[8:12], b'WEBP')
        self.assertEqual(site.page_lastmod('/products/copper-slag/'), '2026-10-21')
        html = site.render_product_page(site.PRODUCTS_BY_SLUG['copper-slag'])
        # Publication date is not invented from the phone's recording timestamp.
        self.assertNotIn('"@type": "VideoObject"', html)


if __name__ == '__main__': unittest.main()
