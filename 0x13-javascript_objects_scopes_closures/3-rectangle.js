#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) & (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let xCount = 0;
    const xList = [];
    while (xCount < this.width) {
      xList.push('X');
      xCount++;
    }
    const xString = xList.join('');

    let pCount = 0;
    while (pCount < this.height) {
      console.log(xString);
      pCount++;
    }
  }
}

module.exports = Rectangle;
