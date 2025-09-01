const fs = require('node:fs');

function countStudents (path) {
  let data;
  try {
    data = fs.readFileSync(path, 'utf8');
  } catch (err) {
    throw new Error('Cannot load the database');
  }
  const lines = data.split('\n').slice(1).filter(line => line !== '');
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
}

module.exports = countStudents;
