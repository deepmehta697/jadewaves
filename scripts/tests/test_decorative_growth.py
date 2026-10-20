"""Offline contracts for buyer guidance, loading and read-only measurement."""
from datetime import date
from html.parser import HTMLParser
import importlib.util
import json
from pathlib import Path
import re
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
import generate_site as site

spec = importlib.util.spec_from_file_location('decorative_baseline', ROOT / 'scripts/seo/decorative_baseline.py')
baseline = importlib.util.module_from_spec(spec)
spec.loader.exec_module(baseline)


class Tags(HTMLParser):
    def __init__(self, html):
        super().__init__(); self.tags = []; self.feed(html)
    def handle_starttag(self, tag, attrs): self.tags.append((tag, dict(attrs)))


class FakeResponse:
    def __init__(self, status=200, data=None): self.status_code, self.data = status, data or {}
    def json(self): return self.data


class FakeSession:
    def __init__(self, status=200): self.calls, self.status = [], status
    def post(self, endpoint, **kwargs):
        self.calls.append((endpoint, kwargs))
        return FakeResponse(self.status)


class DecorativeGrowthTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pages = {slug: site.render_product_page(site.CATALOGUE_BY_SLUG[slug]) for slug in baseline.SLUGS}

    def test_three_buyer_guides_stay_inside_one_collapsed_notes_element(self):
        data = json.loads((ROOT / 'templates/decorative-buyer-questions.json').read_text())
        self.assertEqual(set(data), set(baseline.SLUGS) - {'pebbles'})
        for slug, questions in data.items():
            html = self.pages[slug]
            details = re.findall(r'<details\b.*?</details>', html, re.S)
            self.assertEqual(len(details), 1)
            self.assertNotIn('open', next(a for t, a in Tags(html).tags if t == 'details'))
            self.assertEqual(len(questions), 3)
            self.assertIn('Before you order', details[0])
            for question in questions: self.assertIn(question['question'], details[0])

    def test_only_first_carousel_photo_gets_high_priority_and_dimensions(self):
        for slug in set(baseline.SLUGS) - {'pebbles'}:
            photos = [a for t, a in Tags(self.pages[slug]).tags if 'data-product-photo' in a or 'data-sand-photo' in a]
            self.assertEqual(len(photos), 1)
            self.assertEqual(photos[0]['fetchpriority'], 'high')
            self.assertEqual(photos[0]['loading'], 'eager')
            self.assertGreater(int(photos[0]['width']), 0)
            self.assertGreater(int(photos[0]['height']), 0)

    def test_email_draft_pages_do_not_load_form_captcha(self):
        for html in self.pages.values():
            self.assertNotIn('data-inquiry-form', html)
            self.assertNotIn('google.com/recaptcha/api.js', html)
            self.assertIn(site.GA4_MEASUREMENT_ID, html)

    def test_all_core_forms_and_home_keep_captcha(self):
        for html in [site.render_homepage()] + [site.render_product_page(p) for p in site.PRODUCTS]:
            self.assertIn('data-inquiry-form', html)
            self.assertIn('google.com/recaptcha/api.js', html)

    def test_future_decorative_submission_form_keeps_captcha(self):
        html = site.page_shell('Test', 'Test', '/products/grout-sand/', '<form data-inquiry-form></form>', [])
        self.assertIn('google.com/recaptcha/api.js', html)

    def test_measurement_uses_previous_28_completed_dates(self):
        self.assertEqual(baseline.reporting_window(date(2026, 10, 20)), ('2026-09-22', '2026-10-19'))
        self.assertEqual(baseline.reporting_window(date(2026, 1, 1)), ('2025-12-04', '2025-12-31'))

    def test_gsc_filters_exact_new_pages_not_similar_paths(self):
        body = baseline.search_request('2026-09-22', '2026-10-19', ['page', 'query'])
        regex = body['dimensionFilterGroups'][0]['filters'][0]['expression']
        for url in baseline.URLS:
            self.assertRegex(url, regex)
            self.assertIsNone(re.search(regex, url + 'other/'))
            self.assertIsNone(re.search(regex, url.replace('.com', 'Xcom')))
        self.assertEqual(body['dataState'], 'final')
        self.assertEqual(body['type'], 'web')
        export = baseline.search_request('a', 'b', ['page'], export_only=True)
        self.assertEqual(export['dimensionFilterGroups'][0]['filters'][1], {'dimension': 'country', 'operator': 'notEquals', 'expression': 'ind'})
        self.assertNotIn('dimensionFilterGroups', baseline.search_request('a', 'b', ['query'], targeted=False))

    def test_ga4_filters_host_pages_and_organic_without_false_lead_metrics(self):
        body = baseline.landing_request('a', 'b')
        self.assertEqual([m['name'] for m in body['metrics']], ['sessions', 'totalUsers'])
        filters = {e['filter']['fieldName']: e['filter'] for e in body['dimensionFilter']['andGroup']['expressions']}
        self.assertEqual(filters['hostName']['stringFilter']['value'], 'jadewavesenterprise.com')
        self.assertEqual(filters['landingPage']['inListFilter']['values'], list(baseline.PATHS))
        self.assertEqual(filters['sessionDefaultChannelGroup']['stringFilter']['value'], 'Organic Search')

    def test_missing_search_rows_never_become_rank_zero(self):
        rows = baseline.summarize_pages([])
        self.assertEqual(len(rows), 4)
        self.assertTrue(all(row['averagePosition'] is None and not row['hasReportedRow'] for row in rows))
        row = baseline.summarize_pages([{'keys': [baseline.URLS[0]], 'position': 12.5, 'clicks': 2, 'impressions': 9}])[0]
        self.assertEqual((row['averagePosition'], row['hasReportedRow']), (12.5, True))

    def test_collection_only_calls_official_read_only_reports_and_inspection(self):
        session = FakeSession()
        result = baseline.collect(session, baseline.BASE + '/', '527330659', date(2026, 10, 20))
        self.assertEqual(len(session.calls), 10)
        self.assertEqual(result['errors'], [])
        self.assertTrue(all(scope.endswith('.readonly') for scope in baseline.SCOPES))
        for endpoint, kwargs in session.calls:
            self.assertTrue(endpoint.endswith('/searchAnalytics/query') or endpoint.endswith('/urlInspection/index:inspect') or endpoint.endswith('/properties/527330659:runReport'))
            self.assertEqual(kwargs['timeout'], 30)
        with self.assertRaises(AssertionError): baseline.collect(session, baseline.BASE + '/', '484597151', date(2026, 10, 20))

    def test_quota_failure_stops_gsc_batch_without_retry(self):
        session = FakeSession(status=429)
        result = baseline.collect(session, baseline.BASE + '/', '527330659', date(2026, 10, 20))
        self.assertEqual(len(session.calls), 2)  # One GSC failure, one independent GA4 report.
        self.assertEqual(len(result['inspection']), 0)
        self.assertNotIn('pageSummary', result)
        self.assertEqual(result['errors'][0]['httpStatus'], 429)


if __name__ == '__main__': unittest.main()
