(() => {
  'use strict';
  const entries = JSON.parse(document.getElementById('pebble-data').textContent);
  const viewer = document.querySelector('[data-carousel]');
  const variant = document.querySelector('[data-variant]');
  const preferredSize = document.querySelector('[data-enquiry-size]');
  const photo = document.querySelector('[data-photo]');
  const frame = document.querySelector('[data-photo-frame]');
  const announcement = document.querySelector('[data-announcement]');
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  let index = 0;

  const text = (selector, value) => { document.querySelector(selector).textContent = value; };
  const setEmail = () => {
    const current = entries[index];
    const size = preferredSize.value;
    const subject = `Pebble enquiry — ${current.name}`;
    const body = `Hello Jade Waves,\n\nI would like to discuss the following selection.\n\nPebble: ${current.name}\nFinish: ${current.finish}\nPreferred size: ${size}\nQuantity: \nDestination: \nSample required: \n\nPlease confirm the selection, sizing and packing.\n`;
    document.querySelector('[data-email]').href = `mailto:deep@jadewavesenterprise.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
  };
  const render = (nextIndex, notify = true) => {
    index = (nextIndex + entries.length) % entries.length;
    const current = entries[index];
    variant.value = current.id;
    photo.classList.remove('is-changing');
    photo.src = current.src;
    photo.alt = `${current.name} — colour and finish reference`;
    photo.width = current.width;
    photo.height = current.height;
    frame.setAttribute('aria-label', `${index + 1} of ${entries.length}: ${current.name}`);
    text('[data-name]', current.name);
    text('[data-finish]', current.finish);
    text('[data-sizes]', current.sizes.join(' · '));
    text('[data-colour]', current.color);
    text('[data-packing]', current.packing);
    text('[data-photo-index]', `${String(index + 1).padStart(2, '0')} / ${entries.length}`);
    text('[data-brief-name]', current.name);
    preferredSize.replaceChildren(...current.sizes.map(size => new Option(size, size)));
    setEmail();
    if (notify) announcement.textContent = `${current.name}. ${current.finish}. Sizes: ${current.sizes.join(', ')}. ${index + 1} of ${entries.length}.`;
  };
  photo.addEventListener('load', () => {
    if (!reducedMotion.matches) photo.classList.add('is-changing');
  });
  variant.addEventListener('change', () => {
    const selectedIndex = entries.findIndex(entry => entry.id === variant.value);
    if (selectedIndex >= 0) render(selectedIndex);
  });
  document.querySelector('[data-previous]').addEventListener('click', () => render(index - 1));
  document.querySelector('[data-next]').addEventListener('click', () => render(index + 1));
  preferredSize.addEventListener('change', setEmail);
  viewer.addEventListener('keydown', event => {
    if (event.target.closest('select,input,textarea,a,button')) return;
    if (event.key === 'ArrowRight') { event.preventDefault(); render(index + 1); }
    else if (event.key === 'ArrowLeft') { event.preventDefault(); render(index - 1); }
    else if (event.key === 'Home') { event.preventDefault(); render(0); }
    else if (event.key === 'End') { event.preventDefault(); render(entries.length - 1); }
  });
  let start = null;
  frame.addEventListener('pointerdown', event => {
    if (event.pointerType === 'touch') start = {x: event.clientX, y: event.clientY};
  });
  frame.addEventListener('pointercancel', () => { start = null; });
  frame.addEventListener('pointerup', event => {
    if (!start || event.pointerType !== 'touch') return;
    const deltaX = event.clientX - start.x;
    const deltaY = event.clientY - start.y;
    start = null;
    if (Math.abs(deltaX) >= 45 && Math.abs(deltaX) > Math.abs(deltaY) * 1.5) render(index + (deltaX < 0 ? 1 : -1));
  });
  document.querySelector('[data-controls]').hidden = false;
  variant.disabled = false;
  preferredSize.disabled = false;
  render(0, false);
})();
