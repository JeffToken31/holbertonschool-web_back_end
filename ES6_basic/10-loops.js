export default function appendToEachArrayValue(array, appendString) {
    const tmpArray = [];
  for (let idx of array) {
    tmpArray.push(appendString + idx);
  }

  return tmpArray;
}