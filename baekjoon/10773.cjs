const process = require("node:process");
const readline = require("node:readline");

async function* createInput() {
  const reader = readline.createInterface({ input: process.stdin });
  for await (const line of reader) yield line;
  return "";
}

async function main() {
  const input = createInput();
  const numberCount = Number((await input.next()).value);
  /** @type {number[]} */
  const numbers = [];
  for (let i = 0; i < numberCount; i++) {
    const number = Number((await input.next()).value);
    if (number === 0) {
      numbers.pop();
    } else {
      numbers.push(number);
    }
  }
  console.log(numbers.reduce((a, b) => a + b, 0));
}

main();
