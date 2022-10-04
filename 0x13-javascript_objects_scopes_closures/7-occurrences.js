#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const item in list) {
    if (list[item] === searchElement) {
      count++;
    }
  }
  return count;
};
