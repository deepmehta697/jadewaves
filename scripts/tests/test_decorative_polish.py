"""The local decorative polish preserves products, photos and form protections."""
from html.parser import HTMLParser
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


class DecorativePolishTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.slugs = ('pebbles', 'glass-chips', 'grout-sand', 'colour-coated-silica-sand', 'marble-chips')
        cls.pages = {slug: site.render_product_page(site.CATALOGUE_BY_SLUG[slug]) for slug in cls.slugs}

    def test_one_compact_protected_form_per_page_with_real_default_context(self):
        for slug, html in self.pages.items():
            with self.subTest(slug=slug):
                tags = Tags(html).tags
                self.assertEqual(len([a for t, a in tags if t == 'form']), 1)
                form = next(a for t, a in tags if t == 'form')
                self.assertIn('data-inquiry-form', form)
                self.assertIn('data-decorative-form', form)
                self.assertEqual(form['data-inquiry-endpoint'], site.INQUIRY_ENDPOINT)
                self.assertEqual(form['data-recaptcha-configured'], str(bool(site.RECAPTCHA_SITE_KEY)).lower())
                fields = {a['name']: a for t, a in tags if t in ('input', 'select', 'textarea') and 'name' in a}
                self.assertEqual(fields['product']['value'], site.CATALOGUE_BY_SLUG[slug]['name'])
                self.assertTrue(fields['notes']['value'])
                self.assertEqual(fields['company_website']['value'], '')
                self.assertIn('required', fields['name']); self.assertIn('required', fields['email'])
                self.assertEqual(fields['email']['type'], 'email')
                self.assertEqual(len([a for t, a in tags if a.get('id') == 'contact']), 1)
                submit = next(a for t, a in tags if t == 'button' and a.get('type') == 'submit')
                self.assertIn('disabled', submit)
                self.assertIn('google.com/recaptcha/api.js', html)
                self.assertIn('Prefer email?', html)

    def test_primary_product_ctas_point_to_onsite_form_not_email(self):
        for html in self.pages.values():
            tags = Tags(html).tags
            primary = [a for t, a in tags if t == 'a' and ('data-decorative-enquire' in a or 'data-selection-link' in a)]
            self.assertTrue(primary)
            self.assertTrue(all(a['href'].endswith('/#contact') and not a['href'].startswith('mailto:') for a in primary))
            ids = [a['id'] for t, a in tags if 'id' in a]
            self.assertEqual(len(ids), len(set(ids)))
            header = html.split('<header', 1)[1].split('</header>', 1)[0]
            self.assertNotIn('Request a specification', header)
            self.assertIn('Request a sample', header)
            self.assertNotIn('href="./#contact"', header)

    def test_selection_script_runs_after_the_page_carousel(self):
        scripts = {'pebbles': 'assets/pebbles/pebbles.js', 'glass-chips': 'assets/decorative-products/carousel.js', 'marble-chips': 'assets/decorative-products/carousel.js',
                   'grout-sand': 'assets/decorative-products/carousel.js', 'colour-coated-silica-sand': 'assets/colour-coated-sand/coated-sand.js'}
        for slug, html in self.pages.items():
            self.assertLess(html.index(scripts[slug]), html.index('assets/decorative-products/enquiry.js'))
            self.assertIn('assets/decorative-products/enquiry.css', html)
            self.assertIn('data-decorative-message', html)
            self.assertNotRegex(html, r'<textarea[^>]*data-decorative-message[^>]*name=')

    def test_images_are_contained_in_stable_frames_not_recropped(self):
        for path, selector in [('assets/pebbles/pebbles.css', '.pebble-photo'), ('assets/colour-coated-sand/coated-sand.css', '.coated-sand-photo')]:
            css = (ROOT / path).read_text()
            rule = re.search(re.escape(selector) + r' \{([^}]+)\}', css).group(1)
            self.assertIn('aspect-ratio: 4 / 3', rule)
            image = re.search(re.escape(selector) + r' img \{([^}]+)\}', css).group(1)
            self.assertIn('object-fit: contain', image)
            self.assertNotIn('object-fit: cover', image)

    def test_published_analytics_script_matches_template_and_only_expands_fixed_labels(self):
        source = (ROOT / 'templates/material-ledger.js').read_text().strip()
        self.assertEqual((ROOT / 'script.js').read_text().strip(), source)
        for slug in self.slugs: self.assertIn('"' + site.CATALOGUE_BY_SLUG[slug]['name'] + '"', source)
        self.assertIn('result?.success !== true', source)
        self.assertIn('trackSuccessfulInquiry(data);', source)


if __name__ == '__main__': unittest.main()
