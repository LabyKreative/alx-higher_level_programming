#!/usr/bin/node
const fs = require('fs');

const [fArg, sArg] = [
  fs.readFileSync(process.argv[2], 'utf8'),
  fs.readFileSync(process.argv[3], 'utf8')
];
fs.writeFileSync(process.argv[4], fArg + sArg);
