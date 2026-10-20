/* Offline interaction tests, not rendered-browser or touch-device verification. */
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const source = fs.readFileSync(path.join(__dirname, '../../assets/colour-coated-sand/coated-sand.js'), 'utf8');
const catalogue = JSON.parse(fs.readFileSync(path.join(__dirname, '../../assets/colour-coated-sand/catalogue.json')));

function setup(reduced = false) {
  const entries = catalogue.map(e => ({...e, src:`assets/colour-coated-sand/${e.id}.webp`, width:720, height:740}));
  const nodes = new Map();
  function node() {
    return {value:'',textContent:'',hidden:true,attributes:{},listeners:{},href:'',
      classes:new Set(),classList:{add(){},remove(){}},
      addEventListener(event,fn){this.listeners[event]=fn;},
      setAttribute(name,value){this.attributes[name]=value;}
    };
  }
  const document = {
    getElementById(){return {textContent:JSON.stringify(entries)};},
    querySelector(selector){if(!nodes.has(selector))nodes.set(selector,node());return nodes.get(selector);}
  };
  vm.runInNewContext(source,{document,window:{matchMedia:()=>({matches:reduced})}});
  return {entries,get:s=>document.querySelector(s),fire(s,event,data={}){nodes.get(s).listeners[event](data);}};
}

test('starts at Red with one contextual photo and visible manual controls',()=>{
  const h=setup();
  assert.equal(h.get('[data-sand-select]').value,'red');
  assert.equal(h.get('[data-sand-select]').disabled,false);
  assert.equal(h.get('[data-sand-photo]').src,'assets/colour-coated-sand/red.webp');
  assert.equal(h.get('[data-sand-counter]').textContent,'01 / 06');
  assert.equal(h.get('[data-sand-controls]').hidden,false);
  assert.equal(h.get('[data-sand-announcement]').textContent,'');
});
test('all six selections align photo, name, index, announcement and email',()=>{
  const h=setup();
  h.entries.forEach((entry,index)=>{
    h.get('[data-sand-select]').value=entry.id;h.fire('[data-sand-select]','change');
    assert.equal(h.get('[data-sand-photo]').src,entry.src);
    assert.equal(h.get('[data-sand-name]').textContent,entry.name);
    assert.equal(h.get('[data-sand-counter]').textContent,`${String(index+1).padStart(2,'0')} / 06`);
    assert.ok(h.get('[data-sand-announcement]').textContent.includes(entry.name));
    assert.ok(h.get('[data-sand-announcement]').textContent.includes('0.5–1 mm'));
    const link=new URL(h.get('[data-sand-email]').href);
    assert.equal(link.protocol,'mailto:');assert.equal(link.pathname,'deep@jadewavesenterprise.com');
    assert.ok(link.searchParams.get('body').includes(entry.name));
    assert.ok(link.searchParams.get('body').includes(entry.size));
  });
});
test('manual arrows wrap in both directions',()=>{
  const h=setup();h.fire('[data-sand-prev]','click');
  assert.equal(h.get('[data-sand-select]').value,'mixed');
  h.fire('[data-sand-next]','click');assert.equal(h.get('[data-sand-select]').value,'red');
});
test('Arrow keys and Home/End navigate without stealing select keys',()=>{
  const h=setup();let prevented=0;
  const key=(key,control=false)=>h.fire('[data-sand-carousel]','keydown',{key,target:{closest:()=>control},preventDefault(){prevented++;}});
  key('End');assert.equal(h.get('[data-sand-select]').value,'mixed');
  key('ArrowRight');assert.equal(h.get('[data-sand-select]').value,'red');
  key('ArrowLeft');assert.equal(h.get('[data-sand-select]').value,'mixed');
  key('Home');assert.equal(h.get('[data-sand-select]').value,'red');
  key('ArrowRight',true);assert.equal(h.get('[data-sand-select]').value,'red');
  assert.equal(prevented,4);
});
test('horizontal touch changes colour; vertical scroll and cancelled touch do not',()=>{
  const h=setup();const p=(x,y)=>({pointerType:'touch',clientX:x,clientY:y});
  h.fire('[data-sand-frame]','pointerdown',p(200,100));h.fire('[data-sand-frame]','pointerup',p(100,105));
  assert.equal(h.get('[data-sand-select]').value,'pink');
  h.fire('[data-sand-frame]','pointerdown',p(200,100));h.fire('[data-sand-frame]','pointerup',p(190,200));
  assert.equal(h.get('[data-sand-select]').value,'pink');
  h.fire('[data-sand-frame]','pointerdown',p(200,100));h.fire('[data-sand-frame]','pointercancel');h.fire('[data-sand-frame]','pointerup',p(100,100));
  assert.equal(h.get('[data-sand-select]').value,'pink');
});
test('unknown colour does not corrupt the selected photo',()=>{
  const h=setup();h.get('[data-sand-select]').value='not-a-colour';h.fire('[data-sand-select]','change');
  assert.equal(h.get('[data-sand-photo]').src,'assets/colour-coated-sand/red.webp');
});
test('no network submission, analytics event, autoplay or timer is present',()=>{
  assert.equal(/\bfetch\(|XMLHttpRequest|sendBeacon|gtag\(|setInterval|setTimeout/.test(source),false);
});
test('reduced-motion mode suppresses the image transition',()=>{
  const h=setup(true);let animated=false;
  h.get('[data-sand-photo]').classList.add=()=>{animated=true;};
  h.fire('[data-sand-photo]','load');assert.equal(animated,false);
});
