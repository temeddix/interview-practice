from collections import deque
from dataclasses import dataclass
from sys import stdin, stdout

Node = list[int]  # Neighboring nodes


def choose_start_node(was_grouped: list[bool]) -> int | None:
    for i, value in enumerate(was_grouped):
        if not value:
            return i
    return None


@dataclass
class Record:
    was_taken: list[bool]
    did_use_edge: list[list[bool]]
    group_numbers: list[int]
    is_group_tree: dict[int, bool]


def spread_tree(
    nodes: list[Node],
    record: Record,
    start_node: int,
):
    was_taken = record.was_taken
    group_numbers = record.group_numbers
    is_group_tree = record.is_group_tree
    did_use_edge = record.did_use_edge

    cursors = deque[int]()
    cursors.append(start_node)
    current_group = group_numbers[start_node]
    is_group_tree[current_group] = True
    group_numbers[start_node] = -1

    while cursors:
        current = cursors.popleft()
        if group_numbers[current] == current_group:
            is_group_tree[current_group] = False
        was_taken[current] = True
        group_numbers[current] = current_group
        for neighbor in nodes[current]:
            if did_use_edge[current][neighbor]:
                continue
            did_use_edge[current][neighbor] = True
            did_use_edge[neighbor][current] = True
            cursors.append(neighbor)


def count_trees(nodes: list[Node]) -> int:
    was_taken = [False for _ in nodes]
    did_use_edge: list[list[bool]] = [[False for _ in nodes] for _ in nodes]
    group_numbers = [i for i in range(len(nodes))]
    is_group_tree: dict[int, bool] = {}
    record = Record(
        was_taken=was_taken,
        did_use_edge=did_use_edge,
        group_numbers=group_numbers,
        is_group_tree=is_group_tree,
    )

    while True:
        start_node = choose_start_node(was_taken)
        if start_node is None:
            break
        spread_tree(
            nodes,
            record=record,
            start_node=start_node,
        )

    groups = set(group_numbers)
    trees = 0
    for group in groups:
        if is_group_tree[group]:
            trees += 1

    return trees


def main():
    case_number = 0
    while True:
        case_number += 1
        node_count, edge_count = (int(s) for s in stdin.readline().split())
        if node_count == 0 and edge_count == 0:
            break
        nodes: list[Node] = [[] for _ in range(node_count)]
        for _ in range(edge_count):
            node_a, node_b = (int(s) for s in stdin.readline().split())
            node_a -= 1
            node_b -= 1
            nodes[node_a].append(node_b)
            nodes[node_b].append(node_a)
        trees = count_trees(nodes)
        if trees == 0:
            text = "No trees."
        elif trees == 1:
            text = "There is one tree."
        else:
            text = f"A forest of {trees} trees."
        stdout.write(f"Case {case_number}: {text}\n")


main()
