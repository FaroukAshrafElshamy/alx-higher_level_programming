#!/usr/bin/node

function fact (number) {
  if (number === 1) {
    return 1;
  } else {
    return number * fact(number - 1);
  }
}

const digit = Number(process.argv[2]);
if (isNaN(digit)) {
  console.log(1);
} else {
  console.log(fact(digit));
}
