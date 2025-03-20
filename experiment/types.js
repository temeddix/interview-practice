/**
 * @param {number[]} arr
 * @returns {number[]}
 */
function compact(arr) {
  if (arr.length > 10) {
    return arr.slice(0, 10);
  }
  return arr;
}
