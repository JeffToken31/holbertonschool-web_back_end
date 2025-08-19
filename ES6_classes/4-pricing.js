import Currency from './3-currency.js';

export default class Pricing {
  constructor(amount, currency) {
    this._amount = amount;
    this.currency = currency;
  }
  get amount() {
    return this._amount;
  }
  set amount(v) {
    if (typeof v !== 'number') {
      throw new TypeError('amount must be a number');
    }
    this._amount = v;
  }
  get currency() {
    return this._currency;
  }
  set currency(v) {
    if (!(v instanceof Currency)) {
      throw new TypeError('currency must be an intance of Currency');
    }
    this._currency = v;
  }
  displayFullPrice() {
    return `${this.amount} ${this.currency.name} (${this.currency.code})`;
  }

  static convertPrice(amount, conversionRate) {
    if (typeof amount !== 'number' || typeof conversionRate !== 'number') {
      throw new TypeError('amount must be a number');
    }
    return amount * conversionRate;
  }
}
