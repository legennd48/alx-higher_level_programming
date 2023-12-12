#!/usr/bin/node
function factoria (n) {
  if (isNaN(n) || n < 0) {
    return 1;
  }
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factoria(n - 1);
  }
}
const num = parseInt(process.argv[2]);
const result = factoria(num);
console.log(result);
