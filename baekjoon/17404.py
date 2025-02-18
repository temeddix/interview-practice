from sys import stdin
from typing import NamedTuple


def main():
    house_count = int(stdin.readline().strip())
    color_costs: list[ColorCost] = []
    for _ in range(house_count):
        r, g, b = (int(s) for s in stdin.readline().split())
        color_costs.append(ColorCost(r, g, b))
    min_cost = calculate_min_cost(color_costs)
    print(min_cost)


class ColorCost(NamedTuple):
    red: int
    green: int
    blue: int


COLORS = 3
INVALID = 1_000_000_007


def calculate_min_cost(color_costs: list[ColorCost]) -> int:
    houses = len(color_costs)

    initial_r, initial_g, initial_b = color_costs[0]
    cost_sums = [
        [initial_r, INVALID, INVALID],  # Started from red
        [INVALID, initial_g, INVALID],  # Started from green
        [INVALID, INVALID, initial_b],  # Started from blue
    ]

    for i in range(1, houses):
        this_r, this_g, this_b = color_costs[i]
        for cost_sum in cost_sums:
            prev_r, prev_g, prev_b = cost_sum

            # Compute new DP values using only previous state.
            cost_sum[0] = min(prev_g, prev_b) + this_r
            cost_sum[1] = min(prev_r, prev_b) + this_g
            cost_sum[2] = min(prev_r, prev_g) + this_b

    from_r, from_g, from_b = cost_sums
    return min(from_r[1], from_r[2], from_g[0], from_g[2], from_b[0], from_b[1])


main()
