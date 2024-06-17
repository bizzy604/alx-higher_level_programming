#!/usr/bin/node
const arg = process.argv[2];

if (Number.isInteger(Number(arg))) {
  let i = 0;
  while (i < parseInt(arg)) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
