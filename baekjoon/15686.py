from itertools import combinations
from sys import stdin
from typing import NamedTuple


def main():
    map_size, final_store_count = (int(s) for s in input().split())
    stores: list[Spot] = []
    houses: list[House] = []
    for i in range(map_size):
        row = [int(s) for s in stdin.readline().split()]
        for j, value in enumerate(row):
            if value == HOUSE_SYMBOL:
                houses.append(House(Spot(i, j), []))
            elif value == STORE_SYMBOL:
                stores.append(Spot(i, j))
    compute_distances(houses, stores)
    min_total_distance = find_min_total_distance(houses, final_store_count)
    print(min_total_distance)


HOUSE_SYMBOL = 1
STORE_SYMBOL = 2


class Spot(NamedTuple):
    row: int
    column: int


class House(NamedTuple):
    spot: Spot
    distances: list[int]


def compute_distances(houses: list[House], stores: list[Spot]):
    for store_spot in stores:
        store_row, store_column = store_spot
        for house in houses:
            house_spot, distances = house
            house_row, house_column = house_spot
            distance = abs(house_row - store_row) + abs(house_column - store_column)
            distances.append(distance)


INFINITY = 1_000_000_007


def find_min_total_distance(houses: list[House], final_store_count: int) -> int:
    store_count = len(houses[0].distances)
    store_indices = list(range(store_count))

    min_total_distance = INFINITY
    for chosen_stores in combinations(store_indices, final_store_count):
        total_distance = 0
        for house in houses:
            _, distances = house
            distance = min(distances[i] for i in chosen_stores)
            total_distance += distance
        min_total_distance = min(min_total_distance, total_distance)

    return min_total_distance


main()
