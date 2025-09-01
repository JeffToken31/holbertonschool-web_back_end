const fs = require('node:fs');

async function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }
      const lines = data.split('\n').slice(1).filter((line) => line !== '');
      const fields = {};
      const total = lines.length;

      for (const line of lines) {
        const [firstname, , , field] = line.split(',');
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
      }
      console.log(`Number of students: ${total}`);
      for (const field of Object.keys(fields)) {
        console.log(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
      }
      resolve();
    });
  });
}

module.exports = countStudents;
