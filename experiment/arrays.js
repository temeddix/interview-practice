function solution() {
  /** @type {number[]} */
  const arrA = Array(10).fill(7);
  console.log(arrA);

  /** @type {number[][]} */
  const arrB = Array(5)
    .fill(undefined)
    .map((_) => Array(5).fill(7));
  console.log(arrB);
}

solution();
