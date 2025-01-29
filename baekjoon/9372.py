from sys import stdin
from typing import NamedTuple


class Edge(NamedTuple):
    node_a: int
    node_b: int


def main():
    test_count = int(input())
    for _ in range(test_count):
        # Node means country, and edge means plane route.
        node_count, edge_count = (int(s) for s in input().split())
        for _ in range(edge_count):
            _, _ = (int(s) for s in stdin.readline().split())
        print(node_count - 1)


main()
