#!/usr/bin/node
// a script that computes the number of tasks completed by user id.
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const todos = JSON.parse(body);
    const completedTask = {};
    todos.forEach((todo) => {
      if (todo.completed) {
        const userId = parseInt(todo.userId);
        if (completedTask[userId] === undefined) {
          completedTask[userId] = 1;
        } else {
          completedTask[userId] += 1;
        }
      }
    });
    const formattedOutput = JSON.stringify(completedTask, null, 2);
    console.log(formattedOutput);
  } else {
    console.error('Error: Unable to fetch data from the API.');
  }
});
