const process = require("node:process");
const readline = require("node:readline");

async function* createInput() {
  const reader = readline.createInterface({ input: process.stdin });
  for await (const line of reader) yield line;
  return "";
}

/**
 * @typedef Pair
 * @property {number} smaller
 * @property {number} bigger
 */

async function main() {
  const input = createInput();
  const numCount = Number((await input.next()).value);

  for (let i = 0; i < numCount; i++) {
    const num = Number((await input.next()).value);

    /** @type {Pair} */
    const pair = { smaller: 1, bigger: num - 1 };
    /** @type {Pair[]} */
    const pairs = [];

    while (pair.smaller < pair.bigger) {
      pairs.push({ smaller: pair.smaller, bigger: pair.bigger });
      pair.smaller += 1;
      pair.bigger -= 1;
    }
    const pairStr = pairs.map((p) => `${p.smaller} ${p.bigger}`).join(", ");
    console.log(`Pairs for ${num}: ` + pairStr);
  }
}

main();
