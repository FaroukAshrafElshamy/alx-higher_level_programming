#!/usr/bin/node

const array = [];
for (let i = 2; i < process.argv.length; i++) {
  array.push(process.argv[i]);
}
array.sort();
if (isNaN(array[1]) || array[1] === '1') {
  console.log(0);
} else {
  console.log(array[array.length - 2]);
}
