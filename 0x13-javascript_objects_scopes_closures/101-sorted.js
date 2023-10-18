const data = require('./101-data'); // Import the dictionary from 101-data.js

// Initialize a new dictionary to store user IDs by occurrence
const userIDsByOccurrence = {};

// Iterate through the original dictionary and populate the new dictionary
for (const userID in data) {
  const occurrence = data[userID];

  if (!userIDsByOccurrence[occurrence]) {
    userIDsByOccurrence[occurrence] = [];
  }

  userIDsByOccurrence[occurrence].push(userID);
}

// Print the new dictionary
console.log(userIDsByOccurrence);
