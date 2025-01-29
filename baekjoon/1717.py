from sys import stdin, stdout
from typing import NamedTuple

UNION_OP = 0
SEARCH_OP = 1


class Operation(NamedTuple):
    command: int
    number_a: int
    number_b: int


def find_parent(nodes: list[int], node_index: int) -> int:
    current = node_index
    middle_indices = [node_index]
    while nodes[current] != current:
        parent = nodes[current]
        middle_indices.append(parent)
        current = parent
    for middle_index in middle_indices:
        nodes[middle_index] = current
    return current


def union_parents(nodes: list[int], number_a: int, number_b: int):
    if number_a == number_b:
        return
    parent_a = find_parent(nodes, number_a)
    parent_b = find_parent(nodes, number_b)
    if parent_a < parent_b:
        nodes[parent_b] = parent_a
    else:
        nodes[parent_a] = parent_b


def perform_operations(max_number: int, operations: list[Operation]) -> list[bool]:
    nodes: list[int] = [i for i in range(max_number + 1)]
    results: list[bool] = []
    for operation_type, number_a, number_b in operations:
        if operation_type == UNION_OP:
            union_parents(nodes, number_a, number_b)
        elif operation_type == SEARCH_OP:
            parent_a = find_parent(nodes, number_a)
            parent_b = find_parent(nodes, number_b)
            results.append(parent_a == parent_b)
    return results


def main():
    max_number, operation_count = (int(s) for s in input().split())
    operations: list[Operation] = []
    for _ in range(operation_count):
        op_type, number_a, number_b = (int(s) for s in stdin.readline().split())
        operation = Operation(op_type, number_a, number_b)
        operations.append(operation)
    results = perform_operations(max_number, operations)
    for result in results:
        stdout.write("YES\n" if result else "NO\n")


main()
