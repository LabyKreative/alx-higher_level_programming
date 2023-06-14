#!/usr/bin/node
const argument = procress.argv[2];

if (argument === undefined) {
  console.log("No argument");
} else {
  console.log(argument);
}
