# Pebble page — local approval preview

This folder is intentionally separate from the generated production site. It is
not linked from the live portfolio or sitemap. The production builder uses an
explicit directory allowlist and does not include `previews/`. The user approved
a local Git commit after the preview handoff. Publication, additional product
registration, inquiry submission and GA4 changes remain outside this approval.

## Scope

- One carousel with 31 pebble selections, not 31 product pages or an image grid.
- Manual previous/next, grouped native selector, keyboard arrows/Home/End, touch
  swipe, live announcement, and reduced-motion handling. No autoplay.
- Sizes, appearance labels, and packing references only. No supplier identity,
  contact details, prices, minimum orders, payment terms, tax, delivery promises,
  or original catalogue download.
- B-grade identity is retained. Finishes not explicitly established by the
  source are marked for confirmation. Photos do not certify sizing or grade.
- No unrelated chips, shell, sand, resin, cat litter, grinding media or boulders.
- Enquiry action opens a contextual email draft; it never sends a message.
- No analytics or reCAPTCHA loads. `noindex,nofollow,noarchive` on the draft.

## Local use

Serve this folder on the existing preview origin (port 4173), then open
`http://127.0.0.1:4173/`. Do not change ports or use another browser
to work around any saved browser denial. A user-facing preview handoff does not
prove an automated mobile/rendering check passed.

The generated `index.html`, `base.css` and `media/` are local preview outputs.
`build_preview.py` reads the supplied PDF and generates only this folder. The four
clean image inputs are retained for rebuilding; branded originals are not copied
into the page's media directory. All images are exported without source metadata.

On user approval, the four branded originals were cropped directly, with no
generative reconstruction. Source crop rectangles (left, top, right, bottom) are:
pink `(65, 0, 527, 465)`, dark green `(0, 0, 640, 425)`, natural black
`(0, 0, 450, 298)`, yellow tumbled `(0, 0, 350, 214)`. Clean PNG inputs retain
the remaining source pixels exactly; lossless WebP media retains those pixels.
The image editor's generated alternatives are not used by this page.

Run offline interaction checks with `node --test previews/pebbles/pebbles.test.cjs`.
Real browser rendering and touch-device verification must be reported separately.

## Verification — 20 October 2026

- Seven offline interaction contracts passed, covering all 31 selections,
  wrapping, contextual size/email updates, keyboard and swipe logic.
- JavaScript syntax, local image/style references, fragment targets, unique IDs,
  one H1, one product-photo element and draft `noindex` were checked.
- All 31 final photos were visually inspected in diagnostic contact sheets.
  Supplier lettering is absent in the selected/exported photos. All four cropped
  WebP assets match the retained original pixels exactly. No EXIF, XMP or source
  ICC metadata is retained (WebP decoder loop/background fields are format data).
- The page's HTML contains no supplier names, contact identifiers, rates or
  commercial terms. No original catalogue PDF is linked or served from this folder.
- All 11 production products remain unchanged; `previews/` is outside the build
  allowlist. The page returns HTTP 200 on the existing local preview origin.
- Rendered desktop/mobile checks have **not** been performed: the previous saved
  localhost browser denial was not retried or bypassed. The user-facing panel
  open request returned queued; use the preview URL directly if needed.
- At the initial preview handoff, nothing had been staged, committed, pushed or
  published. The subsequent approval is for a local commit of this folder only;
  no push or publication is included.

## Subsequent production approval

The user subsequently approved integrating and deploying Pebbles on the website.
The production page is now generated separately at `/products/pebbles/`; see
`docs/pebbles-release.md`. This original preview remains an excluded approval
snapshot, not the source of the published route or part of the Pages artifact.
