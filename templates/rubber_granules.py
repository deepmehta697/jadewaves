"""One-image colour reference carousel within the existing core product page."""
from html import escape
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def catalogue():
    return json.loads((ROOT/'assets/rubber-granules/catalogue.json').read_text())


def render_colours():
    entries = catalogue()
    first = entries[0]
    options = ''.join(f'<option value="{e["id"]}">{escape(e["name"])}{(" · RAL " + e["ral"]) if e["ral"] else ""}</option>' for e in entries)
    links = ', '.join(f'<a href="/{e["src"]}">{escape(e["name"])}{(" · chart RAL " + e["ral"]) if e["ral"] else ""}</a>' for e in entries)
    data = json.dumps(entries, ensure_ascii=False).replace('<', '\\u003c')
    return f'''<section class="ml-section rubber-colours" id="colour-range" aria-labelledby="rubber-colours-heading">
      <div class="ml-container">
        <div class="ml-section-head" data-reveal><div><p class="ml-eyebrow">Colour range</p><h2 id="rubber-colours-heading">Find your colour.</h2></div></div>
        <div class="rubber-colour-carousel" role="region" aria-roledescription="carousel" aria-label="Rubber granule colour references" tabindex="0" data-rubber-carousel>
          <div class="rubber-colour-stage" data-reveal>
            <figure class="rubber-colour-photo" role="group" aria-roledescription="slide" aria-label="1 of {len(entries)}: Black" data-rubber-frame>
              <img src="/{first['src']}" alt="{escape(first['alt'])}" width="{first['width']}" height="{first['height']}" loading="lazy" decoding="async" data-rubber-photo>
            </figure>
            <div class="rubber-colour-controls" data-rubber-controls hidden><span data-rubber-counter>01 / {len(entries):02d}</span><div>
              <button type="button" aria-label="Previous rubber colour" data-rubber-prev>←</button>
              <button type="button" aria-label="Next rubber colour" data-rubber-next>→</button>
            </div></div>
          </div>
          <div class="rubber-colour-selection" data-reveal>
            <h3 data-rubber-name>Black</h3><p class="rubber-colour-reference" data-rubber-reference hidden></p>
            <label for="rubber-colour">Colour</label><select id="rubber-colour" data-rubber-select disabled>{options}</select>
            <p class="rubber-colour-note">Chart references only. Confirm material type, grading and shade with a sample.</p>
            <a class="button button--dark" href="#contact" data-set-request="Sample" data-rubber-enquire>Request a colour sample <span aria-hidden="true">↗</span></a>
            <p class="rubber-colour-status" role="status" aria-live="polite" aria-atomic="true" data-rubber-announcement></p>
          </div>
        </div>
        <noscript><p class="rubber-colour-note">View colour references: {links}. Printed RAL references are shown in the colour list; confirm the shade with a sample.</p></noscript>
      </div><script type="application/json" id="rubber-colour-data">{data}</script>
    </section>'''


def add_assets(g, html):
    return html.replace('</head>',
        f'<link rel="stylesheet" href="assets/rubber-granules/carousel.css?v={g["BUILD_VERSION"]}">'
        f'<script defer src="assets/rubber-granules/carousel.js?v={g["BUILD_VERSION"]}"></script></head>')
