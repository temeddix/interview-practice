function solution() {
  /** @type {number[]} */
  const arrA = new Array(10).fill(7);
  console.log(arrA);

  /** @type {number[][]} */
  const arrB = new Array(5).fill(undefined).map((_) => new Array(5).fill(7));
  console.log(arrB);
}

solution();
