#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (!err) {
    const todos = JSON.parse(body);

    // Renamed 'completed' to 'completedCounts'
    const completedCounts = {};

    todos.forEach((todo) => {
      // Renamed 'todo' to 'currentTodo'
      const currentTodo = todo;

      if (currentTodo.completed && completedCounts[currentTodo.userId] === undefined) {
        completedCounts[currentTodo.userId] = 1;
      } else if (currentTodo.completed) {
        completedCounts[currentTodo.userId] += 1;
      }
    });

    console.log(completedCounts);
  }
});
