#!/usr/bin/node

const fs = require('fs');

const firstFilePath = process.argv[2];
const secondFilePath = process.argv[3];
const outputFilePath = process.argv[4];

const contentFromFirstFile = fs.readFileSync(firstFilePath, 'utf8');
const contentFromSecondFile = fs.readFileSync(secondFilePath, 'utf8');
const concatenatedContent = contentFromFirstFile + contentFromSecondFile;

fs.writeFileSync(outputFilePath, concatenatedContent);
