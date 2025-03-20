const process = require("node:process");
const readline = require("node:readline");

async function* createInput() {
  const reader = readline.createInterface({ input: process.stdin });
  for await (const line of reader) yield line;
  return "";
}

/**
 * @typedef Spot
 * @property {number} row
 * @property {number} col
 */

/**
 * @param {number[][]} cells
 * @param {Spot} startSpot
 * @param {Spot} endSpot
 * @returns {number}
 */
function getSum(cells, startSpot, endSpot) {
  let sumValue = 0;
  for (let r = startSpot.row; r <= endSpot.row; r++) {
    for (let c = startSpot.col; c <= endSpot.col; c++) {
      sumValue += cells[r][c];
    }
  }
  return sumValue;
}

async function main() {
  const input = createInput();
  const [rowCount, _colCount] = (await input.next()).value
    .split(" ")
    .map((s) => Number(s));

  /** @type {number[][]} */
  const cells = [];
  for (let i = 0; i < rowCount; i++) {
    const rowCells = (await input.next()).value
      .split(" ")
      .map((s) => Number(s));
    cells.push(rowCells);
  }

  const cases = Number((await input.next()).value);
  for (let i = 0; i < cases; i++) {
    const [aRow, aCol, bRow, bCol] = (await input.next()).value
      .split(" ")
      .map((s) => Number(s));
    const sumValue = getSum(
      cells,
      { row: aRow - 1, col: aCol - 1 },
      { row: bRow - 1, col: bCol - 1 }
    );
    console.log(sumValue);
  }
}

main();
