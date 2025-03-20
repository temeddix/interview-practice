const process = require("node:process");
const readline = require("node:readline");

async function* createInput() {
  const reader = readline.createInterface({ input: process.stdin });
  for await (const line of reader) yield line;
  return "";
}

class Stack {
  /** @type {number[]} */
  #data = [];

  /**
   * @param {string[]} command
   * @returns {number?}
   */
  operate(command) {
    const commandType = command[0];
    if (commandType === "push") {
      this.#data.push(Number(command[1]));
    } else if (commandType === "pop") {
      const number = this.#data.pop();
      return number === undefined ? -1 : number;
    } else if (commandType === "size") {
      return this.#data.length;
    } else if (commandType === "empty") {
      return this.#data.length === 0 ? 1 : 0;
    } else {
      const dataLen = this.#data.length;
      return dataLen == 0 ? -1 : this.#data[dataLen - 1];
    }
    return null;
  }
}

async function main() {
  const input = createInput();
  const commandCount = Number((await input.next()).value);

  const stack = new Stack();
  /** @type {number[]} */
  const outputs = [];
  for (let i = 0; i < commandCount; i++) {
    const command = (await input.next()).value.split(" ");
    const output = stack.operate(command);
    if (output !== null) {
      outputs.push(output);
    }
  }

  console.log(outputs.join("\n"));
}

main();
