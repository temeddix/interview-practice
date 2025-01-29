from sys import stdin, stdout
from typing import NamedTuple

FRED_NODE = 0


class Edge(NamedTuple):
    node_a: int
    node_b: int


class Node(NamedTuple):
    parent: int
    tree_size: int  # The number of childrens and oneself


def find_root(nodes: list[Node], node_index: int) -> int:
    current = node_index
    while nodes[current][0] != current:
        current, _ = nodes[current]
    root = current

    return root


def union_nodes(nodes: list[Node], edge: Edge):
    node_a, node_b = edge
    root_a = find_root(nodes, node_a)
    root_b = find_root(nodes, node_b)
    _, tree_size_a = nodes[root_a]
    _, tree_size_b = nodes[root_b]
    tree_size_sum = tree_size_a + tree_size_b
    # Choose the node with smaller index as root.
    if root_a < root_b:
        nodes[root_a] = Node(root_a, tree_size_sum)
        nodes[root_b] = Node(root_a, tree_size_b)
    elif root_b < root_a:
        nodes[root_a] = Node(root_b, tree_size_a)
        nodes[root_b] = Node(root_b, tree_size_sum)


def main():
    test_count = int(input())
    for _ in range(test_count):
        edge_count = int(stdin.readline().strip())
        nodes: list[Node] = []
        ids: dict[str, int] = {}
        for _ in range(edge_count):
            name_a, name_b = (str(s) for s in stdin.readline().split())
            if name_a in ids:
                node_a = ids[name_a]
            else:
                node_a = len(nodes)
                ids[name_a] = node_a
                nodes.append(Node(node_a, 1))
            if name_b in ids:
                node_b = ids[name_b]
            else:
                node_b = len(nodes)
                ids[name_b] = node_b
                nodes.append(Node(node_b, 1))
            edge = Edge(node_a, node_b)
            union_nodes(nodes, edge)
            fred_root = find_root(nodes, node_a)
            _, connected = nodes[fred_root]
            stdout.write(f"{connected}\n")


main()
