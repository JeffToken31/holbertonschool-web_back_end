import {types} from '@babel/core';

export default class HolbertonCourse {
  constructor(name, length, students) {
    this._name = name;
    this._length = length;
    this._students = students;
  }
  get name() {
    return this._name;
  }
  set name(v) {
    if (typeof v !== 'string') {
      throw new TypeError('name must be a string');
    }
  }
  get length() {
    return this._length;
  }
  set length(v) {
    if (typeof v !== 'number') {
      throw new TypeError('length must be a number');
    }
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
  }
}
