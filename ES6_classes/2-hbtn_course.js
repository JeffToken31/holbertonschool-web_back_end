export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') {
      throw new TypeError('name must be a string');
    }
    this._name = name;
    if (typeof length !== 'number') {
      throw new TypeError('length must be a number');
    }
    this._length = length;
    if (!Array.isArray(students)) {
      throw new TypeError('students must be an array');
    }
    for (const student of students) {
      if (typeof student !== 'string') {
        throw new TypeError('students must be a string');
      }
    }
    this._students = students;
  }
  get name() {
    return this._name;
  }
  set name(v) {
    if (typeof v !== 'string') {
      throw new TypeError('name must be a string');
    }
    this._name = v;
  }
  get length() {
    return this._length;
  }
  set length(v) {
    if (typeof v !== 'number') {
      throw new TypeError('length must be a number');
    }
    this._length = v;
  }
  get students() {
    return this._students;
  }
  set students(v) {
    if (!Array.isArray(v)) {
      throw new TypeError('students must be an array');
    }
    for (const student of v) {
      if (typeof student !== 'string') {
        throw new TypeError('students must be a string');
      }
    }
    this._students = v;
  }
}
