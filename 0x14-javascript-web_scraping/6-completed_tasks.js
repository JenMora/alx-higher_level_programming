#!/usr/bin/node
const request = require('request');

// Check if the API URL is provided
if (process.argv.length !== 3) {
  console.error('Usage: node countCompletedTasks.js <api-url>');
  process.exit(1); // Exit with an error code
}

const apiUrl = process.argv[2];

// Make a request to the JSONPlaceholder API todos endpoint
request(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
  } else if (response.statusCode === 200) {
    const todosData = JSON.parse(body);

    // Create an object to store the count of completed tasks for each user
    const completedTasksCount = {};

    // Iterate through each todo and count completed tasks
    todosData.forEach(todo => {
      if (todo.completed) {
        const userId = todo.userId;
        completedTasksCount[userId] = (completedTasksCount[userId] || 0) + 1;
      }
    });

    console.log(completedTasksCount);
  } else {
    console.error(`Error: Unable to fetch data from ${apiUrl}. Status code: ${response.statusCode}`);
  }
});
