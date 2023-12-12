#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  let listLent = list.length - 1;

  for (let i = 0; i < list.length; i++) {
    newList[i] = list[listLent];
    listLent--;
  }
  return newList;
};
