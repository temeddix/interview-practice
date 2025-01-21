import sys
from collections import deque

START_NODE = 0

Node = set[int]  # Neighboring nodes of this node


def count_affected(nodes: list[Node]) -> int:
    explored = [False for _ in nodes]
    explored[0] = True
    cursors = deque[int]()
    cursors.append(0)

    count = 0
    while cursors:
        cursor = cursors.popleft()
        node = nodes[cursor]
        for neighboring_node in node:
            if explored[neighboring_node]:
                continue
            count += 1
            explored[neighboring_node] = True
            cursors.append(neighboring_node)

    return count


def main():
    node_count = int(input())
    connection_count = int(input())
    nodes: list[Node] = [set() for _ in range(node_count)]
    for _ in range(connection_count):
        node_a, node_b = (int(s) for s in sys.stdin.readline().split())
        node_a -= 1
        node_b -= 1
        nodes[node_a].add(node_b)
        nodes[node_b].add(node_a)
    count = count_affected(nodes)
    print(count)


main()
