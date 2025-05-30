const process = require("node:process");
const readline = require("node:readline");

const READER = readline.createInterface({ input: process.stdin });

/** @returns {Promise<string>} */
function input() {
  return new Promise((r) => READER.question("", r));
}

async function main() {
  const line = await input();
  const [numA, numB] = line.split(" ").map((s) => Number(s));
  if (numA > numB) {
    console.log(">");
  } else if (numA < numB) {
    console.log("<");
  } else {
    console.log("==");
  }
}

main();
