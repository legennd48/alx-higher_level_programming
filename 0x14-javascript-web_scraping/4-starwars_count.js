#!/usr/bin/node
/* display the status code of a GET request. */

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/'

request(url, function (err, httpResponse, body) {
  if (err) {
    console.error(err);
  }
  
  console.log(JSON.parse(body).title);
});
