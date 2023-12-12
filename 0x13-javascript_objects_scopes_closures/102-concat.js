#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 5) {
  console.log('Usage: concatFiles.js <sourceFilePath1> <sourceFilePath2> <destinationFilePath>');
  process.exit(1);
}

const sourceFilePath1 = process.argv[2];
const sourceFilePath2 = process.argv[3];
const destinationFilePath = process.argv[4];

const content1 = fs.readFileSync(sourceFilePath1, 'utf8');
const content2 = fs.readFileSync(sourceFilePath2, 'utf8');
const concatenatedContent = content1 + '\n' + content2;

fs.writeFileSync(destinationFilePath, concatenatedContent);
