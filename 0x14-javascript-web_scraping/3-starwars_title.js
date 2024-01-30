#!/usr/bin/node
/* display the status code of a GET request. */

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  }
  console.log(JSON.parse(body).title);
});
