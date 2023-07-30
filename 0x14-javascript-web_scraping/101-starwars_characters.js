#!/usr/bin/node
// a script that prints all characters of a Star Wars movie:
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    charactersPrint(characters, 0);
  }
});

function charactersPrint (characters, index) {
  request(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        charactersPrint(characters, index + 1);
      }
    }
  });
}
