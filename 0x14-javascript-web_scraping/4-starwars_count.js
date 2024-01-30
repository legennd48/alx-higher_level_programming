#!/usr/bin/node

const apiUrl = process.argv[2];
const request = require('request');

request(apiUrl, function (error, response, responseBody) {
  if (error) console.log(error);

  let charactersList = [];

  for (const film of JSON.parse(responseBody).results) {
    charactersList = charactersList.concat(film.characters);
  }

  const uniqueCharacters = charactersList.filter(character => character.includes('18'));
  console.log(uniqueCharacters.length);
});
