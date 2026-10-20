"""Media discovery and factual metadata for the October product/home releases."""
from datetime import datetime
import json
from pathlib import Path
import re
import sys
import unittest
from unittest.mock import patch
from urllib.parse import urlsplit
from urllib.robotparser import RobotFileParser

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
import generate_site as site
from templates import media_seo, pebbles
from test_bentonite_media import Tags, boxes


def schemas(html):
    return json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', html, re.S).group(1))


class MediaSEOTests(unittest.TestCase):
    def test_every_product_shares_its_real_photo_not_the_company_logo(self):
        for product in site.CATALOGUE_PRODUCTS:
            with self.subTest(slug=product['slug']):
                html = site.render_product_page(product)
                data = next(item for item in schemas(html) if item['@type'] == 'Product')
                photo = data['image'][0] if isinstance(data['image'], list) else data['image']
                tags = Tags(html).tags
                metas = {a.get('property', a.get('name')): a.get('content') for t, a in tags if t == 'meta'}
                self.assertEqual(metas['og:image'], photo)
                self.assertEqual(metas['twitter:image'], photo)
                self.assertEqual(metas['twitter:title'], product['seo_title'])
                self.assertEqual(metas['twitter:description'], product['meta_description'])
                self.assertTrue(metas['og:image:alt'])
                self.assertEqual(metas['og:image:alt'], metas['twitter:image:alt'])
                self.assertEqual(metas['twitter:card'], 'summary_large_image')
                self.assertTrue((ROOT/urlsplit(photo).path.lstrip('/')).is_file())

    def test_articles_share_their_actual_image_and_use_article_type(self):
        for post in site.BLOGS:
            html = site.render_blog_post_page(post)
            article = next(item for item in schemas(html) if item['@type'] == 'BlogPosting')
            metas = {a.get('property', a.get('name')): a.get('content') for t, a in Tags(html).tags if t == 'meta'}
            self.assertEqual(metas['og:image'], article['image'])
            self.assertEqual(metas['twitter:image'], article['image'])
            self.assertEqual(metas['og:type'], 'article')
            self.assertTrue(article['publisher']['logo']['url'].endswith('/jade-waves-logo-transparent.png'))

    def test_only_the_assigned_recent_videos_have_schema_on_each_page(self):
        for product in site.CATALOGUE_PRODUCTS:
            html = site.render_product_page(product)
            videos = [item for item in schemas(html) if item['@type'] == 'VideoObject']
            expected = {'bentonite': '/assets/bentonite/bentonite-clip.mp4',
                        'feldspar': '/assets/feldspar/feldspar-footage.mp4',
                        'quartz-sand-for-ceramics': '/assets/product-handling/material-handling.mp4'}.get(product['slug'])
            self.assertEqual([v['contentUrl'] for v in videos], [site.BASE_URL+expected] if expected else [])
            if videos:
                item = next(item for item in schemas(html) if item['@type'] == 'Product')
                self.assertEqual(item['subjectOf'], [{'@id': videos[0]['@id']}])
        home = site.render_homepage()
        videos = [item for item in schemas(home) if item['@type'] == 'VideoObject']
        self.assertEqual([v['contentUrl'] for v in videos], [site.BASE_URL+'/assets/dispatch/dispatch-loading.mp4'])
        self.assertIn('assets/jcb.mp4', home)
        # No invented legacy uploadDate, watch-page URL, or fake embed endpoint.
        self.assertNotIn('embedUrl', videos[0])
        self.assertFalse(any(item['@type'] == 'VideoObject' for item in schemas(site.material_support.render_operations_page(vars(site)))))

    def test_video_fields_match_visible_sources_posters_and_publication_evidence(self):
        pages = [('/', site.render_homepage())] + [('/products/'+p['slug']+'/', site.render_product_page(p)) for p in site.PRODUCTS]
        for path, html in pages:
            tags = Tags(html).tags
            sources = {site.BASE_URL+'/'+a['src'].lstrip('/') for t, a in tags if t == 'source'}
            posters = {site.BASE_URL+'/'+a['poster'].lstrip('/') for t, a in tags if t == 'video'}
            for video in [item for item in schemas(html) if item['@type'] == 'VideoObject']:
                self.assertIn(video['contentUrl'], sources)
                self.assertEqual(len(video['thumbnailUrl']), 1)
                self.assertIn(video['thumbnailUrl'][0], posters)
                self.assertEqual(video['isPartOf']['@id'], site.BASE_URL+path)
                self.assertTrue(video['name']); self.assertTrue(video['description'])
                self.assertEqual(datetime.fromisoformat(video['uploadDate'].replace('Z', '+00:00')).date().isoformat(), '2026-10-20')
                for field in ('interactionStatistic', 'expires', 'regionsAllowed', 'hasPart', 'potentialAction'):
                    self.assertNotIn(field, video)

    def test_durations_match_real_mp4_headers_and_media_are_crawlable(self):
        robots = RobotFileParser(); robots.parse(site.render_robots().splitlines())
        for source, info in media_seo.VIDEOS.items():
            data = (ROOT/source.lstrip('/')).read_bytes()
            _, start, end = next(b for b in boxes(data) if b[0] == b'moov')
            _, start, _ = next(b for b in boxes(data, start, end) if b[0] == b'mvhd')
            self.assertEqual(data[start], 0)
            seconds = int.from_bytes(data[start+16:start+20], 'big') / int.from_bytes(data[start+12:start+16], 'big')
            self.assertAlmostEqual(seconds, float(info['duration'][2:-1]), places=3)
            for path in (source, info['thumbnail']):
                self.assertTrue((ROOT/path.lstrip('/')).is_file())
                self.assertTrue(robots.can_fetch('Googlebot', site.BASE_URL+path))

    def test_video_dates_do_not_follow_build_or_camera_timestamps(self):
        expected = schemas(site.render_homepage())
        with patch.object(site, 'BUILD_VERSION', '20991231000000'):
            self.assertEqual(schemas(site.render_homepage()), expected)
        self.assertEqual(media_seo.VIDEOS['/assets/dispatch/dispatch-loading.mp4']['uploadDate'], '2026-10-20T10:30:40Z')

    def test_pebbles_has_all_31_photos_and_natural_supplier_metadata(self):
        product = next(item for item in schemas(site.render_product_page(pebbles.PRODUCT)) if item['@type'] == 'Product')
        self.assertEqual(product['image'], [site.BASE_URL+'/'+photo['src'] for photo in pebbles.catalogue()])
        self.assertIn('Supplier in India', pebbles.PRODUCT['seo_title'])
        for field in ('offers', 'aggregateRating', 'review'): self.assertNotIn(field, product)

    def test_core_product_sitemap_uses_the_current_hero_including_bentonite(self):
        for product in site.PRODUCTS:
            self.assertEqual(site.product_sitemap_images('/products/'+product['slug']+'/'),
                             [site.BASE_URL+site.PRODUCT_VISUALS[product['slug']]['hero']])
        self.assertEqual(site.product_sitemap_images('/operations/'), [])

    def test_mismatched_video_poster_fails_and_unknown_clips_are_not_invented(self):
        body = '<main><video poster="/wrong.jpg"><source src="/assets/feldspar/feldspar-footage.mp4"></video></main>'
        with self.assertRaises(ValueError): media_seo.video_schemas(site.BASE_URL, '/', media_seo.PageMedia(body))
        body = '<main><video><source src="/assets/jcb.mp4"></video></main>'
        self.assertEqual(media_seo.video_schemas(site.BASE_URL, '/', media_seo.PageMedia(body)), [])


if __name__ == '__main__': unittest.main()
