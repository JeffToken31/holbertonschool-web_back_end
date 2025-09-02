import readDatabase from '../utils';

class StudentsController {
  static async getAllStudents(req, res) {
    try {
      const datas = await readDatabase(process.argv[2]);
      const datastoarray = Object.keys(datas).sort();
      let totalStr = 'This is the list of our students';
      for (const field of datastoarray) {
        const students = datas[field];
        const line = `Number of students in ${field}: ${students.length}. List: ${students.join(', ')}`;
        totalStr += `\n${line}`;
      }
      res.status(200).send(totalStr);
    } catch (err) {
      res.status(500).send(err.message);
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const { major } = req.params;
    try {
      const datas = await readDatabase(process.argv[2]);
      let totalStr = '';
      if (major !== 'CS' && major !== 'SWE') {
        return res.status(500).send('Major parameter must be CS or SWE');
      }
      const student = datas[major];
      const line = `List: ${student.join(', ')}`;
      totalStr += line;
      return res.status(200).send(totalStr);
    } catch (err) {
      return res.status(500).send(err.message);
    }
  }
}

export default StudentsController;
