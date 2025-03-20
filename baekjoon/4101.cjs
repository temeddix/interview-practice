const process = require("node:process");
const readline = require("node:readline");

const READER = readline.createInterface({ input: process.stdin });

async function main() {
  for await (const line of READER) {
    const [numA, numB] = line.split(" ").map((s) => Number(s));
    if (numA === 0 && numB === 0) {
      break;
    }
    console.log(numA > numB ? "Yes" : "No");
  }
}

main();
