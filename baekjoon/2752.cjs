const process = require("node:process");
const readline = require("node:readline");

const READER = readline.createInterface({ input: process.stdin });

/** @returns {Promise<string>} */
function input() {
  return new Promise((r) => READER.question("", r));
}

async function main() {
  const line = await input();
  const numbers = line.split(" ").map((s) => Number(s));
  numbers.sort((a, b) => a - b);
  console.log(numbers.join(" "));
}

main();
