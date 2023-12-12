#!/usr/bin/node

let fileA = process.argv[2];
let fileB = process.argv[3];
let fileC = process.argv[4];
const fs = require('fs');

let contentA = fs.readFileSync(fileA, 'utf8');
let contentB = fs.readFileSync(fileB, 'utf8');

fs.writeFileSync(fileC, contentA + contentB);
