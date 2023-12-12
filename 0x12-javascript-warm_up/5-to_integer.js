#!/usr/bin/node
const arg = Number(process.argv[2]);
if (isNaN(arg)) {
  console.log('Not a number');
} else {
  console.log('My Number:', Math.floor(arg));
}
