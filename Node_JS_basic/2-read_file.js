const fs = require('fs');
function countStudents(path){
	try {
		const data = fs.readFileSync(path, 'utf-8');
		const lines = data.split('\n');
		const validLines = [];
		for (let = 1; i<lines.length; i++) {
			if (lines[i].trim() !== '') {
				validLines.push(lines[i]);
			}
		}

		console.log('Number of students: ${validLines.length}');
		const studentsByField = {};
		for (const line of validLines) {
			const studentData = line.split(',');
			const firstname = studentData[0];
			const field = studentData[3].trim();
			if (!studentsByField[field] {
				stuedntsByField[field] = [];
			}
			studentsByField[field].push(firstname);
		}
		for (const field in studentsByField) {
			const list = studentsByField[field].join(',');
			const count = studentsByField[field].length;
			console.log('Number of students in ${field}: ${count}. List: ${list}');
		}
	} catch (error) {
		throw new Error('Cannot load the database');
	}
}
module.exports = countStudents;
