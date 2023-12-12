#!/usr/bin/node

const inputFile1 = process.argv[2];
const inputFile2 = process.argv[3];
const outputFile = process.argv[4];
const fs = require('fs');

const textFromInputFile1 = fs.readFileSync(inputFile1, 'utf8');
const textFromInputFile2 = fs.readFileSync(inputFile2, 'utf8');
const concatenatedText = textFromInputFile1 + textFromInputFile2;

fs.writeFileSync(outputFile, concatenatedText);
