export default class Currency {
  constructor(code, name) {
    this._code = code;
    this._name = name;
  }
  get code() {
    return this._code;
  }
  set code(v) {
    if (typeof code !== 'string') {
      throw new TypeError('code must be a string');
    }
    this._code = this.code;
  }
  get name() {
    return this._name;
  }
  set name(v) {
    if (typeof name !== 'string') {
      throw new TypeError('name must be a string');
    }
    this._name = this.name;
  }
  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
