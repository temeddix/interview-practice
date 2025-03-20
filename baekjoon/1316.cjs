const process = require("node:process");
const readline = require("node:readline");

async function* createInput() {
  const reader = readline.createInterface({ input: process.stdin });
  for await (const line of reader) yield line;
  return "";
}

const LETTERS = 26;
const BASE_CODE = "a".charCodeAt(0);

/**
 * @param {string} word
 * @returns {boolean}
 */
function isGroupWord(word) {
  /** @type {boolean[]} */
  const groupFinished = new Array(LETTERS).fill(false);

  let prevCode = word.charCodeAt(0) - BASE_CODE;
  for (let i = 0; i < word.length; i++) {
    const code = word.charCodeAt(i) - BASE_CODE;
    if (groupFinished[code]) {
      return false;
    }
    if (code != prevCode) {
      groupFinished[prevCode] = true;
    }
    prevCode = code;
  }

  return true;
}

async function main() {
  const input = createInput();
  const wordCount = Number((await input.next()).value);

  let groupWords = 0;
  for (let i = 0; i < wordCount; i++) {
    const word = (await input.next()).value;
    if (isGroupWord(word)) {
      groupWords += 1;
    }
  }

  console.log(groupWords);
}

main();
