/* Offline DOM-contract tests, not rendered device/browser QA. */
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const root=path.resolve(__dirname,'../..');
const source = fs.readFileSync(path.join(root, 'assets/decorative-products/carousel.js'), 'utf8');
const products = JSON.parse(fs.readFileSync(path.join(root, 'templates/decorative-products.json')));

function setup(product, reduced = false) {
  const data = {...product, entries: JSON.parse(fs.readFileSync(path.join(root, 'assets', product.slug, 'catalogue.json')))};
  const coloursPath=path.join(root,'assets',product.slug,'colours.json');
  data.colours=fs.existsSync(coloursPath)?JSON.parse(fs.readFileSync(coloursPath)):[];
  const nodes = new Map();
  function node() {
    return {value:'', textContent:'', hidden:true, attributes:{}, listeners:{}, href:'',
      classList:{add(){},remove(){}},
      addEventListener(event,fn){this.listeners[event]=fn;},
      setAttribute(name,value){this.attributes[name]=value;}};
  }
  const colourNodes=data.colours.map((colour,index)=>Object.assign(node(),{value:colour.id,checked:index===0}));
  const document = {
    getElementById(){return {textContent:JSON.stringify(data)};},
    querySelectorAll(){return colourNodes;},
    querySelector(selector){if(!nodes.has(selector))nodes.set(selector,node());return nodes.get(selector);}
  };
  vm.runInNewContext(source, {document, window:{matchMedia:()=>({matches:reduced})}});
  const get = name => document.querySelector(`[data-product-${name}]`);
  return {data, get, colourNodes, fire(name,event,arg={}){get(name).listeners[event](arg);}};
}

for (const product of products) {
  test(`${product.name}: starts with one contextual photo, selectors and visible manual controls`,()=>{
    const h=setup(product), first=h.data.entries[0];
    assert.equal(h.get('select').value,first.id); assert.equal(h.get('photo').src,first.src);
    assert.equal(h.get('photo').alt,first.alt); assert.equal(h.get('size').value,product.sizes[0]);
    assert.equal(h.get('select').disabled,false); assert.equal(h.get('size').disabled,false);
    assert.equal(h.get('controls').hidden,false); assert.equal(h.get('announcement').textContent,'');
  });
  test(`${product.name}: every photo and grade combination keeps email context aligned`,()=>{
    const h=setup(product);
    h.data.entries.forEach((entry,index)=>{
      h.get('select').value=entry.id; h.fire('select','change');
      assert.equal(h.get('photo').src,entry.src); assert.equal(h.get('photo').width,entry.width);
      assert.equal(h.get('photo').height,entry.height); assert.equal(h.get('name').textContent,entry.name);
      assert.equal(h.get('counter').textContent,`${String(index+1).padStart(2,'0')} / ${String(h.data.entries.length).padStart(2,'0')}`);
      product.sizes.forEach(size=>{
        h.get('size').value=size; h.fire('size','change');
        const link=new URL(h.get('email').href), body=link.searchParams.get('body');
        assert.equal(link.protocol,'mailto:'); assert.equal(link.pathname,'deep@jadewavesenterprise.com');
        assert.ok(body.includes(product.name.toLowerCase())); assert.ok(body.includes(entry.name)); assert.ok(body.includes(size));
        assert.ok(h.get('announcement').textContent.includes(size));
      });
    });
  });
  test(`${product.name}: arrows wrap and preserve selected grade`,()=>{
    const h=setup(product); h.get('size').value=product.sizes[2];h.fire('size','change');
    h.fire('prev','click'); assert.equal(h.get('select').value,h.data.entries.at(-1).id);
    h.fire('next','click'); assert.equal(h.get('select').value,h.data.entries[0].id);
    assert.equal(h.get('size').value,product.sizes[2]); assert.ok(decodeURIComponent(h.get('email').href).includes(product.sizes[2]));
  });
  test(`${product.name}: keyboard navigation does not steal native select or link keys`,()=>{
    const h=setup(product);let prevented=0;
    const key=(key,control=false)=>h.fire('carousel','keydown',{key,target:{closest:()=>control},preventDefault(){prevented++;}});
    key('End'); assert.equal(h.get('select').value,h.data.entries.at(-1).id);
    key('ArrowRight'); assert.equal(h.get('select').value,h.data.entries[0].id);
    key('ArrowLeft'); assert.equal(h.get('select').value,h.data.entries.at(-1).id);
    key('Home'); key('ArrowRight',true); key('Tab'); assert.equal(h.get('select').value,h.data.entries[0].id); assert.equal(prevented,4);
  });
  test(`${product.name}: horizontal touch works without hijacking vertical scroll`,()=>{
    const h=setup(product), p=(x,y)=>({pointerType:'touch',clientX:x,clientY:y});
    h.fire('frame','pointerdown',p(200,100)); h.fire('frame','pointerup',p(100,105));
    assert.equal(h.get('select').value,h.data.entries[1].id);
    h.fire('frame','pointerdown',p(200,100)); h.fire('frame','pointerup',p(190,200));
    assert.equal(h.get('select').value,h.data.entries[1].id);
    h.fire('frame','pointerdown',p(200,100)); h.fire('frame','pointercancel'); h.fire('frame','pointerup',p(100,100));
    assert.equal(h.get('select').value,h.data.entries[1].id);
  });
  test(`${product.name}: invalid selector values cannot pollute the enquiry`,()=>{
    const h=setup(product), before=h.get('email').href;
    h.get('select').value='not-a-finish';h.fire('select','change');
    h.get('size').value='not-a-size';h.fire('size','change');
    assert.equal(h.get('select').value,h.data.entries[0].id);assert.equal(h.get('size').value,product.sizes[0]);assert.equal(h.get('email').href,before);
  });
  test(`${product.name}: respects reduced motion and announces an image failure`,()=>{
    const h=setup(product,true);let animated=false;
    h.get('photo').classList.add=()=>{animated=true;};h.fire('photo','load');assert.equal(animated,false);
    h.fire('photo','error');assert.ok(h.get('announcement').textContent.includes('Photo unavailable'));
  });
}
test('all 25 grout colours preserve independent photo/grade selection and update both email drafts',()=>{
  const h=setup(products.find(p=>p.slug==='grout-sand'));
  assert.equal(h.colourNodes.length,25);
  h.get('size').value='150 mesh';h.fire('size','change');
  h.fire('next','click');
  const photo=h.get('photo').src;
  h.data.colours.forEach((colour,index)=>{
    const radio=h.colourNodes[index];assert.equal(radio.disabled,false);
    radio.checked=true;radio.listeners.change();
    assert.equal(h.get('selected-colour').textContent,colour.name);
    assert.equal(h.get('colour-email').href,h.get('email').href);
    const link=new URL(h.get('email').href),body=link.searchParams.get('body');
    assert.ok(body.includes('Requested colour: '+colour.name));assert.ok(body.includes('150 mesh'));
    assert.ok(link.searchParams.get('subject').includes(colour.name));
    assert.equal(h.colourNodes.filter(r=>r.checked).length,1);
    assert.equal(h.get('photo').src,photo);
    assert.ok(h.get('announcement').textContent.includes(colour.name));
  });
});
test('an invalid grout radio value cannot contaminate an enquiry',()=>{
  const h=setup(products.find(p=>p.slug==='grout-sand')),before=h.get('email').href;
  h.colourNodes[1].value='unknown-colour';h.colourNodes[1].checked=true;h.colourNodes[1].listeners.change();
  assert.equal(h.get('email').href,before);assert.equal(h.get('selected-colour').textContent,'White');
  assert.equal(h.colourNodes[0].checked,true);assert.equal(h.colourNodes[1].checked,false);
});
test('carousel never transmits an inquiry, records a lead, autoplays or uses timers',()=>{
  assert.equal(/\bfetch\(|XMLHttpRequest|sendBeacon|gtag\(|setInterval|setTimeout/.test(source),false);
});
