from math import pow, sqrt
from sys import stdin
from typing import NamedTuple

FRED_NODE = 0


class Edge(NamedTuple):
    weight: float
    node_a: int
    node_b: int


class Node(NamedTuple):
    parent: int


class God(NamedTuple):
    x_pos: float
    y_pos: float


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


def get_weight_sum(
    existing_edges: list[Edge],
    possible_edges: list[Edge],
    node_count: int,
) -> float:
    nodes: list[Node] = [Node(i) for i in range(node_count)]
    target_edges = node_count - 1

    existing_left = len(existing_edges) + 1
    used_edges = 0
    weight_sum = 0
    for edge in sorted(existing_edges) + sorted(possible_edges):
        weight, node_a, node_b = edge
        existing_left -= 1
        root_a = find_root(nodes, node_a)
        root_b = find_root(nodes, node_b)
        if root_a == root_b:
            continue
        if existing_left <= 0:
            weight_sum += weight
        used_edges += 1
        union_nodes(nodes, edge)
        if used_edges == target_edges:
            break

    return weight_sum


def get_dist(god_a: God, god_b: God) -> float:
    x_diff = god_a[0] - god_b[0]
    y_diff = god_a[1] - god_b[1]
    weight = sqrt(pow(x_diff, 2) + pow(y_diff, 2))
    return weight


def main():
    god_count, existing_edge_count = (int(s) for s in input().split())
    gods: list[God] = []
    for _ in range(god_count):
        x_pos, y_pos = (float(s) for s in stdin.readline().split())
        god = God(x_pos, y_pos)
        gods.append(god)
    existing_edges: list[Edge] = []
    for _ in range(existing_edge_count):
        node_a, node_b = (int(s) for s in stdin.readline().split())
        node_a -= 1
        node_b -= 1
        god_a = gods[node_a]
        god_b = gods[node_b]
        weight = get_dist(god_a, god_b)
        existing_edges.append(Edge(weight, node_a, node_b))
    possible_edges: list[Edge] = []
    for i, god_a in enumerate(gods):
        for j, god_b in enumerate(gods):
            if not i < j:
                continue
            weight = get_dist(god_a, god_b)
            possible_edges.append(Edge(weight, i, j))
    weight_sum = get_weight_sum(existing_edges, possible_edges, god_count)
    print(f"{weight_sum:.2f}")


main()
