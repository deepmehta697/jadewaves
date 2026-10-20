# Decorative Range release — 20 October 2026

The user approved deploying the previewed separate-page architecture.

- New route: `/products/colour-coated-silica-sand/`.
- Materials family renamed **Decorative Range**, containing Pebbles and
  Colour-Coated Silica Sand; the old `#decorative-stone` fragment remains an alias.
- Homepage and Materials directory expose both decorative products.
- Industrial Silica Sand retains its chemistry, documents, guides and inquiry
  form, with only one quiet related-product link; no decorative carousel or images.
- Existing eleven core mineral products, Pebbles and fifteen buyer guides remain;
  the expanded catalogue has thirteen products and thirty-seven active routes.

The new page preserves the approved single-photo, six-colour carousel, concise
applications, grain size, email-draft enquiry and collapsed packing/grade notes.
The six approved original photos are copied without alteration. No supplier marks,
rates, original supplier PDF, minimum-order/legal terms, invented coating test,
price, review, certification, manufacturer identity or guarantee is introduced.
Industrial COA/TDS references are explicitly not treated as coating certification.
Opening an email draft is not a confirmed `generate_lead` submission.

Builds use checked-in clean image files and JSON dimensions. They require neither
the supplier PDF nor Pillow/pypdf, and do not publish any preview/source folder.
The production page retains the existing root/project-host-aware base behavior;
it does not use the preview-only static base or resource rewriting. Sitemap dates
change only for the newly published page and the industrial page's related link;
article dates and unchanged core-product dates are retained.

Verification covers generator/build contracts, carousel keyboard/selection/swipe
logic, metadata, links, structured data, local image paths, disabled false lead
emission, existing inquiry regressions and the full production-artifact verifier.
Rendered browser/mobile QA remains unverified because the saved localhost browser
denial has not changed; no retry or rendering workaround was used. Unrelated
working-tree configuration/report edits, invoices and other assets are excluded.

Pre-deployment validation of the exact staged checkout passed: 27 Python tests,
36 JavaScript tests, JavaScript syntax check, and the production verifier covering
37 active pages and 27 linked technical documents. All six image hashes match
the approved originals. The clean production artifact excludes preview/source
folders, unrelated untracked assets and the original supplier PDF.
