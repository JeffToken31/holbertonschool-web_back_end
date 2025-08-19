export default class Airport {
  constructor(name, code) {
    this._name = name;
    this._code = code;
  }
  get name() {
    return this._name;
  }
  set name(str) {
    if (typeof str !== 'string') {
      throw new TypeError('name must be a sring');
    }
    this._name = str;
  }
  get code() {
    return this._code;
  }
  set code(str) {
    if (typeof str !== 'string') {
      throw new TypeError('code must be a sring');
    }
    this._code = str;
  }
  toString() {
    return `[${typeof this} ${this._code}]`;
  }
  get [Symbol.toStringTag]() {
    return this._code;
  }
}
