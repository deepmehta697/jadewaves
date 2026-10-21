"""Supplied salt sample photographs, one visible at a time."""
from html import escape
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IODINE_NOTE = 'Iodine content can be customized as per client requirements.'


def catalogue():
    return json.loads((ROOT/'assets/salt/catalogue.json').read_text())


def render():
    entries = catalogue(); first = entries[0]
    options = ''.join(f'<option value="{e["id"]}">{escape(e["name"])}</option>' for e in entries)
    links = ', '.join(f'<a href="/{e["src"]}">{escape(e["name"])}</a>' for e in entries)
    data = json.dumps(entries, ensure_ascii=False).replace('<', '\\u003c')
    return f'''<section class="ml-section salt-gallery" id="salt-gallery" aria-labelledby="salt-gallery-heading"><div class="ml-container">
      <div class="ml-section-head" data-reveal><div><p class="ml-eyebrow">Sample gallery</p><h2 id="salt-gallery-heading">Salt grades.</h2></div></div>
      <div class="salt-carousel" role="region" aria-roledescription="carousel" aria-label="Salt sample photographs" tabindex="0" data-salt-carousel>
        <div class="salt-stage" data-reveal>
          <figure class="salt-photo" role="group" aria-roledescription="slide" aria-label="1 of 5: {escape(first['name'])}" data-salt-frame>
            <img src="/{first['src']}" alt="{escape(first['alt'])}" width="{first['width']}" height="{first['height']}" loading="lazy" decoding="async" data-salt-photo>
          </figure>
          <div class="salt-controls" data-salt-controls hidden><span data-salt-counter>01 / 05</span><div>
            <button type="button" aria-label="Previous salt photo" data-salt-prev>←</button>
            <button type="button" aria-label="Next salt photo" data-salt-next>→</button>
          </div></div>
        </div>
        <div class="salt-selection" data-reveal>
          <h3 data-salt-name>{escape(first['name'])}</h3>
          <label for="salt-photo-choice">Salt sample</label><select id="salt-photo-choice" data-salt-select disabled>{options}</select>
          <p class="salt-iodine-note">{IODINE_NOTE}</p>
          <p class="salt-gallery-note">Confirm the required grade and iodine level with your enquiry.</p>
          <a class="button button--dark" href="#contact" data-set-request="Sample" data-salt-enquire>Request a sample <span aria-hidden="true">↗</span></a>
          <p class="salt-status" role="status" aria-live="polite" aria-atomic="true" data-salt-announcement></p>
        </div>
      </div>
      <noscript><p class="salt-gallery-note">View the sample photographs: {links}.</p></noscript>
    </div><script type="application/json" id="salt-gallery-data">{data}</script></section>'''


def add_assets(g, html):
    return html.replace('</head>',
        f'<link rel="stylesheet" href="assets/salt/carousel.css?v={g["BUILD_VERSION"]}">'
        f'<script defer src="assets/salt/carousel.js?v={g["BUILD_VERSION"]}"></script></head>')
