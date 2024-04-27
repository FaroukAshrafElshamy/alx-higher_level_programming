#!/usr/bin/node
let i = 0;
exports.logMe = function (item) {
  console.log(`${i++}: ${item}`);
};
const logMe = require('./9-logme').logMe;
