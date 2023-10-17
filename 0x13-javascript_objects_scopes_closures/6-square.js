#!/usr/bin/node
const Square5 = require('./5-rectangle');

class Square extends Square5 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let s = 0; s < this.width; s++) {
        let sqr = ' ';
	for (let t = 0; t < this.height; t++) {
	  sqr += c;
	}
        console.log(sqr);
      }
    }
  }
}

module.exports = Square;
