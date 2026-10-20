"""Homepage dispatch replaces repeated plant photography, not product footage."""
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
import generate_site as site
from test_bentonite_media import Tags, boxes


class HomeDispatchTests(unittest.TestCase):
    def test_supply_route_retains_four_steps_without_the_plant_image(self):
        html = site.render_homepage()
        process = html.split('id="process"', 1)[1].split('</section>', 1)[0]
        self.assertEqual(process.count('class="ml-process-step"'), 4)
        self.assertNotIn('<img ', process)
        self.assertNotIn('packing-area', html)

    def test_dispatch_replaces_the_entire_field_evidence_gallery(self):
        html = site.render_homepage()
        self.assertNotIn('Field evidence', html)
        self.assertNotIn('class="ml-gallery"', html)
        self.assertNotIn('The material. The handling. The paperwork.', html)
        self.assertIn('>Dispatch footage</p>', html)
        self.assertIn('href="operations/"', html)
        self.assertLess(html.index('id="process"'), html.index('id="dispatch-footage"'))
        self.assertLess(html.index('id="dispatch-footage"'), html.index('id="countries-served"'))

    def test_two_muted_on_demand_dispatch_videos_with_correct_sources_and_posters(self):
        html = site.render_homepage()
        tags = Tags(html).tags
        videos = [a for t, a in tags if t == 'video']
        self.assertEqual(len(videos), 2)
        for video, dimensions, poster in zip(videos, [('1280', '720'), ('474', '850')],
                ['assets/jcb-poster.jpg', 'assets/dispatch/dispatch-loading-poster.webp']):
            for attr in ('controls', 'muted', 'playsinline'): self.assertIn(attr, video)
            for attr in ('autoplay', 'loop'): self.assertNotIn(attr, video)
            self.assertEqual(video['preload'], 'none')
            self.assertEqual((video['width'], video['height']), dimensions)
            self.assertEqual(video['poster'], poster)
            self.assertTrue((ROOT/poster).is_file())
        self.assertEqual([a for t, a in tags if t == 'source'],
                         [{'src': 'assets/jcb.mp4', 'type': 'video/mp4'},
                          {'src': 'assets/dispatch/dispatch-loading.mp4', 'type': 'video/mp4'}])
        self.assertNotIn('product-handling/material-handling', html)
        self.assertNotIn('feldspar-footage', html)
        self.assertNotIn('assets/loading.mp4', html)
        self.assertNotIn('Bag loading in the dispatch yard', html)
        self.assertIn('Loading activity during cargo preparation', html)

    def test_dispatch_asset_is_small_fast_start_and_has_no_audio_track(self):
        for path, budget in [('assets/jcb.mp4', 3_500_000),
                             ('assets/dispatch/dispatch-loading.mp4', 1_700_000)]:
            with self.subTest(path=path):
                self.check_dispatch_asset(path, budget)

    def check_dispatch_asset(self, path, budget):
        data = (ROOT/path).read_bytes()
        self.assertLess(len(data), budget)
        top = list(boxes(data)); kinds = [k for k, _, _ in top]
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

    def test_new_dispatch_clip_is_not_added_to_any_product_page(self):
        for product in site.CATALOGUE_PRODUCTS:
            self.assertNotIn('assets/dispatch/', site.render_product_page(product))


if __name__ == '__main__': unittest.main()
