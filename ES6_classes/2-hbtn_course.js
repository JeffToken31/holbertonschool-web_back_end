export default class HolbertonCourse {
  constructor(name, length, students) {
    this.name = name;
    this.length = length;
    this.students = students;
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
