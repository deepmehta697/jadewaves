/* Manual sample-reference navigation. No submission or lead event is sent. */
(() => {
  'use strict';
  const entries = JSON.parse(document.getElementById('salt-gallery-data').textContent);
  const get = name => document.querySelector(`[data-salt-${name}]`);
  const photo = get('photo'), select = get('select'), frame = get('frame');
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  let index = 0, start = null, inserted = '';
  const render = (next, announce = true) => {
    index = (next + entries.length) % entries.length;
    const entry = entries[index];
    select.value = entry.id;
    photo.classList.remove('is-changing');
    photo.src = entry.src; photo.alt = entry.alt;
    photo.width = entry.width; photo.height = entry.height;
    frame.setAttribute('aria-label', `${index + 1} of ${entries.length}: ${entry.name}`);
    get('name').textContent = entry.name;
    get('counter').textContent = `${String(index + 1).padStart(2, '0')} / ${String(entries.length).padStart(2, '0')}`;
    if (announce) get('announcement').textContent = `${entry.name}. ${index + 1} of ${entries.length}.`;
  };
  select.addEventListener('change', () => {
    const next = entries.findIndex(entry => entry.id === select.value);
    if (next >= 0) render(next); else select.value = entries[index].id;
  });
  get('prev').addEventListener('click', () => render(index - 1));
  get('next').addEventListener('click', () => render(index + 1));
  photo.addEventListener('load', () => { if (!reduced.matches) photo.classList.add('is-changing'); });
  photo.addEventListener('error', () => { get('announcement').textContent = 'Photo unavailable. Choose another sample view or contact the export desk.'; });
  get('carousel').addEventListener('keydown', event => {
    if (event.target.closest('select,button,a,input,textarea')) return;
    const next = {ArrowLeft:index-1, ArrowRight:index+1, Home:0, End:entries.length-1}[event.key];
    if (next !== undefined) { event.preventDefault(); render(next); }
  });
  frame.addEventListener('pointerdown', event => {
    if (event.pointerType === 'touch') start = {x:event.clientX, y:event.clientY};
  });
  frame.addEventListener('pointercancel', () => { start = null; });
  frame.addEventListener('pointerup', event => {
    if (!start || event.pointerType !== 'touch') return;
    const dx = event.clientX-start.x, dy = event.clientY-start.y; start = null;
    if (Math.abs(dx) >= 45 && Math.abs(dx) > Math.abs(dy)*1.5) render(index+(dx < 0 ? 1 : -1));
  });
  get('enquire').addEventListener('click', () => {
    const notes = document.querySelector('form[data-inquiry-form] [name="notes"]');
    if (!notes) return;
    const prefix = `Salt sample reference: ${entries[index].name}\n`;
    const previous = inserted && notes.value.startsWith(inserted) ? notes.value.slice(inserted.length) : notes.value;
    if (notes.maxLength > 0 && prefix.length+previous.length > notes.maxLength) return;
    notes.value = prefix+previous; inserted = prefix;
  });
  select.disabled = false; get('controls').hidden = false; render(0, false);
})();
