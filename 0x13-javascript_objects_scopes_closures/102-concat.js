#!/usr/bin/node
const fs = require('fs');

try {
  const [fArg, sArg] = [
    fs.readFileSync(process.argv[2], 'utf8'),
    fs.readFileSync(process.argv[3], 'utf8')
  ];

  fs.writeFileSync(process.argv[4], fArg + sArg);
  console.log('Files concatenated successfully!');
} catch (error) {
  console.error('An error occurred:', error);
}
