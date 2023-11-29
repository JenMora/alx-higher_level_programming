#!/usr/bin/node
const request = require('request');

// Check if the Movie ID is provided
if (process.argv.length !== 3) {
  console.error('Usage: node starWarsCharacters.js <movie-id>');
  process.exit(1); // Exit with an error code
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Function to make a request and return a promise
const makeRequest = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (err, response, body) => {
      if (err) {
        reject(err);
      } else if (response.statusCode === 200) {
        resolve(JSON.parse(body).name);
      } else {
        reject(`Error: Unable to fetch character data. Status code: ${response.statusCode}`);
      }
    });
  });
};

// Make a request to the Star Wars API films endpoint for the specified movie ID
request(apiUrl, async (err, response, body) => {
  if (err) {
    console.error(err);
  } else if (response.statusCode === 200) {
    const movieData = JSON.parse(body);

    try {
      // Use Promise.all to handle all character requests in parallel
      const characterNames = await Promise.all(movieData.characters.map(makeRequest));
      
      // Print characters one by line in the same order as the list in the /films/ response
      characterNames.forEach((characterName) => {
        console.log(characterName);
      });
    } catch (error) {
      console.error(error);
    }
  } else {
    console.error(`Error: Unable to fetch movie data. Status code: ${response.statusCode}`);
  }
});
