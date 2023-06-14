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

  rotate () {
    const rt = this.width;
    this.width = this.height;
    this.height = rt;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
