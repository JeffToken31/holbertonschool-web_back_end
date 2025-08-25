export default function hasValuesFromArray (set, array) {
  let result = false;
  array.forEach(number => {
    if (set.has(number)) {
      result = true;
    } else {
      result = false;
    }
  });
  return result;
}
