#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}

const fest = parseInt(process.argv[2]);
const sec = parseInt(process.argv[3]);

add(fest, sec);
