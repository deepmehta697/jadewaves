# Jade Waves Enterprise Website

Static marketing site for Jade Waves Enterprise, focused on industrial mineral exports.

## Local Preview

- Home: [http://127.0.0.1:4173/](http://127.0.0.1:4173/)
- Products: [http://127.0.0.1:4173/products/](http://127.0.0.1:4173/products/)

To run the site locally:

```bash
cd /Users/deepmehta/Documents/Jadewaves
python3 -m http.server 4173
```

## Project Files

- `generate_site.py` — product/blog data, metadata, and static page generation
- `templates/material_pages.py` — homepage, portfolio, product, company, markets, and journal layouts
- `templates/material_layout.py` — shared navigation, footer, and procurement form
- `templates/material_support.py` — operations and policy pages
- `templates/material-ledger.css` — the shared design system
- `templates/material-ledger.js` — navigation, form requests, and restrained reveals
- `assets/responsive/` — responsive WebP images and their source manifest
- `index.html`, `products/`, `styles.css`, and `script.js` — generated output; edit the sources above

## Build and Verify

Regenerate and assemble the static artifact:

```bash
python3 scripts/build_site.py --regenerate
python3 scripts/verify_site.py --root _site
```

When authored images change, prepare their responsive copies after an initial regeneration. This optional preparation step requires Pillow; regular builds use the saved manifest and do not require it.

```bash
python3 generate_site.py
python3 scripts/prepare_site_images.py
python3 scripts/build_site.py --regenerate
```

The source verifier checks active pages, metadata, structured data, document and image references, section anchors, inquiry fields, and design invariants. Desktop/mobile browser review is also required for visual release approval.
