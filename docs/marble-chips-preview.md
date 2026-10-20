# Marble Chips — local preview, 20 October 2026

Initially prepared as an uncommitted addition to the Decorative Range, built on
the polished single-photo carousel and on-page enquiry pattern. The user then
requested deployment on 20 October, together with Bentonite media changes;
see `bentonite-media-release.md`. No indexing submission, account setting change
or external enquiry is part of the release.

## Design

Visual thesis: quiet, material-led presentation with one original photograph and
clear colour/grade choices; retain the limestone/jade palette and type system.
Content plan: product heading and brief, one carousel with two native selectors,
two application rows, one collapsed notes panel, then the compact enquiry form.
Interaction thesis: retain manual photo transitions, touch/keyboard navigation,
native disclosure and CTA focus/scroll. Respect reduced motion; no autoplay,
image grid, extra hero, new cards or decorative motion.

## Evidence and exclusions

The supplier PDF has 16 pages. Twelve selections explicitly identify marble:
White, Red, Rojo pink, Pink wood, Green, Grey, Mocha, Brown, Black, Panther,
Ivory cream and Mixed marble. Their five listed grades are 0.5–1.5 mm, 1–3 mm,
3–6 mm, 6–9 mm and 9–12 mm. Catalogue names are colour/blend references, not
verified geological classifications, calibrated colour standards or sieve reports.

The separate Quartz Chips and Mix Gravels entries are not put on a Marble Chips
page or relabeled as marble. No new quartz/gravel page is added by inference.
The catalogue's MOQ is not evidence of bag packing: no bag weight is invented.
Supplier identity, location, phone, website, prices, MOQ, cover and contact pages
are omitted. The source PDF is not copied into public assets or linked for download.

All twelve embedded product images were visually inspected and have no supplier
marks within the photo. Only the surrounding PDF contains supplier/price text.
The original full RGB pixels are preserved exactly in metadata-free lossless
WebP files; no AI editing, colour correction, zooming, retouching or unnecessary
cropping is used. The full photo remains visible within the established frame.
Private source mapping and pixel/asset hashes remain in ignored
`tmp/pdfs/marble-chips/photo-provenance.json`, not in public catalogue metadata.

Application rows describe possible cement/epoxy terrazzo and precast terrazzo
uses, not tested performance or conformity of this supplier's grades. General
context is supported by the [NTMA terrazzo description](https://ntma.com/) and
[precast terrazzo guidance](https://ntma.com/wp-content/uploads/2024/11/Guide-Specifications-for-Precast-Terrazzo-Stairs-6-11-24-FINAL.pdf).
Physical sample, grading and binder suitability still require confirmation.
No certification, chemistry, strength, safety or manufacturer claim is added.

## Integration and checks

- The 11 core products remain; the full catalogue now has 16 products, including
  five decorative products. The Materials directory and homepage link to Marble
  Chips. Related links connect it with glass, coated sand and grout sand.
- The new canonical route is `/products/marble-chips/`. Local sitemap output has
  40 pages and 57 original photo entries, including the 12 new marble photos.
  Existing page dates and photos are preserved. No sitemap is submitted externally.
- The selected colour/blend and one of five grades reach the existing protected
  enquiry handler and contextual email fallback. CAPTCHA is retained. Only a
  server-confirmed form may emit a lead with the fixed `Marble Chips` label;
  browsing, opening email and failed submissions are not leads.
- Production builds use only clean public assets and stdlib templates; the
  supplier PDF, private preparation scripts, Pillow and pypdf are not dependencies.

Browser rendering remains unverified under the saved localhost denial; no retry,
alternate port, remote rendering or other workaround is used. Photo inspection,
offline interaction tests and production-source checks do not establish rendered
mobile quality or Core Web Vitals. No real inquiry was submitted.

Completed clean-snapshot validation: 68 Python tests and 81 JavaScript tests
passed, including all 60 marble colour/grade combinations. The production
verifier passed for 40 active pages and 27 linked technical documents. All 12
new photo hashes match their inspected extraction record, and all 45 existing
photo hashes still match HEAD. The artifact excludes the supplier PDF, private
configuration/reporting sources, CRM and previews. Whitespace checks passed.
At that preview stage the real Git index was untouched and HEAD was `679fd2d`.

Preview on the existing local server: `http://127.0.0.1:4173/products/marble-chips/`.
The prior uncommitted polish and unrelated workspace changes are preserved.
