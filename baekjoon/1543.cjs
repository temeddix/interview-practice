const process = require("node:process");
const readline = require("node:readline");

async function* createInput() {
  const reader = readline.createInterface({ input: process.stdin });
  for await (const line of reader) yield line;
  return "";
}

async function main() {
  const input = createInput();
  const doc = (await input.next()).value;
  const docLen = doc.length;
  const pattern = (await input.next()).value;
  const patternLen = pattern.length;

  let i = 0;
  let occurence = 0;
  while (i < docLen) {
    const slice = doc.substring(i, i + patternLen);
    if (slice === pattern) {
      occurence += 1;
      i += patternLen;
    } else {
      i += 1;
    }
  }

  console.log(occurence);
}

main();
