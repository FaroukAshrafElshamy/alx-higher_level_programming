#!/usr/bin/node
const fs = require('fs');
const First = fs.readFileSync(process.argv[2]);
const Second = fs.readFileSync(process.argv[3]);
fs.writeFileSync(process.argv[4], First + Second);
