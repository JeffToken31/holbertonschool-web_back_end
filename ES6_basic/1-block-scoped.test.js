import taskBlock from './1-block-scoped.js';

test('return boolean values', () => {
  expect(taskBlock()).toEqual([false, true]);
});
