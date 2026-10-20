# Pebble product release — 20 October 2026

The user approved integrating and deploying the previously approved local preview.
The production route is `/products/pebbles/`, with discovery links on the homepage
and Materials page, a dedicated Decorative Stone family, and a sitemap entry.
The existing eleven core mineral products and fifteen buyer guides are retained;
the full catalogue now has twelve products and thirty-six active routes.

The page preserves the approved single-photo carousel with thirty-one selections,
contextual sizes, an optional comparison table, and an email-draft enquiry action.
It uses shared site navigation, footer, metadata and existing page-view measurement.
Opening an email draft is not counted as a confirmed `generate_lead` submission.

Supplier identity, rates, minimum orders, legal/payment terms and the original
catalogue download are absent. Approved original-photo crops are copied unchanged;
the generated image alternatives are not used. No price, review, certification,
manufacturer identity or shipment guarantee was invented. Unspecified finishes
remain subject to confirmation. The page's Product metadata has no fabricated offer.

Production builds use checked-in clean WebP media and JSON dimensions, not a local
supplier PDF, Pillow, the Downloads folder, or `previews/`. The preview remains an
excluded historical approval snapshot. Its commit `66243ac` alone did not publish
the page; this integration makes the new route part of the existing Pages build.

Verification includes source/build contracts, carousel interaction contracts,
the production-artifact verifier and post-deployment HTTP/content checks.
Rendered mobile/browser review remains limited by the previously saved localhost
denial; it has not been retried or bypassed. No Google settings, additional inquiry,
new schedule, unrelated report/configuration, or invoice files are part of release.

The exact staged release was checked in a clean temporary checkout before push:
production regeneration/build and the 36-route/27-document verifier passed,
alongside 18 Python and 28 JavaScript tests and carousel syntax validation.
All 31 release photos match the approved preview byte-for-byte. The preview,
source templates, supplier PDF and unrelated untracked assets were absent from
the clean production artifact. This is source/build evidence, not rendered QA.
