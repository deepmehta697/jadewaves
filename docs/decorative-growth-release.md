# Decorative buyer guidance and measurement — 20 October 2026

## Website scope

Glass Chips, Grout Sand and Colour-Coated Silica Sand gain three concise buyer
questions each, inside their existing single, collapsed notes panel. Guidance
covers sample approval, grade selection, application/binder requirements and
enquiry details. Only catalogue facts and cautious buying guidance are used;
there are no invented projects, lab results, certifications or performance claims.
Pebbles retains its existing buying checklist.

The approved layout, original photos, single-photo carousels, all 25 grout
colours, 16 coated applications and separate industrial Silica Sand page remain.
The catalogue still has 11 core products and four decorative products. The
sitemap remains 39 canonical pages and 45 original carousel-photo entries.

## Loading change, not a measured speed claim

The four decorative pages open contextual email drafts; they do not submit the
protected enquiry form. They now omit the unused reCAPTCHA script. All 11 core
product submission forms and the homepage retain CAPTCHA. If a decorative page
gains a real `data-inquiry-form`, its CAPTCHA script is retained automatically.
No Google account settings, CAPTCHA configuration or form submission behavior
are changed. Analytics remains present; email drafts still do not emit confirmed
`generate_lead` events.

The first visible photo on the three newer decorative pages has intrinsic
dimensions, eager loading and high fetch priority. No preload of every carousel
image is introduced. This follows [Google's fetch-priority guidance](https://web.dev/articles/fetch-priority),
but is not evidence of an improved LCP, INP, CLS or mobile speed score.

Rendered mobile QA remains unverified because of the saved browser restriction.
Source, interaction tests and HTTP checks do not replace rendering or field data.
No alternate browser/port, remote rendering or PageSpeed workaround is used.

## Repeatable, manual baseline

`scripts/seo/decorative_baseline.py` uses existing reporting credentials and only
the official read-only Search Console and Analytics APIs. It does not submit
URLs/sitemaps, change analytics settings, send inquiries or create schedules.
Use a Python environment with `google-auth` and `requests` and the existing
private local configuration or environment-variable credential path:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/seo/decorative_baseline.py --as-of 2026-10-20
```

Raw output defaults to ignored `tmp/seo-decorative-baseline/YYYY-MM-DD.json`.
Do not commit that output, credentials, tokens or private query-level data.
The helper is protected against accidentally querying the older GA4 property.

- Last 28 completed dates, finalized GSC web-search data, Pacific-time dates.
- Exact four canonical product URLs, all-market and excluding-India views kept
  separate; no country filter is silently presented as worldwide performance.
- Page/query clicks, impressions and positions; sitewide query context is
  explicitly separate from new-page performance. Top-row/privacy limits apply.
- Four stored URL Inspection snapshots, not fresh live crawl tests or indexing
  submissions. A GSC failure stops the GSC batch without retrying.
- Organic landing sessions/users for the exact pages and production hostname
  in active GA4 property 527330659; not confirmed inquiry attribution.
- Missing rows are not a ranking of zero, proof of zero demand, or a causal
  ranking improvement. Newest finalized dates can remain delayed.

Read-only API semantics: [Search Analytics](https://developers.google.com/webmaster-tools/v1/searchanalytics/query),
[URL Inspection](https://developers.google.com/webmaster-tools/v1/urlInspection.index/inspect),
[GA4 reporting schema](https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema).

## Verification

Regression coverage checks the compact buyer panels, first-photo priority,
CAPTCHA removal only on email-draft pages, CAPTCHA retention on real forms,
exact measurement filters/windows, missing-row semantics, official read-only
endpoints and stopping on quota errors. Existing carousel, analytics, metadata,
source-evidence and sitemap tests remain required.

Exact-staged clean validation passed: 58 Python tests, 53 JavaScript tests, and
the production verifier for 39 active pages and 27 technical documents. The
artifact includes all 45 sitemap photos, with no private configuration, reporting
output, CRM source or preview directories. No photo bytes were changed.

Industry-channel research and any draft outreach remain local planning work,
not published website copy, sent messages, paid memberships or earned links.
No new schedule is created; existing review arrangements are unchanged.
