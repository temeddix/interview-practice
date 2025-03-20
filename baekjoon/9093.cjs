const process = require("node:process");
const readline = require("node:readline");

async function* createInput() {
  const reader = readline.createInterface({ input: process.stdin });
  for await (const line of reader) yield line;
  return "";
}

async function main() {
  const input = createInput();
  const cases = Number((await input.next()).value);
  for (let i = 0; i < cases; i++) {
    const line = (await input.next()).value;
    const reversed = line.split(" ").map((w) => w.split("").reverse().join(""));
    const joined = reversed.join(" ");
    console.log(joined);
  }
}

main();
