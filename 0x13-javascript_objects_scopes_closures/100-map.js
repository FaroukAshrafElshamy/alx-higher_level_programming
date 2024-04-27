#!/usr/bin/node
const list = require('./100-data.js');
const list2 = list.map(num => num * num.indexOf());
console.log(list);
console.log(list2);
