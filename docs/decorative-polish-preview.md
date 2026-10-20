# Decorative polish — local review, 20 October 2026

Visual thesis: retain the limestone/jade material-led design, with a stable photo
frame, readable practical information and one clear on-site enquiry journey.
Content plan: product and selection, applications/optional notes, then a compact
sample/quote form with the chosen catalogue details and email fallback.
Interaction thesis: retain manual carousel transitions; focus and scroll to the
enquiry heading from the CTA; retain native notes disclosure. Respect reduced
motion; no autoplay, extra hero animation or decorative motion is added.

## Scope

Pebbles, Glass Chips, Grout Sand and Colour-Coated Silica Sand only. Keep all 11
core products, 15 catalogue products, 39 sitemap pages, 45 photo sitemap entries,
25 grout colours and all 16 coated-sand applications. No new page/SEO expansion,
supplier branding, prices, project evidence, lab reports or unsupported claims.

- Primary decorative and header actions lead to the on-page sample enquiry,
  rather than opening a mail client or sending the buyer back to the homepage.
- The compact form reuses the existing JSON inquiry endpoint, CAPTCHA,
  honeypot, validation, duplicate-submit prevention and explicit success handling.
  Name and email are required; request type, company, destination, quantity,
  application and optional notes complete the brief. No free-sample promise.
- Original carousels still synchronize their email fallback. The separate form
  bridge uses only valid catalogue selections; photos, grades and all 25 grout
  colours update the form summary. Buyer notes are preserved and combined into
  the existing `notes` payload before submission, including on keyboard submit.
- Email fallback remains available with and without JavaScript. Real forms now
  legitimately require reCAPTCHA on these pages; this supersedes the earlier
  mailto-only loading optimization. No CAPTCHA/account/Google settings changed.
- Confirmed-form analytics now allow the four fixed decorative product labels,
  in addition to the 11 core labels. Personal/free-text fields never enter lead
  analytics; email drafts, selection changes and unconfirmed/failed submissions
  still emit no `generate_lead`. No analytics-property configuration is changed.
- Supporting captions, notes, swatch labels and form controls use larger text.
  The form stacks at 760px; gallery, swatch and application layouts retain their
  responsive stacking and 44px+ carousel/choice touch targets.
- Photos remain byte-for-byte unchanged. Consistent 4:3 frames and `contain`
  fitting preserve the complete crop without stretching, zooming or AI retouching.
  Different original framing/quality cannot be made identical without new photos.

## Verification boundary

Use offline Python/JavaScript tests and a clean release-shaped source snapshot.
Exercise every listed selection/grade, all grout colours, stale/invalid values,
latest-note capture, keyboard CTA focus, reduced motion, reset/retry behavior,
CAPTCHA requirements, fixed analytics labels and failure privacy.

Completed clean-snapshot verification: 63 Python and 72 JavaScript tests passed.
The production artifact verifier passed for 39 active pages and 27 technical
documents. All 45 original photo SHA-256 hashes match HEAD, and the sitemap is
unchanged. No private configuration, reporting output, CRM or preview directory
is included in the artifact. Whitespace checks passed. At that preview stage the
main Git index was unchanged and HEAD was `679fd2d`; the release-shaped snapshot
used a separate temporary index, not a commit.

Saved localhost browser denial remains respected: no browser retries, alternate
ports, remote rendering or PageSpeed workaround. Source/interaction tests do not
prove rendered mobile layout or Core Web Vitals. No real enquiry was sent; an
end-to-end delivery test still requires a user-completed CAPTCHA and confirmation.

Initially prepared as an uncommitted preview. The user subsequently requested
Marble Chips deployment on 20 October; that product uses this shared polish and
enquiry flow, so these changes are included with the Bentonite/Marble release.
Review locally at `/products/grout-sand/`, `/products/glass-chips/`,
`/products/colour-coated-silica-sand/` and `/products/pebbles/` on the existing
127.0.0.1:4173 server. No schedules or unrelated workspace changes are modified.
