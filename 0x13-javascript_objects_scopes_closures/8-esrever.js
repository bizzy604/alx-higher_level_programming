#!/usr/bin/node
exports.esrever = function (list) {
  const reversedList = [];

  let lastObject = list.length - 1;

  for (let i = 0; i < list.length; i++) {
    reversedList.push(list[lastObject]);
    lastObject--;
  }

  return reversedList;
};
