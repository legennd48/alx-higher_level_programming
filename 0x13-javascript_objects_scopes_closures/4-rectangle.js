#!/usr/bin/node

class Rectangle {
  // initialisation
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // print method
  print () {
    for (let i = 1; i <= this.height; i++) {
      const ch = 'X';
      console.log(ch.repeat(this.width));
    }
  }

  // exchanges wisth and height of the rectangle
  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  // multiplies width and height of rectangle by 2
  double () {
    this.height *= 2;
    this.width *= 2;
  }
}

module.exports = Rectangle;
