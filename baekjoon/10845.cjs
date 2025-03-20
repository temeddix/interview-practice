const process = require("node:process");
const readline = require("node:readline");

async function* createInput() {
  const reader = readline.createInterface({ input: process.stdin });
  for await (const line of reader) yield line;
  return "";
}

/**
 * @template T
 */
class Queue {
  /** @type {T[]} */
  #data = [];
  /** @type {number} */
  #begin = 0;
  /** @type {number} */
  #end = 0;

  /**
   * @param {T} num
   */
  push(num) {
    this.#end += 1;
    if (this.#data.length < this.#end) {
      this.#data.push(num);
    } else {
      this.#data[this.#end - 1] = num;
    }
  }

  pop() {
    if (this.empty()) {
      return -1;
    } else {
      const num = this.#data[this.#begin];
      this.#begin += 1;
      if (this.empty()) {
        this.#begin = 0;
        this.#end = 0;
      }
      return num;
    }
  }

  size() {
    return this.#end - this.#begin;
  }

  empty() {
    return this.size() === 0;
  }

  front() {
    return this.empty() ? -1 : this.#data[this.#begin];
  }

  back() {
    return this.empty() ? -1 : this.#data[this.#end - 1];
  }
}

async function main() {
  const input = createInput();
  const cases = Number((await input.next()).value);

  /** @type {Queue<number>} */
  const queue = new Queue();
  /** @type {number[]} */
  const outputs = [];
  for (let i = 0; i < cases; i++) {
    const command = (await input.next()).value.split(" ");
    const commandType = command[0];
    if (commandType === "push") {
      queue.push(Number(command[1]));
    } else if (commandType === "pop") {
      outputs.push(queue.pop());
    } else if (commandType === "size") {
      outputs.push(queue.size());
    } else if (commandType === "empty") {
      outputs.push(queue.empty() ? 1 : 0);
    } else if (commandType === "front") {
      outputs.push(queue.front());
    } else if (commandType === "back") {
      outputs.push(queue.back());
    } else {
      throw new TypeError();
    }
  }

  console.log(outputs.join("\n"));
}

main();
