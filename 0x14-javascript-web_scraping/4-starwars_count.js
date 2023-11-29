#!/usr/bin/node
const request = require('request');

// Check if the API URL is provided
if (process.argv.length !== 3) {
  console.error('Usage: node countMovies.js <api-url>');
  process.exit(1); // Exit with an error code
}

const apiUrl = process.argv[2];
const wedgeAntillesId = 18;

// Make a request to the Star Wars API films endpoint
request(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
  } else if (response.statusCode === 200) {
    const filmsData = JSON.parse(body).results;

    // Count the number of films where Wedge Antilles is present
    const wedgeMoviesCount = filmsData.reduce((count, film) => {
      const wedgeCharacter = film.characters.find(character => character.endsWith(`/${wedgeAntillesId}/`));
      if (wedgeCharacter) {
        count++;
      }
      return count;
    }, 0);

    console.log(`${wedgeMoviesCount}`);
  }
});
