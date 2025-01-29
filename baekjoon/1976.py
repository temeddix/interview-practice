from sys import stdin
from typing import NamedTuple

UNION_OP = 0
SEARCH_OP = 1


class Edge(NamedTuple):
    parent: int
    child: int


def find_parent(parents: list[int], node_index: int) -> int:
    current = node_index
    middle_indices = [node_index]
    while parents[current] != current:
        parent = parents[current]
        middle_indices.append(parent)
        current = parent
    for middle_index in middle_indices:
        parents[middle_index] = current
    return current


def group_nodes(node_count: int, edges: list[Edge]) -> list[int]:
    parents = [i for i in range(node_count)]

    for parent, child in edges:
        child_parent = find_parent(parents, child)
        parent_parent = find_parent(parents, parent)
        if child_parent < parent_parent:
            parents[parent_parent] = child_parent
        else:
            parents[child_parent] = parent_parent

    return parents


def check_trip_plan(parents: list[int], trip_plan: list[int]) -> bool:
    groups = [find_parent(parents, p) for p in trip_plan]
    unique_groups = set(groups)
    if len(unique_groups) == 1:
        return True
    else:
        return False


def main():
    node_count = int(input())
    _ = int(input())
    edges: list[Edge] = []
    for node_a in range(node_count):
        node_b_list = [True if s == "1" else False for s in stdin.readline().split()]
        for node_b, is_connected in enumerate(node_b_list):
            if node_a < node_b and is_connected:
                edge = Edge(node_a, node_b)
                edges.append(edge)
    parents = group_nodes(node_count, edges)
    trip_plan = [int(s) - 1 for s in input().split()]
    is_plan_okay = check_trip_plan(parents, trip_plan)
    print("YES" if is_plan_okay else "NO")


main()
