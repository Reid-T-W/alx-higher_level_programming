#!/usr/bin/node
const firstSquare = require('./5-square');

class Square extends firstSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (typeof c === 'undefined') {
      super.print();
    } else {
      let concat = '';
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          concat = concat + 'C';
        }
        console.log(concat);
        concat = '';
      }
    }
  }
}
module.exports = Square;
