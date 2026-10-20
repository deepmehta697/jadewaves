"""Bentonite media source checks; no encoder or browser dependency in builds."""
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
import generate_site as site


class Tags(HTMLParser):
    def __init__(self, html):
        super().__init__(); self.tags = []; self.feed(html)
    def handle_starttag(self, tag, attrs): self.tags.append((tag, dict(attrs)))


def boxes(data, start=0, end=None):
    """Read the bounded ISO-BMFF boxes used by this small fast-start MP4."""
    end = len(data) if end is None else end
    while start + 8 <= end:
        size = int.from_bytes(data[start:start+4], 'big')
        kind = data[start+4:start+8]
        header = 8
        if size == 1:
            size = int.from_bytes(data[start+8:start+16], 'big'); header = 16
        if size == 0: size = end - start
        if size < header or start+size > end: raise ValueError('Invalid MP4 box')
        yield kind, start+header, start+size
        start += size


class BentoniteMediaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = site.render_product_page(site.PRODUCTS_BY_SLUG['bentonite'])
        cls.tags = Tags(cls.html).tags

    def test_attached_clay_photo_replaces_the_old_dish_photo(self):
        visual = site.PRODUCT_VISUALS['bentonite']
        self.assertEqual(visual['hero'], '/assets/bentonite/bentonite-clay.webp')
        self.assertEqual(visual['thumb'], visual['hero'])
        self.assertNotIn('bentonite-sample-reference', self.html)
        self.assertNotIn('glass dish', self.html)
        hero = next(a for t, a in self.tags if t == 'img' and a.get('class') == 'ml-hero-media')
        self.assertIn('assets/bentonite/bentonite-clay', hero['src'])
        self.assertEqual((hero['width'], hero['height']), ('1000', '1000'))
        schema = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', self.html, re.S).group(1))
        self.assertEqual(next(s for s in schema if s['@type'] == 'Product')['image'], site.BASE_URL + visual['hero'])

    def test_both_old_plant_occurrences_are_removed_and_video_is_shown_once(self):
        self.assertNotIn('packing-area', self.html)
        videos = [a for t, a in self.tags if t == 'video']
        self.assertEqual(len(videos), 1)
        video = videos[0]
        for attribute in ('controls', 'muted', 'playsinline'): self.assertIn(attribute, video)
        self.assertNotIn('autoplay', video); self.assertNotIn('loop', video)
        self.assertEqual(video['preload'], 'none')
        self.assertEqual((video['width'], video['height']), ('848', '480'))
        self.assertEqual(video['poster'], 'assets/bentonite/bentonite-clip-poster.webp')
        self.assertEqual([a['type'] for t, a in self.tags if t == 'source'], ['video/mp4', 'video/webm'])
        for t, a in self.tags:
            if t == 'source': self.assertTrue((ROOT/a['src']).is_file())

    def test_other_product_packing_photos_and_protected_forms_are_preserved(self):
        silica = site.render_product_page(site.PRODUCTS_BY_SLUG['silica-sand'])
        self.assertIn('packing-area', silica)
        self.assertNotIn('bentonite-clip', silica)
        self.assertIn('data-inquiry-form', self.html)
        self.assertIn('google.com/recaptcha/api.js', self.html)

    def test_mp4_is_fast_start_with_exactly_one_video_track_and_no_audio(self):
        path = ROOT/'assets/bentonite/bentonite-clip.mp4'
        data = path.read_bytes()
        self.assertLess(len(data), 1_100_000)
        top = list(boxes(data)); kinds = [kind for kind, _, _ in top]
        self.assertLess(kinds.index(b'moov'), kinds.index(b'mdat'))
        _, start, end = next(b for b in top if b[0] == b'moov')
        handlers = []
        for kind, ts, te in boxes(data, start, end):
            if kind != b'trak': continue
            for kind, ms, me in boxes(data, ts, te):
                if kind != b'mdia': continue
                for kind, hs, he in boxes(data, ms, me):
                    if kind == b'hdlr': handlers.append(data[hs+8:hs+12])
        self.assertEqual(handlers, [b'vide'])
        self.assertIn(b'avc1', data)

    def test_webm_and_responsive_photo_files_are_present(self):
        webm = (ROOT/'assets/bentonite/bentonite-clip.webm').read_bytes()
        self.assertEqual(webm[:4], b'\x1aE\xdf\xa3')
        self.assertIn(b'V_VP9', webm)
        self.assertLess(len(webm), 1_400_000)
        manifest = json.loads((ROOT/'assets/responsive/manifest.json').read_text())['/assets/bentonite/bentonite-clay.webp']
        self.assertEqual((manifest['width'], manifest['height']), (1000, 1000))
        self.assertEqual([v['width'] for v in manifest['variants']], [160, 480, 960, 1000])
        for variant in manifest['variants']: self.assertTrue((ROOT/variant['src'].lstrip('/')).is_file())
        self.assertEqual(site.page_lastmod('/products/bentonite/'), '2026-10-20')


if __name__ == '__main__': unittest.main()
