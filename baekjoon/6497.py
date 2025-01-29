from sys import stdin
from typing import NamedTuple

FRED_NODE = 0


class Edge(NamedTuple):
    weight: int
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
    _, node_a, node_b = edge
    root_a = find_root(nodes, node_a)
    root_b = find_root(nodes, node_b)
    # Choose the node with smaller index as root.
    if root_a < root_b:
        nodes[root_b] = Node(root_a)
    elif root_b < root_a:
        nodes[root_a] = Node(root_b)


def get_weight_sum(edges: list[Edge], nodes: list[Node]) -> int:
    node_count = len(nodes)
    target_edges = node_count - 1

    used_edges = 0
    weight_sum = 0
    for edge in sorted(edges):
        weight, node_a, node_b = edge
        root_a = find_root(nodes, node_a)
        root_b = find_root(nodes, node_b)
        if root_a == root_b:
            continue
        weight_sum += weight
        used_edges += 1
        union_nodes(nodes, edge)
        if used_edges == target_edges:
            break

    return weight_sum


def main():
    while True:
        node_count, edge_count = (int(s) for s in input().split())
        if node_count == 0 and edge_count == 0:
            break
        nodes: list[Node] = [Node(i) for i in range(node_count)]
        edges: list[Edge] = []
        total_sum = 0
        for _ in range(edge_count):
            node_a, node_b, weight = (int(s) for s in stdin.readline().split())
            edges.append(Edge(weight, node_a, node_b))
            total_sum += weight
        weight_sum = get_weight_sum(edges, nodes)
        print(f"{total_sum - weight_sum}")


main()
