#!/usr/bin/node
const req = require("request");
const id = process.argv[2];
const url = "https://swapi-api.alx-tools.com/api/films/"
req.get(url + id, function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const data_chac = data.characters;
  for (const x of data_chac) {
    req.get(x, function (error, res, body1) {
      if (error) {
        console.log(error);
      }
      const data1 = JSON.parse(body1);
      console.log(data1.name);
    });
  }
});
