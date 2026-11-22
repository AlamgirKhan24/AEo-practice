const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');

const input = {value:'', listeners:{}, addEventListener(type,fn){this.listeners[type]=fn;}};
const form = {listeners:{}, addEventListener(type,fn){this.listeners[type]=fn;}};
const status = {textContent:''};
const cards = [
  {textContent:'Active recall guide', hidden:false},
  {textContent:'Flashcards guide', hidden:false},
  {textContent:'Revision plan guide', hidden:false}
];
const doc = {
  querySelector(sel){return {'[data-search]':input,'[data-search-form]':form,'[data-results]':status}[sel]||null;},
  querySelectorAll(sel){return sel==='[data-card]'?cards:[];}
};
vm.runInNewContext(fs.readFileSync('site/assets/site.js','utf8'),{document:doc});
assert.equal(typeof input.listeners.input,'function');
assert.equal(typeof form.listeners.submit,'function');

input.value='flashcard'; input.listeners.input();
assert.deepEqual(cards.map(x=>x.hidden),[true,false,true]);
assert.equal(status.textContent,'1 guide found');

input.value='no matching guide'; input.listeners.input();
assert.deepEqual(cards.map(x=>x.hidden),[true,true,true]);
assert.equal(status.textContent,'0 guides found');

input.value=''; input.listeners.input();
assert.deepEqual(cards.map(x=>x.hidden),[false,false,false]);
assert.equal(status.textContent,'Showing all 3 guides');

input.value='revision'; let prevented=false;
form.listeners.submit({preventDefault(){prevented=true;}});
assert.equal(prevented,true);
assert.deepEqual(cards.map(x=>x.hidden),[true,true,false]);
assert.equal(status.textContent,'1 guide found');
console.log('PASS: search filters matches, reports result counts, resets, and handles form submission.');
