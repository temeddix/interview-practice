from collections import deque
from sys import stdin


def main():
    node_count, edge_count = (int(s) for s in input().split())
    incomings: list[int] = [0 for _ in range(node_count)]
    nexts: list[list[int]] = [[] for _ in range(node_count)]
    for _ in range(edge_count):
        node_a, node_b = (int(s) for s in stdin.readline().split())
        node_a -= 1
        node_b -= 1
        nexts[node_a].append(node_b)
        incomings[node_b] += 1
    sorted_nodes = sort_nodes(incomings, nexts)
    print(" ".join(str(i + 1) for i in sorted_nodes))


def sort_nodes(incomings: list[int], nexts: list[list[int]]) -> list[int]:
    sorted_nodes: list[int] = []
    cursors = deque[int]()

    for node, incoming in enumerate(incomings):
        if incoming == 0:
            cursors.append(node)

    while cursors:
        current_node = cursors.popleft()
        sorted_nodes.append(current_node)
        for next_node in nexts[current_node]:
            incomings[next_node] -= 1
            if incomings[next_node] == 0:
                cursors.append(next_node)

    return sorted_nodes


main()
