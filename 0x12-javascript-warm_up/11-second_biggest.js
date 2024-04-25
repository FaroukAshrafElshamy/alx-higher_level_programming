#!/usr/bin/node
const array = [];
for (let i = 2; i < (process.argv.length); i++) {
  array.push(process.argv[i]);
}
array.sort((a, b) => b - a);
if (array.length > 1) {
  console.log(array[1]);
} else {
  console.log(0);
}
