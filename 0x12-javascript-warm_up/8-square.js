#!/usr/bin/node

const param = process.argv[2];
let width = '';
if (!isNaN(param)) {
  for (let i = 0; i < param; i++) {
    for (let j = 0; j < param; j++) {
      width += 'X';
    }
    console.log(width);
    width = '';
  }
} else {
  console.log('Missing size');
}
