from math import sqrt
from sys import stdin
from typing import NamedTuple

FRED_NODE = 0


class Edge(NamedTuple):
    weight: float
    node_a: int
    node_b: int


class Node(NamedTuple):
    parent: int


class Star(NamedTuple):
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


def get_weight_sum(edges: list[Edge], node_count: int) -> float:
    edges = sorted(edges)
    nodes: list[Node] = [Node(i) for i in range(node_count)]
    target_edges = node_count - 1

    used_edges = 0
    weight_sum = 0
    for edge in edges:
        weight, node_a, node_b = edge
        root_a = find_root(nodes, node_a)
        root_b = find_root(nodes, node_b)
        if root_a == root_b:
            continue
        used_edges += 1
        weight_sum += weight
        union_nodes(nodes, edge)
        if used_edges == target_edges:
            break

    return weight_sum


def main():
    star_count = int(input())
    stars: list[Star] = []
    for _ in range(star_count):
        x_pos, y_pos = (float(s) for s in stdin.readline().split())
        star = Star(x_pos, y_pos)
        stars.append(star)
    edges: list[Edge] = []
    for i, star_a in enumerate(stars):
        for j, star_b in enumerate(stars):
            if not i < j:
                continue
            x_diff = star_a[0] - star_b[0]
            y_diff = star_a[1] - star_b[1]
            weight = sqrt(x_diff**2 + y_diff**2)
            edges.append(Edge(weight, i, j))
    weight_sum = get_weight_sum(edges, star_count)
    print(f"{weight_sum:.2f}")


main()
