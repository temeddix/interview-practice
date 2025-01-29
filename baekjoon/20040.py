from sys import stdin, stdout
from typing import NamedTuple

FRED_NODE = 0


class Edge(NamedTuple):
    node_a: int
    node_b: int


class Node(NamedTuple):
    parent: int


def find_root(nodes: list[Node], node_index: int) -> int:
    trail: list[int] = []

    current = node_index
    while nodes[current][0] != current:
        trail.append(current)
        (current,) = nodes[current]
    root = current

    for each in trail:
        nodes[each] = Node(root)

    return root


def union_nodes(nodes: list[Node], edge: Edge):
    node_a, node_b = edge
    root_a = find_root(nodes, node_a)
    root_b = find_root(nodes, node_b)
    # Choose the node with smaller index as root.
    if root_a < root_b:
        nodes[root_b] = Node(root_a)
    elif root_b < root_a:
        nodes[root_a] = Node(root_b)


def main():
    node_count, edge_count = (int(s) for s in input().split())
    nodes: list[Node] = [Node(i) for i in range(node_count)]
    cycle_at = 0
    for turn in range(edge_count):
        node_a, node_b = (int(s) for s in stdin.readline().split())
        edge = Edge(node_a, node_b)
        root_a = find_root(nodes, node_a)
        root_b = find_root(nodes, node_b)
        if root_a == root_b:
            cycle_at = turn + 1
            break
        union_nodes(nodes, edge)
    stdout.write(str(cycle_at))


main()
