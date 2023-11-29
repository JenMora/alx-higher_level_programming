#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    fs.writeFile(filePath, body, (writeErr) => {
      if (writeErr) {
        console.error(writeErr);
      } else {
        console.log(`Content successfully written to ${filePath}`);
      }
    });
  }
});
