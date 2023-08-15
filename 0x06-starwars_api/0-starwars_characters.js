#!/usr/bin/node
/**
 * return the character names
 * of specified films by id
 * @params integer
 */

const request = require('request');

const endpoint = 'https://swapi-api.alx-tools.com/api';
const filmId = process.argv[2];

request(`/${endpoint}/films/${filmId}/`, async (error, _res, body) => {
  if (error) return console.log(error);

  const characters = await JSON.parse(body).characters;

  for (const character of characters) {
    await new Promise((resolve, reject) => {
      request(character, (error, _res, body) => {
        if (error) {
          reject(error);
        } else {
          console.log(JSON.parse(body).name);
          resolve(body);
        }
      });
    });
  }
});
