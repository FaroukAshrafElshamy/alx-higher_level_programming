#!/usr/bin/node

const array = [];
for (let i = 2; i < (process.argv.length); i++) {
  array.push(process.argv[i]);
}
array.sort((a, b) => b - a);
if (isNaN(array[1]) || array[1] === '1') {
  console.log(0);
} else {
  console.log(array[1]);
}
