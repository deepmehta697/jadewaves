# Product buyer guide evidence

Source review date: 2026-10-13. These eight original guides are prepared in
`templates/product_guides.py`. The user authorized publishing them on
13 October 2026. Each record has stable publication and modification dates for
this first release; routine site builds must not advance either date.

## Evidence boundary

The guides describe existing product records and ask buyers to confirm the
selected material, measurement methods, quotation, and acceptance basis. They
do not turn portfolio figures into guaranteed specifications or present a
representative sample document as a measured shipment certificate.

Primary repository evidence:

- `generate_site.py`, `PRODUCTS`: product names, slugs, listed applications,
  forms, booking points, and published numeric reference values.
- `generate_site.py`, `PACKING_BY_SLUG`: current packing overrides. Use these
  alongside each product's base record; broader TDS packing descriptions are
  separately identified when they differ from the current product reference.
- `generate_tds_pdfs.py`, `PRODUCTS`: text and reference data used to prepare
  the linked technical data sheets and sample COAs.
- `generate_tds_pdfs.py`, `build_tds_story`: published values are aligned again
  against the selected grade, mesh, packing, and shipment requirement before
  final order confirmation.
- `generate_tds_pdfs.py`, `build_coa_story`: the sample COA is a representative,
  client-facing reference; current lot values and final documents require
  confirmation against the approved grade and order basis.
- `templates/material_pages.py`, `_documents`: existing product
  technical-reference links and the china-clay / quartz-sand filename mapping.
- `generate_site.py`, existing `BLOGS` records, and
  `templates/material_pages.py`, `render_blog_post_page`: the existing guide
  record contract and rendering of sections and RFQ questions.

Repository sources were sufficient for the included product descriptions and
reference values. No external technical claims were added. Questions about
test methods, application approval, and project requirements are proposed
buyer checks, not assertions that Jade Waves has the requested certification,
test results, or capability.

## Per-guide evidence and buyer checks

### Silica flour

Guide: `silica-flour-mesh-micron-grade-selection-guide`.

- Record: `generate_site.py`, `PRODUCTS` item `silica-flour`.
- Sheet source: `generate_tds_pdfs.py`, `PRODUCTS` item `silica-flour`.
- Assets: `assets/tds/silica-flour-technical-data-sheet.pdf` and
  `assets/coas/silica-flour-sample-coa.pdf`.
- Grounded descriptions: powder; 80, 300, and 500 mesh options; custom micron
  grading; ceramics, coatings, and fillers; reference SiO2 99.10% and Fe2O3
  0.036%; 50 kg / jumbo bag packing.
- Buyer checks: sieve or particle-size method, measured distribution, any
  whiteness and moisture limits, selected-sample chemistry, process trial,
  and repeat-order acceptance. The guide provides no mesh-to-micron
  conversion or guarantee that a particular grade will disperse successfully.

### Bentonite

Guide: `bentonite-application-grade-trial-checklist`.

- Record: `generate_site.py`, `PRODUCTS` item `bentonite`.
- Sheet source: `generate_tds_pdfs.py`, `PRODUCTS` item `bentonite`.
- Assets: `assets/tds/bentonite-technical-data-sheet.pdf` and
  `assets/coas/bentonite-sample-coa.pdf`.
- Grounded descriptions: sodium, calcium, and application-specific grades;
  drilling, foundry, sealing, and absorbent applications; reference moisture
  14% max, liquid limit 450 min, gel index 60 min, and Marsh funnel viscosity
  50 sec min; pH reference uses a 2% suspension; 50 kg / jumbo bag packing.
- Buyer checks: exact application and supplied form, applicability of reference
  parameters, missing units and methods, preparation conditions, sample trial,
  and lot evidence. Undefined liquid-limit and gel-index units are explicitly
  requested rather than supplied or inferred. No application or standards
  compliance is promised.

### Kaolin / china clay

Guide: `kaolin-china-clay-brightness-fineness-buyer-guide`.

- Record: `generate_site.py`, `PRODUCTS` item `kaolin--china-clay`.
- Sheet source: `generate_tds_pdfs.py`, `PRODUCTS` item `china-clay`.
- Assets: `assets/tds/china-clay-technical-data-sheet.pdf` and
  `assets/coas/china-clay-sample-coa.pdf`.
- Grounded descriptions: lumps and powder; ceramics, coatings, paper, and
  industrial fillers; reference whiteness 86.17, L* 94.48, Fe2O3 0.29%, and
  Al2O3 37.01%; a residue reference at 240# after two minutes of grinding;
  50 kg / jumbo bag packing under the current product override.
- Buyer checks: offered processing description, optical measurement methods,
  supplied-form chemistry, particle or residue results and units, moisture,
  and formulation or firing evaluation. No conversion between whiteness and
  L* is made. The sample COA's appearance/form information is distinguished
  from requested measured optical evidence.

### Talc

Guide: `talc-powder-mesh-brightness-rfq-guide`.

- Record: `generate_site.py`, `PRODUCTS` item `talc`.
- Sheet source: `generate_tds_pdfs.py`, `PRODUCTS` item `talc`.
- Assets: `assets/tds/talc-technical-data-sheet.pdf` and
  `assets/coas/talc-sample-coa.pdf`.
- Grounded descriptions: powder in application-specific mesh sizes; industrial
  uses including plastics, coatings, ceramics, and rubber; sheet also lists
  chips and lumps; brightness reference 90%; product booking points name MgO,
  SiO2, and whiteness; current product packing is jumbo bags, while the TDS
  also lists 50 kg bags. The guide asks buyers to confirm the offered format.
- Buyer checks: measured sizing and optical methods, selected-grade composition,
  application-specific qualification, and formulation trial. No numerical MgO
  or SiO2 claim is introduced. The guide makes no pharmaceutical, cosmetic,
  food, purity, contaminant-free, or safety qualification claim.

### Industrial salt

Guide: `industrial-salt-purity-grain-size-buyer-guide`.

- Record: `generate_site.py`, `PRODUCTS` item `salt`.
- Sheet source: `generate_tds_pdfs.py`, `PRODUCTS` item `salt`.
- Assets: `assets/tds/salt-technical-data-sheet.pdf` and
  `assets/coas/salt-sample-coa.pdf`.
- Grounded descriptions: listed industrial, crystalline, raw, de-icing, and
  iodized grades; chemical, treatment, and utility uses; reference NaCl 99.00%
  min and moisture 0.2% max; grain size is a booking point; 50 kg / jumbo bags.
- Buyer checks: grade for the intended industrial use, reporting basis,
  impurities required by the buyer's process, iodine requirement, measured
  grain distribution, selected-grade results, and repeat-order documents.
  Food or consumption use is framed as a separate qualification request.
  Listing iodized grades is not presented as proof of certified food suitability.

### Fly ash

Guide: `fly-ash-technical-documents-trial-acceptance-guide`.

- Record: `generate_site.py`, `PRODUCTS` item `fly-ash`.
- Sheet source: `generate_tds_pdfs.py`, `PRODUCTS` item `fly-ash`.
- Assets: `assets/tds/fly-ash-technical-data-sheet.pdf` and
  `assets/coas/fly-ash-sample-coa.pdf`.
- Grounded descriptions: cement, concrete, blocks, roads, and infrastructure
  applications; reference SiO2 55.13%, Al2O3 24.45%, loss on ignition below 1%,
  and residue on 45 micron sieve below 12%; dry/bulk forms; current product
  packing is jumbo bags, while the TDS also lists 50 kg bags.
- Buyer checks: offered source/grade, required project standard and
  classification, evidence for each criterion, technical-team-defined trial
  and performance measurements, receiving arrangement, and lot documents.
  No class, standard compliance, strength, replacement ratio, or performance
  guarantee is inferred from the reference chemistry. Loose bulk handling is
  a request to confirm the offered arrangement, not an asserted capability.

### Copper slag

Guide: `copper-slag-grit-size-blasting-trial-guide`.

- Record: `generate_site.py`, `PRODUCTS` item `copper-slag`.
- Sheet source: `generate_tds_pdfs.py`, `PRODUCTS` item `copper-slag`.
- Assets: `assets/tds/copper-slag-technical-data-sheet.pdf` and
  `assets/coas/copper-slag-sample-coa.pdf`.
- Grounded descriptions: abrasive blasting and surface preparation; portfolio
  size fractions from 4.00-3.00 mm to 0.212 mm and below; reference Mohs hardness
  6.0-7.0, specific gravity 3.51, angular granules; current product packing is
  jumbo bags, while the TDS also lists 50 kg bags.
- Buyer checks: selected grit distribution, project abrasive requirements,
  property methods/reports, trial operating conditions, observed surface result,
  and repeat-order controls. No achieved surface profile, consumption rate,
  reuse count, cleanliness class, chemical safety, or handling result is promised.

### Rubber granules

Guide: `rubber-granules-material-size-surface-system-guide`.

- Record: `generate_site.py`, `PRODUCTS` item `rubber-granules`.
- Existing product renderer has no matching rubber-granules TDS/sample COA
  mapping. The TDS/COA generator has no rubber-granules item.
- Grounded descriptions: SBR rubber granules, crumb rubber, application-specific
  grades; turf, sports, playground, and construction uses; booking points name
  application, size, material type, color, packing, and quantity; 50 kg / jumbo bags.
- Buyer checks: actual offered material/composition, grading, moisture and
  cleanliness criteria, color, project-required reports, sample evaluation,
  and installed-system approval requirements. No EPDM availability, chemical
  limit, recycled-content percentage, certified impact performance, durability,
  environmental benefit, or safety qualification is asserted. Surface-system
  evidence is requested for review by the responsible designer or installer.

## Integration and validation

The module exports `PRODUCT_GUIDES` and `PRODUCT_GUIDE_SLUGS`. Add the records to
the generator's active and complete blog collections before page generation;
add their slugs to the current guide set. Product records use the existing
canonical slugs, notably `kaolin--china-clay` and `salt`.

The new slugs are distinct from the legacy article names inspected in
`generate_site.py`. The generator integration should still verify that no
redirect writer runs over an active guide path.

Example import:

```python
from templates.product_guides import PRODUCT_GUIDES, PRODUCT_GUIDE_SLUGS
```

Structural checks should confirm eight unique guides, exactly one per covered
product, valid ISO review dates, all required renderer fields, meaningful
sections/questions, and recorded publication dates for the authorized release.
The parent integration should additionally generate and verify the article
pages, canonical URLs, internal links, and sitemap entries.
