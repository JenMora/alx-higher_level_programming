#!/usr/bin/node
const Square5 = require('./5-square.js');
class Square extends Square5 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X' ) {
    if (c === undefined) {
    }
    for (let i = 0; i < this.height; i++) {
      let rectangle = '';
      for (let j = 0; j < this.width; j++) {
        rectangle += c;
      }
      console.log(rectangle);
    }
  }
}
module.exports = Square;
