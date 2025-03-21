function solution() {
  /** @type {number[]} */
  const arrA = new Array(10).fill(7);
  console.log(arrA);

  /** @type {number[][]} */
  const arrB = Array.from({ length: 5 }, () => new Array(5).fill(7));
  console.log(arrB);
}

solution();
