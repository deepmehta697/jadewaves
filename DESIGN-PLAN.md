# Jade Waves Website Redesign Plan

## Decision

Replace the current soft, animated "supply-chain SaaS" treatment with **Material Ledger / Field-to-Port**: a precise, editorial industrial system that demonstrates how a mineral moves from specification to shipment.

The website should make a technical or procurement buyer feel that Jade Waves is methodical, physically close to the material, and dependable at export execution. It should not try to look like a logistics app.

### Visual thesis

**Tactile mineral evidence, organised with the calm of an export dossier.**

The visual anchor is real quarry, material, packing, inspection, and container imagery. The interface is a disciplined framework around that evidence: strong type, rules, small data labels, and very few elevated surfaces.

## What changes

| Retire | Introduce |
| --- | --- |
| Blue ambient gradients, glow, glass blur, floating route canvas, decorative maps/ships | Full-bleed real process or material photography with deliberate crops |
| Oversized rounded cards, pills, shadows, and repeated micro-labels | Hairline rules, a strict grid, small-radii evidence panels, product/spec tables |
| Three equal hero CTAs and generic trust chips | One primary CTA plus one quiet text link, with factual proof beside it |
| Animation as atmosphere (drift, sweep, pulse, parallax) | Short, once-only reveal for hierarchy; optional photo-crop shift on hover |
| Product pages that lead with abstract treatment | Product pages that lead with the actual material, grade, and a scannable specification summary |

## Design system

### Palette

- **Limestone** `#F3F0E8`: primary background; warm, uncoated paper rather than blue-white.
- **Chalk** `#FBFAF6`: raised/reading surface.
- **Iron** `#1F2523`: primary text and dark CTA.
- **Slate** `#56615D`: supporting copy and data labels.
- **Oxidized jade** `#0E5A50`: sparse operational signal, links, and active state.
- **Quartz sand** `#C6A472`: product/material accent only; never a second CTA color.
- **Safety orange** `#C65A28`: exception/warning state only, not decoration.

No blue gradient, glass effect, or ambient glow. Use colour as a signal, not a surface treatment.

### Typography

- Keep one neutral grotesk for navigation, body copy, forms, and technical data.
- Add one restrained editorial display face **only** for the H1 and large section statements. If adding a font is undesirable, use Instrument Sans at display sizes instead.
- Use a utilitarian mono style only for grade codes, dimensions, document dates, and dispatch labels.
- Reduce all-caps labels. They should identify a section or a datum, not accompany every heading.
- Target 16–18px body text; use a 60–68 character reading measure; allow large headings to wrap into intentional two-line statements.

### Layout and components

- Use an 8px spacing scale and a content width of about 72rem.
- Default to square to 8px corners. A larger corner must have an interaction reason.
- Use cards only for interactive modules or documents. Content should otherwise live in rows, columns, rules, and image bands.
- Primary CTA: one rectangular dark button. Secondary action: underlined text with an arrow.
- Technical evidence is presented as a compact definition list/table, not badges.
- Preserve clear `:focus-visible` states, 4.5:1 contrast, reduced-motion support, and accessible table behaviour.

## Homepage plan

### 1. Factual masthead

Use a full-bleed, authentic image such as container loading, grading, quarry, or packing—not the abstract route canvas. Apply a dark crop/overlay only where the copy needs it.

- Brand: Jade Waves Enterprise / Industrial Mineral Export
- H1: a concise operational promise, e.g. “Mineral supply from India, verified before dispatch.”
- Supporting sentence: chemistry, packing, and FCL/export handling aligned before cargo moves.
- Primary action: **Request a specification** or **Talk to the export desk**.
- Secondary text action: **View material portfolio →**.
- Evidence line adjacent to the copy: Near Mundra Port · 50 kg / jumbo bag · COA & TDS · FCL handling.

This is the only major first-view action. Sample requests remain available within the form and product detail pages.

### 2. Proof ledger

A four-row, rule-separated ledger immediately below the hero. Each entry contains a factual label and one plain-language proof statement:

1. Product fit — application, chemistry, and size aligned.
2. Sample & documents — COA/TDS before approval.
3. Packing — 50 kg and jumbo bag options.
4. Export control — Mundra access, FCL, documents, and dispatch updates.

Use only information the business can substantiate. No invented performance metrics.

### 3. Material families

Feature the three highest-value families as editorial bands with distinct, real crops:

- Silica, quartz & feldspar — glass / ceramics / engineered stone.
- Clays & functional fillers — drilling / foundry / coatings.
- Industrial media & pozzolans — blasting / concrete / infrastructure.

Each band has one image, one brief fit statement, and 2–4 linked material rows. Follow it with an economical complete material directory, rather than a wall of equally weighted cards.

### 4. From specification to vessel

Replace animated logistics theatre with a literal four-step, horizontal ledger:

`Requirement → Grade alignment → Sample / COA → Packing & dispatch`

Pair this with inspection, packing, or container imagery. Every step should say what the buyer receives or approves.

### 5. Evidence gallery

Use a compact asymmetric gallery of real quarry, factory, packing, and container images. Include one document preview (COA/TDS) or quality-control visual. Captions should identify the process, not make a marketing claim.

### 6. Contact brief

Finish with a concise inquiry module styled like a procurement brief. Ask for material, application, country/port, volume, preferred packing, and any target specification. Place direct export contact/CEO information here as human proof.

## Product pages

Each product page should use the same repeatable sequence:

1. **Material hero** — real product/macro photograph, name, one-line fit, primary request-spec CTA.
2. **Specification snapshot** — chemistry/grade, available size, packing, and applications in a scannable table.
3. **Use-case fit** — short list of applicable industries and process requirements.
4. **Evidence** — COA, TDS, parameter sheets, inspection/packing images.
5. **Supply route** — concise requirement-to-dispatch steps, specific to that product where relevant.
6. **Inquiry** — contextual form prefilled with the product.

Use an optional product accent sparingly in media captions or a table marker; the core system remains neutral.

## Supporting pages

- **Portfolio:** application-first directory with thumbnails, product forms, end uses, and technical-document access.
- **About / CEO:** an editorial founder note, one real portrait, a small factual operations ledger, no promotional card mosaics.
- **Export markets:** regional buying considerations presented in a simple briefing format—not a map graphic.
- **Blogs:** typographic reading pages; related content is a compact linked list, not a tile grid.

## Motion

- Keep a 180–300ms fade/translate reveal for entered content, once only.
- A photo can subtly scale on hover; linked rows can shift an arrow or underline.
- Remove continuous canvas, parallax, scan lines, floating surfaces, pulsing beacons, and decorative route/network animation.
- Honour `prefers-reduced-motion` by disabling all non-essential motion.

## Implementation plan

1. **Lock the visual direction with a home-page proof.** Build the masthead, proof ledger, one family band, and the new inquiry treatment first. Review at desktop and 360px before site-wide rollout.
2. **Work from the generator, not generated files.** `generate_site.py` is the shared source for page markup, CSS, and client script; direct edits to emitted `index.html` or `styles.css` will be overwritten on the next build.
3. **Create four reusable shells.** Shared header/footer; editorial home; portfolio index; product detail. Add simple semantic primitives for eyebrow, display heading, evidence row, spec table, document link, and CTA row.
4. **Replace rather than layer CSS.** Retire obsolete visual selectors and consolidate the system into tokens, base, layout, components, page shells, and responsive rules. Do not add a third generation of styles on top of the existing 6,000+ lines.
5. **Simplify JavaScript.** Retain menu, form prefill, and form behaviour. Remove the animated route network, continuous scroll transforms, and parallax. Add only a safe IntersectionObserver reveal if it remains useful.
6. **Roll out in priority order.** Home → one flagship product page (Silica Sand) → product template + portfolio → supporting pages → blogs.
7. **Verify before release.** Check home, portfolio, Silica Sand, and one supporting page at 360px and desktop; audit keyboard navigation, form completion, reduced motion, image crop/dimensions, and SEO metadata/JSON-LD/canonicals.

## Acceptance criteria

- The first viewport visibly proves this is a physical mineral-export business.
- A buyer can understand the product, evidence, and next action in under ten seconds.
- There is one obvious CTA per page context.
- Real material/process imagery carries the brand; no generic route/network graphics remain.
- Product data is easier to scan than marketing copy.
- The mobile hero contains image, proposition, one action, and 3–4 factual proof points without excessive scrolling.
- Existing technical documents, inquiry conversion paths, core SEO pages, and schema remain intact.
