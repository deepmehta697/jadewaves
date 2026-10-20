/* Manual, contextual selection only. Opening an email draft is not a lead. */
(() => {
  'use strict';
  const data = JSON.parse(document.getElementById('decorative-product-data').textContent);
  const {entries, sizes} = data;
  const colours = data.colours || [];
  const colourControls = [...document.querySelectorAll('[data-product-colour]')];
  const get = name => document.querySelector(`[data-product-${name}]`);
  const carousel = get('carousel'), select = get('select'), size = get('size');
  const photo = get('photo'), frame = get('frame');
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  let index = 0, selectedSize = sizes[0], start = null;
  let selectedColour = colours[0] || null;
  const updateEmail = () => {
    const entry = entries[index];
    const colourLine = selectedColour ? `Requested colour: ${selectedColour.name}\n` : '';
    const body = `Hello Jade Waves,\n\nI would like to discuss ${data.name.toLowerCase()}.\n\n${data.choice_label}: ${entry.name}\n${data.size_label}: ${selectedSize}\n${colourLine}Target shade / finish: \nApplication / binder system: \nQuantity: \nDestination: \nSample required: \n\n${data.enquiry_note}\n`;
    const href = `mailto:deep@jadewavesenterprise.com?subject=${encodeURIComponent(data.name + ' — ' + (selectedColour ? selectedColour.name : entry.name) + ' — ' + selectedSize)}&body=${encodeURIComponent(body)}`;
    get('email').href = href;
    if (selectedColour) {
      get('selected-colour').textContent = selectedColour.name;
      get('colour-email').href = href;
    }
  };
  const announce = () => {
    get('announcement').textContent = `${entries[index].name}, ${selectedSize}.${selectedColour ? ' Requested colour: ' + selectedColour.name + '.' : ''} ${index + 1} of ${entries.length}.`;
  };
  colourControls.forEach(control => {
    control.disabled = false;
    control.addEventListener('change', () => {
      if (!control.checked) return;
      const next = colours.find(colour => colour.id === control.value);
      if (next) { selectedColour = next; updateEmail(); announce(); }
      colourControls.forEach(radio => { radio.checked = radio.value === selectedColour.id; });
    });
  });
  const render = (next, notify = true) => {
    index = (next + entries.length) % entries.length;
    const entry = entries[index];
    select.value = entry.id;
    photo.classList.remove('is-changing');
    photo.src = entry.src; photo.alt = entry.alt;
    photo.width = entry.width; photo.height = entry.height;
    frame.setAttribute('aria-label', `${index + 1} of ${entries.length}: ${entry.name}`);
    get('name').textContent = entry.name;
    get('counter').textContent = `${String(index + 1).padStart(2, '0')} / ${String(entries.length).padStart(2, '0')}`;
    updateEmail();
    if (notify) announce();
  };
  select.addEventListener('change', () => {
    const next = entries.findIndex(entry => entry.id === select.value);
    if (next >= 0) render(next);
    else select.value = entries[index].id;
  });
  size.addEventListener('change', () => {
    if (!sizes.includes(size.value)) { size.value = selectedSize; return; }
    selectedSize = size.value; updateEmail(); announce();
  });
  get('prev').addEventListener('click', () => render(index - 1));
  get('next').addEventListener('click', () => render(index + 1));
  photo.addEventListener('load', () => { if (!reduced.matches) photo.classList.add('is-changing'); });
  photo.addEventListener('error', () => { get('announcement').textContent = 'Photo unavailable. Please choose another view or enquire about a sample.'; });
  carousel.addEventListener('keydown', event => {
    if (event.target.closest('select,button,a,input,textarea')) return;
    const next = {ArrowLeft: index - 1, ArrowRight: index + 1, Home: 0, End: entries.length - 1}[event.key];
    if (next !== undefined) { event.preventDefault(); render(next); }
  });
  frame.addEventListener('pointerdown', event => {
    if (event.pointerType === 'touch') start = {x: event.clientX, y: event.clientY};
  });
  frame.addEventListener('pointercancel', () => { start = null; });
  frame.addEventListener('pointerup', event => {
    if (!start || event.pointerType !== 'touch') return;
    const dx = event.clientX - start.x, dy = event.clientY - start.y;
    start = null;
    if (Math.abs(dx) >= 45 && Math.abs(dx) > Math.abs(dy) * 1.5) render(index + (dx < 0 ? 1 : -1));
  });
  size.value = selectedSize; select.disabled = false; size.disabled = false;
  get('controls').hidden = false;
  render(0, false);
})();
