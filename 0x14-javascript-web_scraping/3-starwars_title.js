#!/usr/bin/node
const request = require('request');
const apiUrl = 'https://swapi-api.hbtn.io/api/films/';
const episode = process.argv[2];

request(apiUrl + episode, (err, response, body) => {
  if (err) {
    console.error(err);
  } else if (response.statusCode === 200) {
    const filmData = JSON.parse(body);
    console.log(filmData.title);
  }
});
