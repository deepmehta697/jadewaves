# Product and media SEO — 20 October 2026

## Release scope

- Retain 11 core products, five decorative products and 40 canonical routes.
  No new thin watch pages, location pages, fabricated prices, reviews or ratings.
- Extend the existing image sitemap from 57 decorative photographs to 68
  product photographs, including each current core-product hero and the updated
  Bentonite image. Swatches, private PDFs, source videos and previews stay out.
- Use actual product/article photos for consistent Open Graph and Twitter-card
  previews, with descriptive alt text. Articles use `og:type=article`; publisher
  logo identity is not overwritten by a product photo.
- Improve Pebbles' supplier/India title and description and include all 31
  approved carousel photographs in its Product schema. Existing internal links,
  five decorative carousels, 25 grout colours and 16 coated applications remain.
- Add VideoObject metadata only for the four newly published clips with verified
  first-publication evidence, matching the video and poster actually embedded
  on the page. Quartz footage stays exclusive to Quartz; Feldspar and Bentonite
  retain their own clips; the packed-bags clip is on the homepage.

Video dates describe publication of these encodes on this website, not recording
dates. They are fixed to the completed Pages releases, not file metadata or the
build clock: Bentonite run 39403517318 at 09:50:24 UTC; Quartz/Feldspar run
39406564517 at 10:15:24 UTC; packed bags run 39408379119 at 10:30:40 UTC.
Durations come from the MP4 movie headers. Stable content URLs and the same
posters used by the HTML video players are supplied. No fake player endpoint,
view count, transcript, certification or material-performance assertion is added.

The older cargo-preparation/Operations clips remain native, crawlable HTML
videos, but do not receive an invented first-publication date. Their provenance
does not establish that date. Homepage/product clips are supporting content,
not dedicated watch pages: this release does not claim video-result eligibility.
No video sitemap is added just to imply otherwise. Manual, muted playback and
`preload="none"` remain; no script click is needed to create the video sources.

Original article publication/modification dates remain. Existing same-day page
lastmod records are retained; shared social tags do not reset article history.
Visual layout, image pixels, PDFs, consent/CAPTCHA and confirmed-lead tracking
are unchanged. Metadata is not a ranking guarantee or a measured speed gain.

## Validation and release boundaries

Offline regression checks cover image sitemap identities, all 16 product share
images, article previews, visible-video/schema correspondence, MP4 durations,
stable release dates, robot access, and protection against cross-product footage.
The normal full Python/JavaScript suites and production verifier are required
before publication. The clean release must exclude private reporting output,
credentials, local preview/media-processing files, CRM and unrelated dirty edits.
The exact-staged clean release passed 94 Python and 81 JavaScript tests, the
production verifier for 40 routes and 26 linked documents, and whitespace checks.

Live checks must confirm all 40 canonical routes, 68 image entries and public
media/thumbnail URLs, plus the deployed structured data. A sitemap submission is
discovery, not proof of indexing. Any individual crawl request must use the
permitted Search Console UI, once per target, and stop on quota/temporary error.

Saved localhost browser denial remains respected. Source/HTTP checks and offline
tests do not constitute rendered mobile checks, measured Core Web Vitals or an
official Google rich-results validation. No schedule, outreach, inquiry, Google
permission or analytics-setting change is included.

## References

- [Google image sitemap guidance](https://developers.google.com/search/docs/crawling-indexing/sitemaps/image-sitemaps)
- [Google VideoObject fields](https://developers.google.com/search/docs/appearance/structured-data/video)
- [Google video discovery and watch-page requirements](https://developers.google.com/search/docs/appearance/video)

Private index snapshots and post-release acceptance evidence belong in ignored
`tmp/seo-media-20261020`, not this public-source release.
