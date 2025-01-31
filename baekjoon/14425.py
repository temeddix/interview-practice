from sys import stdin
from typing import NamedTuple


def main():
    word_count, check_count = (int(s) for s in input().split())
    trie = Trie()
    for _ in range(word_count):
        word = stdin.readline().strip()
        trie.insert(word)
    contained_count = 0
    for _ in range(check_count):
        word = stdin.readline().strip()
        if trie.contains(word):
            contained_count += 1
    print(contained_count)


class Node(NamedTuple):
    terminal: list[bool]
    children: list["Node | None"]  # Always size of 26


class Trie:
    def __init__(self):
        self.root = self._create_node()

    def _create_node(self):
        return Node([], [None] * 26)

    def insert(self, word: str):
        current = self.root
        for i in word:
            encoded = ord(i) - ord("a")
            children = current[1]
            child = children[encoded]
            if child is None:
                child = self._create_node()
                children[encoded] = child
            current = child
        current.terminal.append(True)

    def contains(self, word: str) -> bool:
        current = self.root
        for i in word:
            encoded = ord(i) - ord("a")
            children = current[1]
            child = children[encoded]
            if child is None:
                return False
            current = child
        return bool(current.terminal)


main()
