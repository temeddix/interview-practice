from sys import stdin

# Using `set` here is not appropriate
# because the problem was about using the trie data structure.


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


class Node:
    def __init__(self):
        self.terminal = False
        self.children: list[Node | None] = [None for _ in range(26)]


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str):
        current = self.root
        for i in word:
            encoded = ord(i) - ord("a")
            children = current.children
            child = children[encoded]
            if child is None:
                child = Node()
                children[encoded] = child
            current = child
        current.terminal = True

    def contains(self, word: str) -> bool:
        current = self.root
        for i in word:
            encoded = ord(i) - ord("a")
            children = current.children
            child = children[encoded]
            if child is None:
                return False
            current = child
        return current.terminal


main()
