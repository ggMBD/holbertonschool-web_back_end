export default function getlistStudentids(list) {
  if (!Array.isArray(list)) {
    return [];
  }
  return list.map((student) => student.id);
}
