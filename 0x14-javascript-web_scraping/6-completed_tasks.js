#!/usr/bin/node
const request = require("request");
request(process.argv[2], function (error, response, body) {
  if (!error) {
    const todos = JSON.parse(body);
    let completed_task = {};
    todos.forEach((todo) => {
      if (todo.completed_task && completed_task[todo.userId] === undefined) {
        completed_task[todo.userId] = 1;
      } else if (todo.completed_task) {
        completed_task[todo.userId] += 1;
      }
    });
    console.log(completed_task);
  }
});
