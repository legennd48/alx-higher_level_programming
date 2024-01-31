#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const apiUrl = 'https://swapi-api.hbtn.io/api/films/';

request.get(apiUrl + filmId, function (error, response, filmBody) {
  if (error) {
    console.error(error);
    return;
  }

  const filmData = JSON.parse(filmBody);
  const charactersUrls = filmData.characters;

  for (const characterUrl of charactersUrls) {
    request.get(characterUrl, function (error, response, characterBody) {
      if (error) {
        console.error(error);
        return;
      }

      const characterData = JSON.parse(characterBody);
      console.log(characterData.name);
    });
  }
});
