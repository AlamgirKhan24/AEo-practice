// Minimal dependency-free UI smoke test using fake DOM controls.
const fs = require('fs');
const vm = require('vm');
const path = require('path');
const html = fs.readFileSync(path.join(__dirname, '..', 'index.html'), 'utf8');
const script = html.match(/<script>([\s\S]*?)<\/script>/)?.[1];
if (!script) throw new Error('Inline app script not found');
const els = new Map();
function element(id='') { return {id,value:'',textContent:'',innerHTML:'',dataset:{},style:{},classList:{toggle(){}},setAttribute(){},click(){},hasAttribute(){return false},getAttribute(){return null},closest(){return null}} }
const listeners = {};
const document = {
  querySelector(sel) { const id=sel.startsWith('#')?sel.slice(1):sel; if(!els.has(id))els.set(id,element(id)); return els.get(id); },
  querySelectorAll() { return []; },
  addEventListener(type,fn) { listeners[type]=fn; },
  createElement() { return element('download'); }
};
const store = new Map();
const localStorage = {getItem:k=>store.get(k)||null,setItem:(k,v)=>store.set(k,v),removeItem:k=>store.delete(k)};
const context = {document,localStorage,confirm:()=>true,Blob,URL:{createObjectURL:()=>'',revokeObjectURL(){}},setTimeout,Date,JSON,console};
vm.runInNewContext(script,context,{timeout:1000});
const assert=(ok,msg)=>{if(!ok)throw new Error(msg)};
assert(document.querySelector('#statCoverage').textContent==='0 / 27','initial rubric coverage');
assert(document.querySelector('#statScore').textContent==='—','unassessed score should be blank');
listeners.input({target:{dataset:{crit:'C1',key:'rating'},value:'4'}});
assert(String(document.querySelector('#statScore').textContent)==='100','single 4/4 assessment should normalize to 100');
assert(document.querySelector('#statCoverage').textContent==='1 / 27','assessed count after one rating');
listeners.click({target:{id:'addObservation',closest:()=>null,hasAttribute:()=>false}});
const saved=JSON.parse(store.get('answerwise_audit_v1'));
assert(saved.observations.length===1,'manual observation row is saved');
document.querySelector('#schemaInput').value='{"@context":"https://schema.org","@type":"Organization","name":"Example"}';
listeners.click({target:{id:'validateSchema',closest:()=>null,hasAttribute:()=>false}});
assert(document.querySelector('#schemaStatus').textContent.startsWith('Valid JSON syntax'),'valid JSON-LD syntax accepted');
document.querySelector('#schemaInput').value='{broken';
listeners.click({target:{id:'validateSchema',closest:()=>null,hasAttribute:()=>false}});
assert(document.querySelector('#schemaStatus').textContent.startsWith('Could not parse:'),'invalid JSON rejected');
console.log('PASS: initial state, score normalization, coverage, observation persistence, JSON syntax accept/reject');
