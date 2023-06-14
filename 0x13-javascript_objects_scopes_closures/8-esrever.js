#!/usr/bin/node
exports.esrever = function (list) {
  const rvl = [];
  for (let x = list.length - 1; x >= 0; x--) {
    rvl.push(list[x]);
  }
  return rvl;
};
