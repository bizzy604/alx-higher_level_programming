#!/usr/bin/node
const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }

    let cCount = 0;
    const cList = [];
    while (cCount < this.height) {
      cList.push(c);
      cCount++;
    }
    const cString = cList.join('');

    let pCount = 0;
    while (pCount < this.width) {
      console.log(cString);
      pCount++;
    }
  }
}

module.exports = Square;
