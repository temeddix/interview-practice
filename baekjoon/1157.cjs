const process = require("node:process");
const readline = require("node:readline");

async function* createInput() {
  const reader = readline.createInterface({ input: process.stdin });
  for await (const line of reader) yield line;
  return "";
}

const LETTERS = 26;
const BASE_CODE = "A".charCodeAt(0);

async function main() {
  const input = createInput();
  /** @type {number[]} */
  const counts = new Array(LETTERS).fill(0);

  const text = (await input.next()).value.toUpperCase();
  for (const letter of text) {
    const index = letter.charCodeAt(0) - BASE_CODE;
    counts[index] += 1;
  }

  const maxValue = Math.max(...counts);
  /** @type {string[]} */
  const maxChars = [];
  for (let i = 0; i < LETTERS; i++) {
    if (counts[i] == maxValue) {
      maxChars.push(String.fromCharCode(BASE_CODE + i));
    }
  }

  console.log(maxChars.length == 1 ? maxChars[0] : "?");
}

main();
