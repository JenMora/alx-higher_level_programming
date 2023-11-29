#!/usr/bin/node
const fs = require('fs');

// Check if both arguments are provided
if (process.argv.length !== 4) {
  console.error('Usage: node writeToFile.js <file-path> <string-to-write>');
  process.exit(1); // Exit with an error code
}

const filePath = process.argv[2];
const contentToWrite = process.argv[3];

// Write to the file
fs.writeFile(filePath, contentToWrite, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  } else {
    console.log(`Content successfully written to ${filePath}`);
  }
});
