# SEO implementation — 13 October 2026

## Scope and release status

Three GPT-6.1 Sol agents at high reasoning implemented successful-inquiry measurement, search snippets and persisted article dates, and eight evidence-grounded product buyer guides. The parent integrated the changes and verified the production artifact. All 11 products remain active. The user subsequently authorized review, publication to `main`, and Google-property follow-up on 13 October 2026. The eight new guide records now contain that authorized release date; deployment verification is recorded separately after the push.

## Implemented changes

- `templates/material-ledger.js` emits `generate_lead` only after confirmed inquiry acceptance. Fixed-label parameters exclude personal/free-text data, query strings, fragments, and honeypot acknowledgements. Analytics failure cannot prevent a successful inquiry.
- `generate_site.py` retains distinct supplier-focused product titles and concise descriptions. Article publication/update dates are recorded editorial metadata, not the build clock. Existing publication dates have repository provenance; the new guides record their authorized first release. Unknown dates remain omitted. Sitemap modification dates reflect recorded changes.
- `templates/product_guides.py` adds guides for silica flour, bentonite, kaolin, talc, salt, fly ash, copper slag, and rubber granules. All 11 product pages link to supporting guides, and every guide links back to its product reference. The blog contains 15 guides, and the production sitemap contains 35 active pages.
- `scripts/verify_site.py` checks dates against persisted metadata, unique titles/descriptions, product-to-guide links, active routes, technical documents, and existing semantic/asset/SEO-redirect invariants.

Technical references are indicative, not shipment guarantees. No new claims about certifications, capacity, customers, delivery history, safety, or guaranteed grade performance were invented. See `product-guide-evidence.md` for content provenance and `analytics-tracking.md` for event semantics.

## Search Console and analytics baseline

Read-only API checks on 13 October 2026 used the existing configured Google property and credentials. Web-search totals for **15 September–12 October 2026**, across all countries: **8 clicks, 240 impressions, 3.33% CTR, and 21.77 average position**. Recent dates may be subject to normal reporting lag; average position is an aggregate, not the rank of a particular keyword. GA4 returned no rows for `generate_lead` or `submit_lead_form` in that period. That does not prove there were no business inquiries.

URL Inspection is a snapshot of Google's indexed version, not a live-page test. Current live HTTP checks found all 11 product pages returning 200, self-canonical, and `index,follow`.

| Product | Google URL Inspection snapshot | Last crawl in snapshot |
| --- | --- | --- |
| Silica sand | Submitted and indexed | 11 October 2026 |
| Quartz sand | Submitted and indexed | 7 October 2026 |
| Feldspar | Submitted and indexed | 20 September 2026 |
| Silica flour | Excluded by an older noindex tag | 4 August 2026 |
| Bentonite | Excluded by an older noindex tag | 2 July 2026 |
| Salt | Excluded by an older noindex tag | 2 July 2026 |
| Fly ash | Older 404 snapshot | 30 April 2026 |
| Copper slag | Crawled, currently not indexed | 27 April 2026 |
| Kaolin | URL unknown to Google | No crawl reported |
| Talc | Discovered, currently not indexed | No crawl reported |
| Rubber granules | Discovered, currently not indexed | No crawl reported |

The current sitemap was downloaded by Google on 12 October and reported zero warnings/errors. An older submitted `sitemap.website.xml` entry reports one error. Its removal is a separate Search Console administration action; it was not deleted. The API's sitemap `indexed` field is not used as the product-indexing count, since per-URL inspection gives the actual available snapshots.

API documentation: [URL Inspection](https://developers.google.com/webmaster-tools/v1/urlInspection.index/inspect), [Search Analytics](https://developers.google.com/webmaster-tools/v1/searchanalytics/query).

## Release and Google-property follow-up

1. Review and publish the source/generated artifact when authorized. Check the deployed 35-route sitemap, 11 product canonicals, article metadata, and shared script after deployment.
2. Record a new guide's `date_published` only when released. Keep its preparation/review `date_modified` unless its content actually changes. Do not reset dates on routine rebuilds.
3. In GA4, designate `generate_lead` as a key event and optionally register the fixed `product` and `request_type` parameters as event-scoped custom dimensions. Confirm delivery through an authorized test after publication; offline tests do not verify the Google ingestion pipeline.
4. Use Search Console to request recrawls of restored product pages and inspect the new guide URLs after publication. Do not use Google's Indexing API for ordinary product or blog pages. Inclusion is not guaranteed or instantaneous.
5. Review the obsolete submitted sitemap entry before removing it. Retain the valid `sitemap.xml` submission.

## Release access limitations

The guide copy was reviewed against the product records and reference-sheet sources without introducing shipment guarantees. The Google Analytics Admin API returned 403 `SERVICE_DISABLED` for the configured project, so no key-event configuration was changed. The user enabled an Always allow rule for the local site and restarted the desktop app, but Browser Use still reported a saved permission block. Browser-driven recrawl requests, live inquiry delivery tests, and mobile rendering/performance measurements therefore remain blocked; no alternate browser, port, raw browser interface, or remote-render workaround was used.

## Performance and redirects

Existing responsive WebP hero variants are retained. The homepage quarry image is approximately 24 KiB at 480px and 154 KiB at 1600px; these are file sizes, not LCP measurements. Actual mobile LCP, INP, and CLS remain unverified. Browser access was retried only after the user reported permission changes; each attempt was denied. No workaround was attempted.

Existing instant meta-refresh redirects, canonical destinations, and noindex aliases are preserved. They are supported permanent-redirect signals; HTTP 301/308 is preferable where hosting permits. This implementation does not migrate GitHub Pages hosting or change DNS just to support server-side redirects. [Google redirect guidance](https://developers.google.com/search/docs/crawling-indexing/301-redirects).

## Local verification

```sh
python3 scripts/build_site.py --regenerate
python3 scripts/verify_site.py --root _site
python3 -m unittest discover -s scripts/tests -p 'test_seo_metadata.py'
node --test scripts/tests/inquiry_analytics.test.cjs
node --check script.js
```

Use the Codex bundled Node runtime if `node` is not on PATH. Tests use mocked form/network/analytics surfaces and never send a live inquiry.
