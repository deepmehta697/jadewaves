/* Offline interaction checks; not a rendered mobile-browser test. */
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const source = fs.readFileSync(path.join(__dirname, '../../assets/salt/carousel.js'), 'utf8');
const entries = JSON.parse(fs.readFileSync(path.join(__dirname, '../../assets/salt/catalogue.json')));
function setup(reduced = false) {
  const nodes = new Map();
  function node(){return {value:'',textContent:'',hidden:true,maxLength:4000,attributes:{},listeners:{},
    classList:{add(){},remove(){}}, addEventListener(n,fn){this.listeners[n]=fn;}, setAttribute(n,v){this.attributes[n]=v;}};}
  const document = {getElementById(){return {textContent:JSON.stringify(entries)};},
    querySelector(s){if(!nodes.has(s))nodes.set(s,node());return nodes.get(s);}};
  vm.runInNewContext(source,{document,window:{matchMedia:()=>({matches:reduced})}});
  return {get:n=>document.querySelector(`[data-salt-${n}]`),notes:()=>document.querySelector('form[data-inquiry-form] [name="notes"]'),
    fire(n,event,data={}){document.querySelector(`[data-salt-${n}]`).listeners[event](data);}};
}
test('starts at the first supplied photo with manual controls and no initial announcement',()=>{
  const h=setup();assert.equal(h.get('photo').src,entries[0].src);assert.equal(h.get('name').textContent,'Non-iodized salt');
  assert.equal(h.get('select').disabled,false);assert.equal(h.get('controls').hidden,false);
  assert.equal(h.get('counter').textContent,'01 / 05');assert.equal(h.get('announcement').textContent,'');
});
test('all five choices align photo, alt text, dimensions, reference and counter',()=>{
  const h=setup();entries.forEach((e,i)=>{
    h.get('select').value=e.id;h.fire('select','change');assert.equal(h.get('photo').src,e.src);
    assert.equal(h.get('photo').alt,e.alt);assert.equal(h.get('photo').width,e.width);assert.equal(h.get('photo').height,e.height);
    assert.equal(h.get('name').textContent,e.name);assert.equal(h.get('counter').textContent,`0${i+1} / 05`);
    assert.ok(h.get('announcement').textContent.includes(e.name));
  });
});
test('manual arrows wrap and invalid choices do not corrupt the displayed sample',()=>{
  const h=setup();h.fire('prev','click');assert.equal(h.get('select').value,'view-5');h.fire('next','click');assert.equal(h.get('select').value,'view-1');
  h.get('select').value='wrong';h.fire('select','change');assert.equal(h.get('select').value,'view-1');
});
test('keyboard navigation leaves native controls alone',()=>{
  const h=setup();let prevented=0;
  const key=(key,control=false)=>h.fire('carousel','keydown',{key,target:{closest:()=>control},preventDefault(){prevented++;}});
  key('End');assert.equal(h.get('select').value,'view-5');key('ArrowRight');assert.equal(h.get('select').value,'view-1');
  key('ArrowRight',true);assert.equal(h.get('select').value,'view-1');key('Home');assert.equal(prevented,3);
});
test('horizontal touch changes photo but vertical, mouse and cancelled gestures do not',()=>{
  const h=setup();const p=(x,y,pointerType='touch')=>({clientX:x,clientY:y,pointerType});
  h.fire('frame','pointerdown',p(200,100));h.fire('frame','pointerup',p(100,103));assert.equal(h.get('select').value,'view-2');
  h.fire('frame','pointerdown',p(200,100));h.fire('frame','pointerup',p(190,250));assert.equal(h.get('select').value,'view-2');
  h.fire('frame','pointerdown',p(200,100));h.fire('frame','pointercancel');h.fire('frame','pointerup',p(100,100));assert.equal(h.get('select').value,'view-2');
  h.fire('frame','pointerdown',p(200,100,'mouse'));h.fire('frame','pointerup',p(100,100,'mouse'));assert.equal(h.get('select').value,'view-2');
});
test('sample action preserves typed notes and replaces only its own previous reference',()=>{
  const h=setup();h.notes().value='Iodine target to be confirmed';h.fire('enquire','click');
  assert.equal(h.notes().value,'Salt sample reference: Non-iodized salt\nIodine target to be confirmed');
  h.fire('next','click');h.fire('enquire','click');assert.equal(h.notes().value,'Salt sample reference: Raw salt\nIodine target to be confirmed');
  h.notes().value='x'.repeat(4000);h.fire('enquire','click');assert.equal(h.notes().value,'x'.repeat(4000));
});
test('reduced motion, error feedback and no automatic transmission',()=>{
  const h=setup(true);let animated=false;h.get('photo').classList.add=()=>{animated=true;};h.fire('photo','load');assert.equal(animated,false);
  h.fire('photo','error');assert.ok(h.get('announcement').textContent.includes('Photo unavailable'));
  assert.equal(/\bfetch\(|XMLHttpRequest|sendBeacon|gtag\(|setInterval|setTimeout/.test(source),false);
});
