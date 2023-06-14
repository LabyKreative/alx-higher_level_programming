#!/usr/bin/node
const size = Math.floor(Number(process.argv[2]));
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < size; x++) {
    let prtsq = '';
    for (let y = 0; y < size; y++) prtsq += 'X';
    console.log(prtsq);
  }
}
