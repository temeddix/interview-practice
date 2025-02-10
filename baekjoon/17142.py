from collections import deque
from itertools import combinations
from sys import stdin
from typing import NamedTuple


def main():
    map_size, start_count = (int(s) for s in input().split())
    start_spots: list[Spot] = []
    blocks: list[list[int]] = []
    for r in range(map_size):
        row = [int(s) for s in stdin.readline().split()]
        blocks.append(row)
        for c, number in enumerate(row):
            if number == VIRUS_SYMBOL:
                start_spots.append(Spot(r, c))
    block_map = BlockMap(map_size, blocks, start_spots)
    min_time = find_min_time(block_map, start_count)
    print(-1 if min_time is None else min_time)


EMPTY_SYMBOL = 0
WALL_SYMBOL = 1
VIRUS_SYMBOL = 2


class Spot(NamedTuple):
    row: int
    column: int


class BlockMap(NamedTuple):
    map_size: int
    blocks: list[list[int]]
    start_spots: list[Spot]


INFINITY = 1_000_000_007


def find_min_time(block_map: BlockMap, start_count: int) -> int | None:
    _, _, start_spots = block_map

    min_time = INFINITY
    for chosen_spots in combinations(start_spots, start_count):
        spread_time = find_spread_time(block_map, list(chosen_spots))
        if spread_time is not None:
            min_time = min(min_time, spread_time)

    return None if min_time == INFINITY else min_time


class Job(NamedTuple):
    spot: Spot
    spread_time: int


MOVEMENTS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def find_spread_time(block_map: BlockMap, chosen_spots: list[Spot]) -> int | None:
    map_size, blocks, _ = block_map
    visited = [[False for _ in r] for r in blocks]

    bfs_deque = deque[Job]()
    for chosen_spot in chosen_spots:
        bfs_deque.append(Job(chosen_spot, 0))

    total_time = 0
    while bfs_deque:
        spot, spread_time = bfs_deque.popleft()
        r, c = spot
        if visited[r][c]:
            continue
        visited[r][c] = True
        if blocks[r][c] == EMPTY_SYMBOL:
            total_time = max(total_time, spread_time)
        for r_diff, c_diff in MOVEMENTS:
            r_new, c_new = r + r_diff, c + c_diff
            if not 0 <= r_new < map_size or not 0 <= c_new < map_size:
                continue
            if blocks[r_new][c_new] == WALL_SYMBOL or visited[r_new][c_new]:
                continue
            bfs_deque.append(Job(Spot(r_new, c_new), spread_time + 1))

    for r in range(map_size):
        for c in range(map_size):
            if blocks[r][c] == EMPTY_SYMBOL and not visited[r][c]:
                return None

    return total_time


main()
