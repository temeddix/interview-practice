from sys import stdin
from typing import NamedTuple


def main():
    node_count = int(input())
    costs: list[list[int]] = []
    for _ in range(node_count):
        cost_row = [int(s) for s in stdin.readline().split()]
        costs.append(cost_row)
    min_cycle_cost = get_min_cycle_cost(node_count, costs)
    print(min_cycle_cost)


START_NODE = 0
INFINITY = 1_000_000_007
INVALID_COST = 0


class Cursor(NamedTuple):
    standing: int  # The last standing point
    visited: int  # Bitwise visit status
    cost_sum: int  # Total cost until now


def get_min_cycle_cost(node_count: int, costs: list[list[int]]) -> int:
    # Because the node count is not bigger than 16,
    # the cells in this DP list is never more than 65536 * 16.
    visited_max = 2**node_count
    dp_list = [[INFINITY for _ in range(visited_max)] for _ in range(node_count)]

    # Use DFS, not BFS, to minimize memory usage.
    cursors: list[Cursor] = []
    cursors.append(Cursor(0, 0, 0))

    while cursors:
        cursor = cursors.pop()
        standing, visited, cost_sum = cursor
        prev_cost_sum = dp_list[standing][visited]
        if not cost_sum < prev_cost_sum:
            continue
        dp_list[standing][visited] = cost_sum
        for next_node in range(node_count):
            status = bool(visited & (1 << next_node))  # Bitwise AND
            if status:
                continue
            cost = costs[standing][next_node]
            if cost == INVALID_COST:
                # No road or the same city
                continue
            new_visited = visited | (1 << next_node)  # Bitwise OR
            new_cost_sum = cost_sum + cost
            cursor = Cursor(next_node, new_visited, new_cost_sum)
            cursors.append(cursor)

    return dp_list[START_NODE][-1]


main()
