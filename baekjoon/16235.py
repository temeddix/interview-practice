from collections import deque
from dataclasses import dataclass
from itertools import chain
from sys import stdin
from typing import Generator, NamedTuple


def main():
    map_size, initial_trees, years = (int(s) for s in input().split())
    lands: list[list[Land]] = []
    for _ in range(map_size):
        yearly_nutrients = [int(s) for s in stdin.readline().split()]
        row = [Land(5, n, deque()) for n in yearly_nutrients]
        lands.append(row)
    for _ in range(initial_trees):
        row, column, age = (int(s) for s in stdin.readline().split())
        row -= 1
        column -= 1
        lands[row][column].trees.append(age)
    final_trees = simulate_farming(map_size, lands, years)
    print(final_trees)


class Spot(NamedTuple):
    row: int
    column: int


@dataclass
class Land:
    nutrient: int
    yearly_nutrient: int
    trees: deque[int]  # Always sorted


def simulate_farming(map_size: int, lands: list[list[Land]], years: int) -> int:
    for _ in range(years):
        # Spring and summer
        for land in chain(*lands):
            trees = land.trees
            surviving_trees = 0
            for tree in trees:
                if land.nutrient < tree:
                    break
                land.nutrient -= tree
                surviving_trees += 1
            dying_trees = len(trees) - surviving_trees
            for _ in range(dying_trees):
                dying_tree = trees.pop()
                land.nutrient += dying_tree // 2
            for _ in range(surviving_trees):
                trees.append(trees.popleft() + 1)

        # Autumn
        for r, row in enumerate(lands):
            for c, land in enumerate(row):
                for tree in land.trees:
                    if tree % 5 == 0:
                        for nearby_spot in get_nearby_spots(Spot(r, c), map_size):
                            nearby_row, nearby_column = nearby_spot
                            lands[nearby_row][nearby_column].trees.appendleft(1)

        # Winter
        for land in chain(*lands):
            land.nutrient += land.yearly_nutrient

    return sum(len(n.trees) for n in chain(*lands))


NEARBY_VECTORS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def get_nearby_spots(spot: Spot, map_size: int) -> Generator[Spot, None, None]:
    row, column = spot
    for row_diff, column_diff in NEARBY_VECTORS:
        new_row, new_column = row + row_diff, column + column_diff
        if 0 <= new_row < map_size and 0 <= new_column < map_size:
            yield Spot(new_row, new_column)


main()
