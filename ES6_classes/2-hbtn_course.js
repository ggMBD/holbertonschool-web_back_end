export default class HolbertonCourse {
  constructor(name, length, students) {
    this._name = name;
    this._length = length;
    this._students = students;
  }

  set name(name) {
    this._name = name;
  }
  get name() {
    return this._name
  }

  set length(length) {
    this._length = length;
  }
  get length() {
    return this._length
  }

  set students(students) {
    this._students = students;
  }
  get students() {
    return this._students
  }
}
