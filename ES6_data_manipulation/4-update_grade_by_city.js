export default function updateStudentGradeByCity(students, city, newGrades) {
    const grade = {}
    for (const g of newGrades) {
        grade[g.studentId] = g.grade
    }
    return students.filter(student => student.location === city).map(student => ({ ...student, grade: grade[student.id] || 'N/A' }));
}
