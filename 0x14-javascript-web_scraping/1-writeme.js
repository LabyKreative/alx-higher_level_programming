#!/usr/bin/node
// a script that writes a string to a file.
const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], error => {
  if (error) console.log(error);
});
