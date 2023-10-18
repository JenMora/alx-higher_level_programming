#!/usr/bin/node
const FirstArgAsInt = parseInt(process.argv[2]);
if (!isNaN(FirstArgAsInt )) {
  console.log('My number: ' + FirstArgAsInt);
} else {
  console.log('Not a number');
}
