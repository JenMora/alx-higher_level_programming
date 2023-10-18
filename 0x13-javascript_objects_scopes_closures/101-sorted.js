#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newDict = {};
for (const user in dict) { 
  const key = dict[user];
  if (newDict[dict[key]] === undefined) {
    newDict[dict[key]] = [];
  }
    newDict[dict[key]].push(key);
}
console.log(newDict);
