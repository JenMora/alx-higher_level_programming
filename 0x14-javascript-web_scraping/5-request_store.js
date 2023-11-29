#!/usr/bin/node
const request = require('request');
const fs = require('fs');

// Check if both arguments are provided
if (process.argv.length !== 4) {
  console.error('Usage: node fetchAndStore.js <url> <file-path>');
  process.exit(1); // Exit with an error code
}

const url = process.argv[2];
const filePath = process.argv[3];

// Make a request to the specified URL
request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else if (response.statusCode === 200) {
    // Write the body response to the specified file
    fs.writeFile(filePath, body, 'utf-8', (writeErr) => {
      if (writeErr) {
        console.error(writeErr);
      } else {
        console.log(`Content successfully written to ${filePath}`);
      }
    });
  } else {
    console.error(`Error: Unable to fetch content from ${url}. Status code: ${response.statusCode}`);
  }
});
