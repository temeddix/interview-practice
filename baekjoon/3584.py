from sys import stdin, stdout
from typing import NamedTuple


def main():
    test_count = int(input())
    for _ in range(test_count):
        node_count = int(stdin.readline())
        parents: list[int] = [i for i in range(node_count)]
        for _ in range(node_count - 1):
            parent, child = (int(s) for s in stdin.readline().split())
            parent -= 1
            child -= 1
            parents[child] = parent
        node_a, node_b = (int(s) for s in stdin.readline().split())
        node_a -= 1
        node_b -= 1
        node_pair = NodePair(node_a, node_b)
        nca = get_nca(parents, node_pair)
        stdout.write(f"{nca + 1}\n")


class NodePair(NamedTuple):
    node_a: int
    node_b: int


def get_nca(parents: list[int], node_pair: NodePair) -> int:
    # NCA stands for "nearest common ancestor".
    node_a, node_b = node_pair

    trail_a: list[int] = [node_a]
    trail_b: list[int] = [node_b]

    current_node = node_a
    while parents[current_node] != current_node:
        current_node = parents[current_node]
        trail_a.append(current_node)
    trail_a.reverse()

    current_node = node_b
    while parents[current_node] != current_node:
        current_node = parents[current_node]
        trail_b.append(current_node)
    trail_b.reverse()

    if trail_a[0] != trail_b[0]:
        raise ValueError

    max_depth = min(len(trail_a), len(trail_b)) - 1
    nca = trail_a[0]
    depth = 0
    while True:
        depth += 1
        if depth > max_depth:
            break
        child_a = trail_a[depth]
        child_b = trail_b[depth]
        if child_a != child_b:
            break
        nca = child_a

    return nca


main()
