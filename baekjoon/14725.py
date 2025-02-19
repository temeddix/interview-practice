from sys import stdin
from typing import NamedTuple


def main():
    food_count = int(stdin.readline().strip())

    roots: dict[str, Node] = {}
    for _ in range(food_count):
        # Split the input line and ignore the number.
        generator = (str(s) for s in stdin.readline().split())
        next(generator)

        # Get the root node.
        root_name = next(generator)
        current_node = roots.get(root_name)
        if current_node is None:
            current_node = Node(root_name, {})
            roots[root_name] = current_node

        # Go down the chain.
        for child_name in generator:
            _, children = current_node
            child_node = children.get(child_name)
            if child_node is None:
                child_node = Node(child_name, {})
                children[child_name] = child_node
            current_node = child_node

    print(format_trie(roots))


class Node(NamedTuple):
    name: str
    children: dict[str, "Node"]


class Job(NamedTuple):
    node: Node
    depth: int


def format_trie(roots: dict[str, Node]) -> str:
    lines: list[str] = []

    dfs_stack: list[Job] = []
    for _, root_node in sorted(roots.items(), reverse=True):
        dfs_stack.append(Job(root_node, 0))

    while dfs_stack:
        current_node, depth = dfs_stack.pop()
        name, children = current_node
        line = "--" * depth + name
        lines.append(line)
        for _, child_node in sorted(children.items(), reverse=True):
            dfs_stack.append(Job(child_node, depth + 1))

    return "\n".join(lines)


main()
