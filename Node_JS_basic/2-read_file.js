const fs = require('node:fs');

function countStudents(path) {
	let data = [];
	try {
    data = fs.readFileSync(path, 'utf8');
  } catch (err) {
    throw new Error('Cannot load the database');
	}
	const lines = data.split('\n').slice(1).filter(line => line !== '');
	const sweName = [];
	const studentName = [];
	const total = lines.length;

	for (const line of lines) {
		const [firstname, lastname, age, field] = line.split(',');
		if (field === 'SWE') {
			sweName.push(firstname);
		} else if (field === 'CS') {
			studentName.push(firstname);
		}
	}
	console.log(`Number of students: ${total}`);
	console.log(
    `Number of students in CS: ${studentName.length}. List: ${studentName.join(', ')}`);
	console.log(
    `Number of students in CS: ${sweName.length}. List: ${sweName.join(', ')}`);
}

module.exports = countStudents;
