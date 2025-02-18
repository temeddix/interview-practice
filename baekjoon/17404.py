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
    dp_array = [[[INVALID] * COLORS for _ in range(COLORS)] for _ in range(houses)]
    for c, cost in enumerate(color_costs[0]):
        dp_array[0][c][c] = cost

    for h in range(1, houses):
        color_cost = color_costs[h]
        dp_current = dp_array[h]
        dp_previous = dp_array[h - 1]
        for c, cost in enumerate(color_cost):
            for fc, lc_list in enumerate(dp_previous):  # First color
                for lc, previous_cost in enumerate(lc_list):  # Last color
                    if previous_cost == INVALID:
                        continue
                    if c == lc:
                        continue
                    recorded_cost = dp_current[fc][c]
                    new_cost = previous_cost + cost
                    if new_cost < recorded_cost:
                        dp_current[fc][c] = new_cost

    min_cost = INVALID
    dp_last = dp_array[-1]
    for fc, lc_list in enumerate(dp_last):
        for lc, cost in enumerate(lc_list):
            if fc != lc:
                min_cost = min(min_cost, cost)

    return min_cost


main()
