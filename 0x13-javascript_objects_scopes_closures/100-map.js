#!/usr/bin/node
const list = require('./100-data.js').list;
// or
// const Data = require("./100-data.js');
// const list = Data.list;
const newList = list.map((value, index) =>  value * index);
console.log(list);
console.log(newList);
