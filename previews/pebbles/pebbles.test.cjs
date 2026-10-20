/* Offline interaction contracts; these are not a rendered-browser test. */
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const path = require('node:path');
const source = fs.readFileSync(path.join(__dirname, 'pebbles.js'), 'utf8');
const catalogue = JSON.parse(fs.readFileSync(path.join(__dirname, 'catalogue.json')));

function setup(reduced = false) {
  const entries = catalogue.map(e => ({...e, src:`media/${e.id}.webp`, width:500, height:400, packing:e.packing || '25 kg bags'}));
  const elements = new Map();
  function element() {
    return {value:'', textContent:'', hidden:true, href:'', listeners:{}, attributes:{},
      classList:{add(){}, remove(){}},
      addEventListener(name, callback) { this.listeners[name] = callback; },
      setAttribute(name, value) { this.attributes[name] = value; },
      replaceChildren(...options) { this.options = options; this.value = options[0].value; }
    };
  }
  const document = {
    getElementById() { return {textContent:JSON.stringify(entries)}; },
    querySelector(selector) { if (!elements.has(selector)) elements.set(selector, element()); return elements.get(selector); }
  };
  vm.runInNewContext(source, { document, window:{matchMedia:()=>({matches:reduced})}, Option:function(text,value){ this.text=text; this.value=value; } });
  return { entries, get:s=>elements.get(s), fire(s,event,data={}) { elements.get(s).listeners[event](data); } };
}
test('starts with one contextual image and the white size options', () => {
  const h=setup();
  assert.equal(h.get('[data-photo]').src, 'media/white-polished.webp');
  assert.equal(h.get('[data-controls]').hidden, false);
  assert.equal(h.get('[data-variant]').value, 'white-polished');
  assert.equal(h.get('[data-enquiry-size]').value, '8–18 mm');
  assert.equal(h.get('[data-announcement]').textContent, '');
});
test('previous and next wrap around the collection', () => {
  const h=setup();
  h.fire('[data-previous]','click');
  assert.equal(h.get('[data-variant]').value, h.entries.at(-1).id);
  h.fire('[data-next]','click');
  assert.equal(h.get('[data-variant]').value, 'white-polished');
});
test('every selection keeps photo, sizes, brief, counter and email aligned', () => {
  const h=setup();
  h.entries.forEach((entry, i) => {
    h.get('[data-variant]').value=entry.id;
    h.fire('[data-variant]','change');
    assert.equal(h.get('[data-name]').textContent,entry.name);
    assert.equal(h.get('[data-photo]').src,entry.src);
    assert.equal(h.get('[data-brief-name]').textContent,entry.name);
    assert.equal(h.get('[data-sizes]').textContent,entry.sizes.join(' · '));
    assert.equal(h.get('[data-enquiry-size]').options.length,entry.sizes.length);
    assert.equal(h.get('[data-photo-index]').textContent,`${String(i+1).padStart(2,'0')} / ${h.entries.length}`);
    const link=new URL(h.get('[data-email]').href);
    assert.equal(link.pathname,'deep@jadewavesenterprise.com');
    assert.ok(link.searchParams.get('body').includes(entry.name));
    assert.ok(link.searchParams.get('body').includes(entry.sizes[0]));
  });
});
test('size changes update email draft without submission or transmission', () => {
  const h=setup();
  h.get('[data-enquiry-size]').value='30–60 mm';
  h.fire('[data-enquiry-size]','change');
  assert.ok(new URL(h.get('[data-email]').href).searchParams.get('body').includes('30–60 mm'));
  assert.equal(/\bfetch\(|XMLHttpRequest|sendBeacon|gtag\(/.test(source),false);
});
test('arrow keys and Home/End navigate, but select keys stay native', () => {
  const h=setup(); let prevented=0;
  const key=(value,native=false)=>h.fire('[data-carousel]','keydown',{key:value,target:{closest:()=>native},preventDefault(){prevented++;}});
  key('End'); assert.equal(h.get('[data-variant]').value,h.entries.at(-1).id);
  key('ArrowRight'); assert.equal(h.get('[data-variant]').value,'white-polished');
  key('ArrowLeft'); assert.equal(h.get('[data-variant]').value,h.entries.at(-1).id);
  key('Home'); assert.equal(h.get('[data-variant]').value,'white-polished');
  key('ArrowRight',true); assert.equal(h.get('[data-variant]').value,'white-polished');
  assert.equal(prevented,4);
});
test('horizontal touch swipes navigate; vertical gestures do not', () => {
  const h=setup();
  const touch=(x,y)=>({pointerType:'touch',clientX:x,clientY:y});
  h.fire('[data-photo-frame]','pointerdown',touch(200,150));
  h.fire('[data-photo-frame]','pointerup',touch(100,155));
  assert.equal(h.get('[data-variant]').value,'black-polished');
  h.fire('[data-photo-frame]','pointerdown',touch(200,150));
  h.fire('[data-photo-frame]','pointerup',touch(190,250));
  assert.equal(h.get('[data-variant]').value,'black-polished');
});
test('invalid dropdown input does not corrupt the current selection', () => {
  const h=setup(true);
  h.get('[data-variant]').value='missing'; h.fire('[data-variant]','change');
  assert.equal(h.get('[data-name]').textContent,'White polished pebbles');
});
