#!/usr/bin/node
let printedArgs = 0;
exports.logMe = function (item) {
  console.log(`${printedArgs}: ${item}`);
  printedArgs++;
};
