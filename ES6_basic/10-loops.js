export default function appendToEachArrayValue(array, appendString) {
  const tmpArray = [];
  for (const idx of array) {
    tmpArray.push(appendString + idx);
  }
  return tmpArray;
}
