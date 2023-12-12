#!/usr/bin/node
const arg = parseInt(process.argv[2]);
if (isNaN(arg) || arg === undefined) {
  console.log('Not a number');
} else {
  console.log('My Number:', arg);
}
