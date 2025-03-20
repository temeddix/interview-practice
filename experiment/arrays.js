function solution() {
  /** @type {number[]} */
  let arrA = Array(10).fill(7);
  console.log(arrA);

  /** @type {number[][]} */
  let arrB = Array(5)
    .fill(undefined)
    .map((e) => Array(5).fill(7));
  console.log(arrB);
}

solution();
