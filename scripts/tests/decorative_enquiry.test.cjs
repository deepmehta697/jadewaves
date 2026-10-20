/* Selection bridge contracts only; no real browser, CAPTCHA or network requests. */
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const root = path.resolve(__dirname, '../..');
const source = fs.readFileSync(path.join(root, 'assets/decorative-products/enquiry.js'), 'utf8');
const json = file => JSON.parse(fs.readFileSync(path.join(root, file), 'utf8'));
const products = json('templates/decorative-products.json');

function setup(slug, reduced = false) {
  const generic = products.find(p => p.slug === slug);
  const entries = json(`assets/${slug === 'colour-coated-silica-sand' ? 'colour-coated-sand' : slug}/catalogue.json`);
  const colours = slug === 'grout-sand' ? json('assets/grout-sand/colours.json') : [];
  const dataId = generic ? 'decorative-product-data' : slug === 'pebbles' ? 'pebble-data' : 'coated-sand-data';
  const data = generic ? {...generic, entries, colours} : entries;
  const nodes = new Map();
  const get = selector => {
    if (!nodes.has(selector)) nodes.set(selector, {value: '', textContent: ''});
    return nodes.get(selector);
  };
  get('[data-product-select]').value = entries[0].id;
  get('[data-product-size]').value = generic?.sizes[0];
  get('[data-product-colour]:checked').value = colours[0]?.id;
  get('[data-sand-select]').value = entries[0].id;
  get('[data-variant]').value = entries[0].id;
  get('[data-enquiry-size]').value = entries[0].sizes?.[0];
  const formListeners = {}, docListeners = {}, linkListeners = {};
  const notes = {value: ''};
  const form = {
    elements: {namedItem(name) { assert.equal(name, 'notes'); return notes; }},
    addEventListener(event, handler, options) { formListeners[event] = {handler, options}; },
  };
  const calls = [];
  const heading = {focus(options) {calls.push(['focus', options]);}, scrollIntoView(options) {calls.push(['scroll', options]);}};
  const document = {
    getElementById(id) { return id === dataId ? {textContent: JSON.stringify(data)} : id === 'decorative-enquiry-title' ? heading : null; },
    querySelector(selector) { return selector === '[data-decorative-form]' ? form : get(selector); },
    querySelectorAll() { return [{addEventListener(event, handler) {linkListeners[event] = handler;}}]; },
    addEventListener(event, handler) {docListeners[event] = handler;},
  };
  vm.runInNewContext(source, {document, window: {matchMedia: () => ({matches: reduced})}});
  return {get, entries, colours, generic, notes, calls, formListeners, docListeners, linkListeners,
    change() {docListeners.change();}, submit() {formListeners.submit.handler();},
    galleryClick() {docListeners.click({target: {closest: () => true}});}};
}

for (const slug of ['glass-chips', 'grout-sand', 'marble-chips']) {
  test(`${slug}: every catalogue photo and size reaches the on-site enquiry`, () => {
    const h = setup(slug);
    h.entries.forEach(entry => {
      h.get('[data-product-select]').value = entry.id;
      h.generic.sizes.forEach(size => {
        h.get('[data-product-size]').value = size; h.change();
        assert.ok(h.notes.value.includes(entry.name));
        assert.ok(h.notes.value.includes(size));
        assert.equal(h.get('[data-decorative-selection]').textContent, h.notes.value);
      });
    });
  });
}

test('all 25 grout colours preserve independent photo and grade', () => {
  const h = setup('grout-sand');
  h.get('[data-product-select]').value = h.entries[1].id;
  h.get('[data-product-size]').value = '150 mesh';
  h.colours.forEach(colour => {
    h.get('[data-product-colour]:checked').value = colour.id; h.change();
    assert.ok(h.notes.value.includes('Requested colour: ' + colour.name));
    assert.ok(h.notes.value.includes(h.entries[1].name));
    assert.ok(h.notes.value.includes('150 mesh'));
  });
});

test('all six coated shades preserve their own catalogue grade', () => {
  const h = setup('colour-coated-silica-sand');
  h.entries.forEach(entry => {
    h.get('[data-sand-select]').value = entry.id; h.change();
    assert.equal(h.notes.value, `Colour: ${entry.name}\nGrain size: ${entry.size}`);
  });
});

test('all 31 pebble selections use only sizes offered for that selection', () => {
  const h = setup('pebbles');
  h.entries.forEach(entry => {
    h.get('[data-variant]').value = entry.id;
    entry.sizes.forEach(size => {
      h.get('[data-enquiry-size]').value = size; h.change();
      assert.equal(h.notes.value, `Pebble: ${entry.name}\nFinish: ${entry.finish}\nPreferred size: ${size}`);
    });
  });
});

test('capture-phase submit includes the latest buyer notes without overwriting them', () => {
  const h = setup('glass-chips');
  h.get('[data-decorative-message]').value = 'Private packing instructions';
  h.get('[data-product-select]').value = h.entries[2].id;
  assert.equal(h.formListeners.submit.options.capture, true);
  h.submit();
  assert.ok(h.notes.value.includes(h.entries[2].name));
  assert.ok(h.notes.value.endsWith('Buyer notes: Private packing instructions'));
  assert.equal(h.get('[data-decorative-message]').value, 'Private packing instructions');
  assert.equal(h.get('[data-decorative-selection]').textContent.includes('Private'), false);
});

test('gallery arrows refresh the visible form summary without requiring a CTA click', () => {
  const h = setup('glass-chips');
  h.get('[data-product-select]').value = h.entries[3].id; h.galleryClick();
  assert.ok(h.get('[data-decorative-selection]').textContent.includes(h.entries[3].name));
});

test('invalid free-text selections cannot leak into the catalogue summary', () => {
  for (const slug of ['glass-chips', 'grout-sand', 'pebbles', 'colour-coated-silica-sand', 'marble-chips']) {
    const h = setup(slug);
    for (const selector of ['[data-product-select]', '[data-product-size]', '[data-product-colour]:checked', '[data-variant]', '[data-enquiry-size]', '[data-sand-select]']) h.get(selector).value = 'private@example.test';
    h.change();
    assert.equal(h.notes.value.includes('private@example.test'), false);
    assert.ok(h.notes.value.includes(h.entries[0].name));
  }
});

test('after a form reset, the next submit restores current catalogue context', () => {
  const h = setup('glass-chips');
  h.get('[data-product-select]').value = h.entries[4].id;
  h.notes.value = ''; h.get('[data-decorative-message]').value = '';
  h.submit();
  assert.ok(h.notes.value.includes(h.entries[4].name));
});

for (const reduced of [false, true]) {
  test(`CTA focuses the enquiry heading and respects reduced motion: ${reduced}`, () => {
    const h = setup('grout-sand', reduced); let prevented = false;
    h.linkListeners.click({preventDefault() {prevented = true;}});
    assert.equal(prevented, true);
    assert.equal(h.calls[0][0], 'focus');
    assert.equal(h.calls[1][1].behavior, reduced ? 'instant' : 'smooth');
  });
}

test('selection bridge never submits, emits analytics, stores notes or uses timers', () => {
  assert.equal(/\bfetch\(|XMLHttpRequest|sendBeacon|gtag\(|localStorage|sessionStorage|setInterval|setTimeout/.test(source), false);
});
