import sys
from collections import deque

Node = list[int]  # Neighboring nodes

Cursor = tuple[
    int,  # Current
    int,  # Previous
]

NO_PARENT = -2
EMPTY = -1
START_NODE = 0  # 1 in human index


def get_parent_of_each(nodes: list[Node]) -> list[int]:
    node_count = len(nodes)
    parents = [EMPTY for _ in range(node_count)]

    cursors = deque[Cursor]()
    cursors.append((START_NODE, NO_PARENT))
    while cursors:
        current, previous = cursors.popleft()
        if parents[current] != EMPTY:
            continue
        parents[current] = previous
        for neighbor in nodes[current]:
            cursors.append((neighbor, current))

    return parents


def main():
    node_count = int(input())
    nodes: list[Node] = [[] for _ in range(node_count)]
    for _ in range(node_count - 1):
        node_a, node_b = (int(s) for s in sys.stdin.readline().split())
        node_a -= 1
        node_b -= 1
        nodes[node_a].append(node_b)
        nodes[node_b].append(node_a)
    parents = get_parent_of_each(nodes)
    for parent in parents[1:]:
        sys.stdout.write(f"{parent + 1}\n")


main()
