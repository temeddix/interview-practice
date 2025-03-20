const process = require("node:process");
const readline = require("node:readline");

const READER = readline.createInterface({ input: process.stdin });

/** @returns {Promise<string>} */
function input() {
  return new Promise((r) => READER.question("", r));
}

async function main() {
  const received = await input();
  const [numA, numB] = received.split(" ").map((s) => Number(s));
  console.log(numA + numB);
}

main();
