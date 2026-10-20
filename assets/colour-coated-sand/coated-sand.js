(() => {
  'use strict';
  const entries = JSON.parse(document.getElementById('coated-sand-data').textContent);
  const carousel = document.querySelector('[data-sand-carousel]');
  const select = document.querySelector('[data-sand-select]');
  const photo = document.querySelector('[data-sand-photo]');
  const frame = document.querySelector('[data-sand-frame]');
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  let index = 0;
  const render = (next, announce = true) => {
    index = (next + entries.length) % entries.length;
    const entry = entries[index];
    select.value = entry.id;
    photo.classList.remove('is-changing');
    photo.src = entry.src;
    photo.alt = `${entry.name} colour-coated silica sand grain appearance`;
    photo.width = entry.width;
    photo.height = entry.height;
    frame.setAttribute('aria-label', `${index + 1} of ${entries.length}: ${entry.name} colour-coated silica sand`);
    document.querySelector('[data-sand-name]').textContent = entry.name;
    document.querySelector('[data-sand-counter]').textContent = `${String(index + 1).padStart(2, '0')} / ${String(entries.length).padStart(2, '0')}`;
    const body = `Hello Jade Waves,\n\nI would like to discuss colour-coated silica sand.\n\nColour: ${entry.name}\nGrain size: ${entry.size}\nApplication / finish system: \nQuantity: \nDestination: \nSample required: \n\nPlease confirm the shade, coating performance, sizing and packing.\n`;
    document.querySelector('[data-sand-email]').href = `mailto:deep@jadewavesenterprise.com?subject=${encodeURIComponent('Colour-coated silica sand — ' + entry.name)}&body=${encodeURIComponent(body)}`;
    if (announce) document.querySelector('[data-sand-announcement]').textContent = `${entry.name}, colour-coated silica sand, ${entry.size}. ${index + 1} of ${entries.length}.`;
  };
  select.addEventListener('change', () => {
    const next = entries.findIndex(entry => entry.id === select.value);
    if (next >= 0) render(next);
  });
  document.querySelector('[data-sand-prev]').addEventListener('click', () => render(index - 1));
  document.querySelector('[data-sand-next]').addEventListener('click', () => render(index + 1));
  photo.addEventListener('load', () => { if (!reduced.matches) photo.classList.add('is-changing'); });
  carousel.addEventListener('keydown', event => {
    if (event.target.closest('select,button,a,input,textarea')) return;
    if (event.key === 'ArrowLeft') { event.preventDefault(); render(index - 1); }
    else if (event.key === 'ArrowRight') { event.preventDefault(); render(index + 1); }
    else if (event.key === 'Home') { event.preventDefault(); render(0); }
    else if (event.key === 'End') { event.preventDefault(); render(entries.length - 1); }
  });
  let start = null;
  frame.addEventListener('pointerdown', event => {
    if (event.pointerType === 'touch') start = {x:event.clientX, y:event.clientY};
  });
  frame.addEventListener('pointercancel', () => { start = null; });
  frame.addEventListener('pointerup', event => {
    if (!start || event.pointerType !== 'touch') return;
    const dx = event.clientX - start.x, dy = event.clientY - start.y;
    start = null;
    if (Math.abs(dx) >= 45 && Math.abs(dx) > Math.abs(dy) * 1.5) render(index + (dx < 0 ? 1 : -1));
  });
  select.disabled = false;
  document.querySelector('[data-sand-controls]').hidden = false;
  render(0, false);
})();
