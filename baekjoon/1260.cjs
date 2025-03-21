const process = require("node:process");
const readline = require("node:readline");

async function* createInput() {
  const reader = readline.createInterface({ input: process.stdin });
  for await (const line of reader) yield line;
  return "";
}

class Queue {
  /** @type {number[]} */
  #data = [];
  /** @type {number} */
  #begin = 0;
  /** @type {number} */
  #end = 0;

  /**
   * @param {number} num
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
    if (!this.length) {
      throw new TypeError();
    } else {
      const num = this.#data[this.#begin];
      this.#begin += 1;
      if (!this.length) {
        this.#begin = 0;
        this.#end = 0;
      }
      return num;
    }
  }

  get length() {
    return this.#end - this.#begin;
  }
}

class Node {
  /** @type {number[]} */
  neighbors = [];
}

/**
 * @param {Node[]} nodes
 * @param {number} startNode
 * @returns {number[]} */
function searchDfs(nodes, startNode) {
  const visitOrder = [];
  const visited = new Array(nodes.length).fill(false);

  const dfsStack = [];
  dfsStack.push(startNode);
  while (dfsStack.length) {
    const currNode = dfsStack.pop();
    if (currNode === undefined) {
      throw new TypeError();
    }
    if (visited[currNode]) {
      continue;
    }
    visited[currNode] = true;
    visitOrder.push(currNode);
    const reversedNeighbors = nodes[currNode].neighbors.slice();
    reversedNeighbors.reverse();
    for (const nextNode of reversedNeighbors) {
      dfsStack.push(nextNode);
    }
  }

  return visitOrder;
}

/**
 * @param {Node[]} nodes
 * @param {number} startNode
 * @returns {number[]} */
function searchBfs(nodes, startNode) {
  const visitOrder = [];
  const visited = new Array(nodes.length).fill(false);
  visited[startNode] = true;

  const bfsQueue = new Queue();
  bfsQueue.push(startNode);
  while (bfsQueue.length) {
    const currNode = bfsQueue.pop();
    visitOrder.push(currNode);
    for (const nextNode of nodes[currNode].neighbors) {
      if (!visited[nextNode]) {
        bfsQueue.push(nextNode);
        visited[nextNode] = true;
      }
    }
  }

  return visitOrder;
}

async function main() {
  const input = createInput();
  let [nodeCount, edgeCount, startNode] = (await input.next()).value
    .split(" ")
    .map(Number);
  startNode -= 1;

  const nodes = Array.from({ length: nodeCount }, (_) => new Node());
  for (let i = 0; i < edgeCount; i++) {
    const [nodeA, nodeB] = (await input.next()).value
      .split(" ")
      .map((s) => Number(s) - 1);
    nodes[nodeA].neighbors.push(nodeB);
    nodes[nodeB].neighbors.push(nodeA);
  }

  for (const node of nodes) {
    node.neighbors.sort((a, b) => a - b);
  }

  const dfsOrder = searchDfs(nodes, startNode);
  console.log(dfsOrder.map((n) => n + 1).join(" "));
  const bfsOrder = searchBfs(nodes, startNode);
  console.log(bfsOrder.map((n) => n + 1).join(" "));
}

main();
