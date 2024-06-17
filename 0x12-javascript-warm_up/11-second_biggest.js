#!/usr/bin/node
const { argv } = require('node:process');

if (argv.length <= 2) {
  console.log(0);
} else if (argv.length === 3) {
  console.log(0);
} else {
  let argsList = [];
  let i = 2;
  while (i < argv.length) {
    argsList.push(Number(argv[i]));
    i++;
  }

  argsList = argsList.sort((a, b) => b - a);
  console.log(argsList[1]);
}
