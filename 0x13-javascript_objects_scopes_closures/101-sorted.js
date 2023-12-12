#!/usr/bin/node

const inputDictionary = require('./101-data').dict;
const outputDictionary = {};

for (const key in inputDictionary) {
  const value = inputDictionary[key];

  if (!outputDictionary[value]) {
    outputDictionary[value] = [];
  }

  outputDictionary[value].push(key);
}

console.log(outputDictionary);
