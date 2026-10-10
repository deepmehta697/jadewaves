# Material Ledger implementation verification

Implementation date: 10 October 2026.

## Implemented scope

The homepage, portfolio, all 11 product pages, seven buyer guides, company profile, CEO note, export markets, operations, and two policy pages use the shared Material Ledger system. The homepage includes the photographic masthead, proof ledger, three featured material families, complete directory, four-step supply process, evidence gallery, and procurement brief. Product pages include material photography, specification tables, application checks, technical documents, process, FAQs, and contextual inquiries.

The source lives in `templates/material_pages.py`, `material_layout.py`, `material_support.py`, `material-ledger.css`, and `material-ledger.js`, with data and generation managed by `generate_site.py`. Obsolete generated style and animation systems were replaced. Responsive WebP assets include intrinsic dimensions and thumbnail-specific source sizes. All source-set candidates follow the deployment base path.

## Verified

- `python3 scripts/build_site.py --regenerate` successfully assembles `_site`.
- `python3 scripts/verify_site.py --root _site` passes across all 27 active pages and 27 linked technical documents. It checks local links and anchors, canonical URLs, JSON-LD, product and article schema, single H1s, unique IDs, image dimensions and assets, inquiry fields/endpoints, production sitemap coverage, and removal of continuous decorative motion.
- JavaScript syntax and Python compilation pass. `git diff --check` passes.
- The interactions agent verified mocked navigation and form behaviour: menu focus trapping/inert restoration, Escape/resize closing, request prefill, native validity checks, CAPTCHA gates, sanitized JSON fields, explicit success confirmation, and failure messages. No live inquiry was sent.
- Source checks cover reduced-motion styles, visible focus states, labels, no-JavaScript navigation/direct-contact fallbacks, and disabled submission until its JSON handler is ready.
- A 65% dark hero overlay provides at least 4.5:1 contrast for body text even over a white source image; other image crops still require visual review.

## Remaining acceptance gate

Desktop and 360px browser visual review remains unverified. The browser tool rejected access to `http://127.0.0.1:4173/` because permission was denied. No alternate browser, port, remote preview, or browser automation workaround was attempted. This leaves actual line wrapping, focal crops, viewport fit, touch/keyboard interaction, and measured browser performance pending.

The user requested committing and pushing to `main`, explicitly retaining all 11 products. Publication proceeds with this browser review still pending; pushing does not complete that acceptance gate.

## Main-branch integration

The newer remote history is merged without rewriting it. Its public CRM inquiry endpoint and reCAPTCHA site key are retained as build defaults, while environment overrides still work. Existing SEO aliases, malformed-URL redirects, parameter-document aliases, crawl exclusions, and the regenerate-on-deploy workflow are retained. Product redirects now resolve against the complete 11-product portfolio. The production builder uses explicit site sections and generated alias roots, excluding CRM source, integrations, templates, and workspace previews.
