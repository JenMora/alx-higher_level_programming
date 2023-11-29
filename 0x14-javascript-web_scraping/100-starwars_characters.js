#!/usr/bin/node
const request = require('request');

// Check if the Movie ID is provided
if (process.argv.length !== 3) {
  console.error('Usage: node starWarsCharacters.js <movie-id>');
  process.exit(1); // Exit with an error code
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Make a request to the Star Wars API films endpoint for the specified movie ID
request(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
  } else if (response.statusCode === 200) {
    const movieData = JSON.parse(body);

    // Print characters one by line
    movieData.characters.forEach((characterUrl) => {
      request(characterUrl, (charErr, charResponse, charBody) => {
        if (charErr) {
          console.error(charErr);
        } else if (charResponse.statusCode === 200) {
          const characterData = JSON.parse(charBody);
          console.log(characterData.name);
        } else {
          console.error(`Error: Unable to fetch character data. Status code: ${charResponse.statusCode}`);
        }
      });
    });
  } else {
    console.error(`Error: Unable to fetch movie data. Status code: ${response.statusCode}`);
  }
});
