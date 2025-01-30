from sys import stdin


def main():
    node_count = int(input())
    costs: list[list[int]] = []
    for _ in range(node_count):
        cost_row = [int(s) for s in stdin.readline().split()]
        costs.append(cost_row)
    min_cycle_cost = get_min_cycle_cost(node_count, costs)
    print(min_cycle_cost)


INFINITY = 1_000_000_007
INVALID_COST = 0


def get_min_cycle_cost(node_count: int, costs: list[list[int]]) -> int:
    # Because the node count is not bigger than 16,
    # the cells in this DP list is never more than 65536 * 16.
    all_visited = (1 << node_count) - 1  # 2 to the power of node count minus 1
    dp_list = [[INFINITY] * (all_visited + 1) for _ in range(node_count)]

    for second_node in range(1, node_count):
        cost = costs[0][second_node]
        if cost == INVALID_COST:
            continue
        new_visited = 1 << second_node | 1
        dp_list[second_node][new_visited] = cost

    for visited in range(all_visited + 1):
        for current_node in range(1, node_count):
            current_cost = dp_list[current_node][visited]
            if current_cost == INFINITY:
                # Not searched yet.
                continue
            for next_node in range(1, node_count):
                extra_cost = costs[current_node][next_node]
                if extra_cost == INVALID_COST:
                    # There's no road or it's the same city.
                    continue
                if visited & (1 << next_node):
                    # Has already visited the next node.
                    continue
                new_visited = visited | 1 << next_node
                existing_cost = dp_list[next_node][new_visited]
                new_cost = current_cost + extra_cost
                if new_cost < existing_cost:
                    dp_list[next_node][new_visited] = new_cost

    min_cycle_cost = INFINITY
    for last_node in range(1, node_count):
        if costs[last_node][0] == INVALID_COST:
            continue
        extra_cost = costs[last_node][0]
        last_cost = dp_list[last_node][all_visited]
        cycle_cost = last_cost + extra_cost
        min_cycle_cost = min(min_cycle_cost, cycle_cost)

    return min_cycle_cost


main()
