const process = require("node:process");
const readline = require("node:readline");

async function* createInput() {
  const reader = readline.createInterface({ input: process.stdin });
  for await (const line of reader) yield line;
  return "";
}

/**
 * @param {string} text
 * @returns {boolean}
 */
function isVps(text) {
  let depth = 0;
  for (const letter of text) {
    if (letter === "(") {
      depth += 1;
    } else {
      depth -= 1;
    }
    if (depth < 0) {
      return false;
    }
  }
  return depth === 0;
}

async function main() {
  const input = createInput();
  const cases = Number((await input.next()).value);
  for (let i = 0; i < cases; i++) {
    const text = (await input.next()).value;
    console.log(isVps(text) ? "YES" : "NO");
  }
}

main();
