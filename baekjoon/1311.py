from itertools import combinations
from typing import Generator, NamedTuple


def main():
    item_count = int(input())
    cost_table: list[list[int]] = []
    for _ in range(item_count):
        row = [int(s) for s in input().split()]
        cost_table.append(row)
    min_cost = find_min_cost(item_count, cost_table)
    print(min_cost)


UNKNOWN = 1_000_000_007


def find_min_cost(item_count: int, cost_table: list[list[int]]) -> int:
    # Index is chosen people represented in bits, value means the minimum cost.
    dp_array = [UNKNOWN] * int(2**item_count)
    dp_array[0] = 0

    for new_item in range(item_count):
        for index in get_indices(item_count, new_item + 1):
            cost = UNKNOWN
            for prev_index, new_person in get_prev_indices(item_count, index):
                new_cost = dp_array[prev_index] + cost_table[new_person][new_item]
                cost = min(cost, new_cost)
            dp_array[index] = cost

    return dp_array[-1]


def get_indices(item_count: int, chosen_people: int) -> Generator[int, None, None]:
    for combination in combinations(range(item_count), chosen_people):
        index = 0
        for person in combination:
            index = index | (1 << person)
        yield index


class PrevInfo(NamedTuple):
    dp_index: int
    new_person: int


def get_prev_indices(item_count: int, index: int) -> Generator[PrevInfo, None, None]:
    for person in range(item_count):
        prev_index = index & ~(1 << person)
        if prev_index != index:
            yield PrevInfo(prev_index, person)


main()
