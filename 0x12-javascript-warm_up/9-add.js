#!/usr/bin/node
function add (x, y) {
  return x + y;
}
console.log(add(Number(process.argv[2]), Number(process.argv[3])));
