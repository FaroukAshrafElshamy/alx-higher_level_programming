#!/usr/bin/node
let i = 0;
const list = require('./100-data').list;
const list2 = list.map(num => num * (i++));
console.log(list);
console.log(list2);
