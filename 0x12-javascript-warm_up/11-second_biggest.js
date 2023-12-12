#!/usr/bin/node

const findSecondLargest = (numbers) => {
  if (numbers.length <= 1) {
    return 0;
  }

  const sortedNumbers = numbers.map(Number).sort((a, b) => b - a);
  return sortedNumbers[1];
};

const inputNumbers = process.argv.slice(2);
const sec = findSecondLargest(inputNumbers);
console.log(sec);
