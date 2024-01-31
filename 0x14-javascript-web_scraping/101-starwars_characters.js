#!/usr/bin/node

const request = require('request');

function fetchCharacterNames (urls, index) {
  if (index === urls.length) {
    return;
  }

  request(urls[index], function (error, response, body) {
    if (error) {
      console.error('Error fetching character:', error);
      fetchCharacterNames(urls, index + 1); // Continue with the next character
      return;
    }

    try {
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    } catch (parseError) {
      console.error('Error parsing character content:', parseError.message);
    }

    fetchCharacterNames(urls, index + 1);
  });
}

const movieId = process.argv[2];
const apiUrl = 'https://swapi-api.hbtn.io/api/films/';

request.get(apiUrl + movieId, function (error, response, body) {
  if (error) {
    console.error('Error fetching movie:', error);
    return;
  }

  try {
    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;
    fetchCharacterNames(characterUrls, 0);
  } catch (parseError) {
    console.error('Error parsing movie content:', parseError.message);
  }
});
