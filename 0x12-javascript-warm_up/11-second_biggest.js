#!/usr/bin/node
let biggerNum = 0;
const num = process.argv.slice(2);
if (num.length > 1) {
  num.sort((x, y) => x - y);
  biggerNum = num[num.length - 2];
}
console.log(biggerNum);
