#!/usr/bin/node
const arg = process.argv[2];

if (!isNaN(arg)) {
  const arr = [];

  let b = 0;
  while (b < Number(arg)) {
    arr.push('X');
    b++;
  }
  const str = arr.join('');

  let i = 0;
  while (i < Number(arg)) {
    console.log(str);
    i++;
  }
} else {
  console.log('Missing size');
}
