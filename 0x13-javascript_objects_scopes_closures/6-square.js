#!/usr/bin/node

const Square1 = require('./5-square.js');

class Square extends Square1 {
  charPrint (c) {
    let ch;

    if (c === undefined) {
      ch = 'X';
    } else {
      ch = c;
    }
    for (let i = 1; i <= this.height; i++) {
      console.log(ch.repeat(this.width));
    }
  }
}
module.exports = Square;
