# Decorative product SEO — 20 October 2026

Scope: Glass Chips, Grout Sand and Colour-Coated Silica Sand, plus image discovery
for the recently published Pebbles carousel. Preserve the approved layout,
original photos, all 25 grout colours, 16 coated applications, 11 core products,
15-product catalogue and 39-page sitemap. No new blog/doorway/colour-variant URLs.

## Audit and implementation

- Existing HTTP routes, self canonicals, index/follow, product breadcrumbs and
  homepage/Materials discovery were already present; these are not claimed as
  newly fixed defects. Robots permit the product routes and public photo assets.
- Titles now state specific supplier intent. Descriptions include actual colour,
  finish and size information with a sample request, not keyword repetition.
  Short, visible copy establishes supply from India without claiming to be the
  manufacturer. Grout filler remains explicitly not ready-to-use grout.
- Reciprocal HTML links connect the three product pages and Pebbles. Industrial
  Silica Sand remains distinct and unchanged, with its existing quiet cross-link.
- Product schema lists the real carousel image URLs and visible size values;
  coated colours match the actual six options. No fabricated price, offers,
  reviews, ratings, manufacturer identity, safety or certification claims.
- Existing sitemap gains the image namespace and 45 product-photo entries:
  Pebbles 31, coated sand 6, glass 6, grout 2. Flat chart swatches are not promoted
  as product photos. This exposes images reached through manual carousel actions
  without adding an image grid. No deprecated image-caption/title tags are used.
- The same 39 canonical page URLs and persisted modification dates remain.
  No change to global tracking, form submission semantics, Google account access,
  scheduled reviews, robots rules or unrelated dirty configuration/report files.

## Search Console baseline

At 08:18:43 UTC on 20 October, four official read-only URL Inspection requests
using existing reporting credentials returned “URL is unknown to Google” for
Glass Chips, Grout Sand, coated sand and Pebbles; no crawl or canonical snapshot
was available. This is Google's stored index status, not a deployed noindex or
robots defect. The inspected public pages independently allow indexing.

The sitemap read reported last submission `2026-10-13T07:24:20.046Z`, last download
`2026-10-13T07:24:20.666Z`, 35 submitted web URLs, zero warnings/errors. Its reported
indexed count is not used as a sitewide indexing total. Raw local proof is in
ignored `tmp/seo-new-products-20261020/before.json`; no credential or token saved.

## Verification boundaries

The release uses a clean exact-staged checkout, preserving unrelated local edits.
Source/build/HTTP tests are not rendered browser or Core Web Vitals measurement;
the saved localhost denial is not retried or bypassed. Search Console is accessed
only through its official API and the permitted signed-in browser interface.
Sitemap acceptance and individual priority-crawl requests are not indexing or
ranking guarantees. Stop a request batch on a temporary Google error or quota
message, without repeated requests or CAPTCHA/permission workarounds.

Pre-deployment validation passed in the exact staged checkout: 47 Python tests,
53 JavaScript tests, the production verifier for 39 pages / 27 technical documents,
and whitespace checks. Image sitemap assertions cover all 45 original carousel
photos and their local paths/robots allowance. No photo, carousel behavior,
swatch, global tracking script or technical document was edited.

## Official references

- [Google title-link guidance](https://developers.google.com/search/docs/appearance/title-link)
- [Google snippet guidance](https://developers.google.com/search/docs/appearance/snippet)
- [Image sitemaps, including JavaScript-discovered images](https://developers.google.com/search/docs/crawling-indexing/sitemaps/image-sitemaps)
- [Product snippet eligibility](https://developers.google.com/search/docs/appearance/structured-data/product-snippet)
- [Official sitemap submission API](https://developers.google.com/webmaster-tools/v1/sitemaps/submit)
