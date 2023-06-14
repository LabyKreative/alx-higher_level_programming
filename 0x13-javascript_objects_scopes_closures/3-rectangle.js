#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let x = 0; x < this.height; x++) {
      let y = '';
      for (let z = 0; z < this.width; z++) {
        y += 'X';
      }
      console.log(y);
    }
  }
}
module.exports = Rectangle;
