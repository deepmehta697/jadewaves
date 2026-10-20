/* Synchronize catalogue-only selections; the shared handler submits and tracks. */
(() => {
  'use strict';
  const form = document.querySelector('[data-decorative-form]');
  if (!form) return;
  const read = id => {
    const node = document.getElementById(id);
    return node ? JSON.parse(node.textContent) : null;
  };
  const product = read('decorative-product-data');
  const sand = read('coated-sand-data');
  const pebbles = read('pebble-data');
  const value = selector => document.querySelector(selector)?.value;
  const selection = () => {
    if (product) {
      const entry = product.entries.find(e => e.id === value('[data-product-select]')) || product.entries[0];
      const size = value('[data-product-size]');
      const colour = (product.colours || []).find(c => c.id === value('[data-product-colour]:checked'));
      return `${product.choice_label}: ${entry.name}\n${product.size_label}: ${product.sizes.includes(size) ? size : product.sizes[0]}${colour ? '\nRequested colour: ' + colour.name : ''}`;
    }
    if (sand) {
      const entry = sand.find(e => e.id === value('[data-sand-select]')) || sand[0];
      return `Colour: ${entry.name}\nGrain size: ${entry.size}`;
    }
    if (pebbles) {
      const entry = pebbles.find(e => e.id === value('[data-variant]')) || pebbles[0];
      const size = value('[data-enquiry-size]');
      return `Pebble: ${entry.name}\nFinish: ${entry.finish}\nPreferred size: ${entry.sizes.includes(size) ? size : entry.sizes[0]}`;
    }
    return '';
  };
  const sync = () => {
    const summary = selection();
    document.querySelector('[data-decorative-selection]').textContent = summary;
    const message = document.querySelector('[data-decorative-message]').value.trim();
    form.elements.namedItem('notes').value = summary + (message ? '\n\nBuyer notes: ' + message : '');
  };
  // Bubble after each carousel's own handler; no user notes are overwritten.
  document.addEventListener('change', sync);
  document.addEventListener('click', event => {
    if (event.target.closest('[data-product-controls], [data-sand-controls], [data-controls]')) sync();
  });
  form.addEventListener('submit', sync, {capture: true});
  document.querySelectorAll('[data-decorative-enquire], [data-selection-link]').forEach(link => {
    link.addEventListener('click', event => {
      event.preventDefault();
      sync();
      const heading = document.getElementById('decorative-enquiry-title');
      heading.focus({preventScroll: true});
      heading.scrollIntoView({behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth', block: 'start'});
    });
  });
  sync();
})();
