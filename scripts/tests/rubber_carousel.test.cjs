/* Offline state/interaction tests, not rendered-browser verification. */
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const source = fs.readFileSync(path.join(__dirname, '../../assets/rubber-granules/carousel.js'), 'utf8');
const entries = JSON.parse(fs.readFileSync(path.join(__dirname, '../../assets/rubber-granules/catalogue.json')));
function setup(reduced = false) {
  const nodes = new Map();
  function node() { return {value:'', textContent:'', hidden:true, maxLength:4000, attributes:{}, listeners:{},
    classList:{add(){},remove(){}}, addEventListener(name, fn){this.listeners[name]=fn;}, setAttribute(name,value){this.attributes[name]=value;}}; }
  const document = {getElementById(){return {textContent:JSON.stringify(entries)};},
    querySelector(selector){if(!nodes.has(selector))nodes.set(selector,node());return nodes.get(selector);}};
  vm.runInNewContext(source, {document, window:{matchMedia:()=>({matches:reduced})}});
  return {get: name => document.querySelector(`[data-rubber-${name}]`),
    notes:()=>document.querySelector('form[data-inquiry-form] [name="notes"]'),
    fire(name,event,data={}){document.querySelector(`[data-rubber-${name}]`).listeners[event](data);}};
}
test('starts at the supplied black photo, no RAL invented, manual controls enabled',()=>{
  const h=setup();
  assert.equal(h.get('photo').src,'assets/rubber-granules/black.webp');
  assert.equal(h.get('select').value,'black');assert.equal(h.get('select').disabled,false);
  assert.equal(h.get('counter').textContent,'01 / 23');assert.equal(h.get('controls').hidden,false);
  assert.equal(h.get('reference').hidden,true);assert.equal(h.get('announcement').textContent,'');
});
test('all 23 selections align name, reference, image, size, counter and announcement',()=>{
  const h=setup();
  entries.forEach((e,i)=>{
    h.get('select').value=e.id;h.fire('select','change');
    assert.equal(h.get('photo').src,e.src);assert.equal(h.get('photo').alt,e.alt);
    assert.equal(h.get('photo').width,e.width);assert.equal(h.get('photo').height,e.height);
    assert.equal(h.get('name').textContent,e.name);
    assert.equal(h.get('reference').textContent,e.ral ? `Chart reference: RAL ${e.ral}` : '');
    assert.equal(h.get('counter').textContent,`${String(i+1).padStart(2,'0')} / 23`);
    assert.ok(h.get('announcement').textContent.includes(e.name));
  });
});
test('previous and next wrap; invalid selection restores the current colour',()=>{
  const h=setup();h.fire('prev','click');assert.equal(h.get('select').value,'dark-grey');
  h.fire('next','click');assert.equal(h.get('select').value,'black');
  h.get('select').value='bad';h.fire('select','change');assert.equal(h.get('select').value,'black');
});
test('keyboard moves on the carousel, not inside native fields or buttons',()=>{
  const h=setup();let prevented=0;
  const key=(key,control=false)=>h.fire('carousel','keydown',{key,target:{closest:()=>control},preventDefault(){prevented++;}});
  key('End');assert.equal(h.get('select').value,'dark-grey');
  key('ArrowRight');assert.equal(h.get('select').value,'black');
  key('Home');key('ArrowRight',true);assert.equal(h.get('select').value,'black');assert.equal(prevented,3);
});
test('horizontal touch navigates; vertical, mouse, and cancelled gestures do not',()=>{
  const h=setup();const p=(x,y,pointerType='touch')=>({clientX:x,clientY:y,pointerType});
  h.fire('frame','pointerdown',p(200,100));h.fire('frame','pointerup',p(100,103));assert.equal(h.get('select').value,'white');
  h.fire('frame','pointerdown',p(200,100));h.fire('frame','pointerup',p(190,250));assert.equal(h.get('select').value,'white');
  h.fire('frame','pointerdown',p(200,100));h.fire('frame','pointercancel');h.fire('frame','pointerup',p(100,100));assert.equal(h.get('select').value,'white');
  h.fire('frame','pointerdown',p(200,100,'mouse'));h.fire('frame','pointerup',p(100,100,'mouse'));assert.equal(h.get('select').value,'white');
});
test('sample action prefills selection without overwriting notes or duplicating its own prefix',()=>{
  const h=setup();h.notes().value='Keep my grading requirement';
  h.fire('enquire','click');assert.equal(h.notes().value,'Colour reference: Black\nKeep my grading requirement');
  h.fire('enquire','click');assert.equal(h.notes().value,'Colour reference: Black\nKeep my grading requirement');
  h.fire('next','click');h.fire('enquire','click');
  assert.equal(h.notes().value,'Colour reference: White (chart RAL 9010)\nKeep my grading requirement');
});
test('manual edits and maximum-length notes are preserved',()=>{
  const h=setup();h.notes().value='x'.repeat(4000);h.fire('enquire','click');assert.equal(h.notes().value,'x'.repeat(4000));
  h.notes().value='Black and white samples';h.fire('enquire','click');
  h.notes().value='My edit\n'+h.notes().value;h.fire('next','click');h.fire('enquire','click');assert.ok(h.notes().value.includes('My edit'));
});
test('reduced motion, image error feedback, and no automatic submissions/timers',()=>{
  const h=setup(true);let animated=false;h.get('photo').classList.add=()=>{animated=true;};h.fire('photo','load');assert.equal(animated,false);
  h.fire('photo','error');assert.ok(h.get('announcement').textContent.includes('Photo unavailable'));
  assert.equal(/\bfetch\(|XMLHttpRequest|sendBeacon|gtag\(|setInterval|setTimeout/.test(source),false);
});
