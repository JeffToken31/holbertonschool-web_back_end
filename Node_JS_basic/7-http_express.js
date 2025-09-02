const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const port = 1245;

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  countStudents(process.argv[2])
    .then((data) => {
      res.write('');
      res.end(`This is the list of our students\n${data.join('\n')}`);
    })
    .catch((error) => {
      res.statusCode = 500;
      res.end(error.message);
    });
});

app.listen(port);

module.exports = app;
