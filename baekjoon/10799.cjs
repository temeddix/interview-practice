const process = require("node:process");
const readline = require("node:readline");

async function* createInput() {
  const reader = readline.createInterface({ input: process.stdin });
  for await (const line of reader) yield line;
  return "";
}

/**
 * @param {string} text
 * @returns {number}
 */
function getPieces(text) {
  const processed = text.replaceAll("()", ".");
  let depth = 0;
  let pieces = 0;
  for (const letter of processed) {
    if (letter === "(") {
      depth += 1;
      pieces += 1;
    } else if (letter === ")") {
      depth -= 1;
    } else {
      pieces += depth;
    }
  }
  return pieces;
}

async function main() {
  const input = createInput();
  const text = (await input.next()).value;
  console.log(getPieces(text));
}

main();
