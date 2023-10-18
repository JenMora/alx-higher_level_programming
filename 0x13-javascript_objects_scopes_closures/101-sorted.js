#!/usr/bin/node
const dictUser = require('./101-data.js').dictUser;
const newDictUser = {};
for (const key in dictUser) {
  if (!newDictUser[dictUser[key]]
    newDictUser[dictUser[key]] = [];
  }
  newDictUser[dictUser[key]].push(key);
}
console.log(newDictUser);
