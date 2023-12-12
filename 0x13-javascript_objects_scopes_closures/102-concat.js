#!/usr/bin/node
const fs = require('fs');

const txt1 = fs.readFileSync(process.argv[2]).toString();
const txt2 = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], txt1 + txt2);
