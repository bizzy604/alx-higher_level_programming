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

  rotate () {
    const wTemp = this.width;
    this.width = this.height;
    this.height = wTemp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
