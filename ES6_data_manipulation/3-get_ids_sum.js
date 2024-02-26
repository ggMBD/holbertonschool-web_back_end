export default function getStudentIdSum(studentList) {
  return studentList.reduce((sum, student) => sum + student.id, 0);
}
