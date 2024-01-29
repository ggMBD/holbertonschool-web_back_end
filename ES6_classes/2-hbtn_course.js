export default class HolbertonCourse {
  constructor(name, length, students) {
    this._name = this.validateString(name, 'name');
    this._length = this.validateNumber(length, 'length');
    this._students = this.validateStudentsArray(students, 'students');
  }

  set name(name) {
    this._name = this.validateString(name, 'name');
  }
  get name() {
    return this._name
  }

  set length(length) {
    this._length = this.validateNumber(length, 'length');
  }
  get length() {
    return this._length
  }

  set students(students) {
    this._students = this.validateStudentsArray(students, 'students');
  }
  get students() {
    return this._students
  }


  validateString(value, attribute) {
    if (typeof value !== 'string') {
      throw new Error(`${attribute} must be a string`);
    }
    return value;
  }

  validateNumber(value, attribute) {
    if (typeof value !== 'number' || isNaN(value)) {
      throw new Error(`${attribute} must be a valid number`);
    }
    return value;
  }

  validateStudentsArray(value, attribute) {
    if (!Array.isArray(value) || !value.every(item => typeof item === 'string')) {
      throw new Error(`${attribute} must be an array of strings`);
    }
    return value;
  }
}