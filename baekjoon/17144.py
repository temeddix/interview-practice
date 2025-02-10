from sys import stdin
from typing import NamedTuple


def main():
    r_count, c_count, seconds = (int(s) for s in input().split())
    dusts: list[list[int]] = []
    purifier_spots: list[Spot] = []
    for r in range(r_count):
        row = [int(s) for s in stdin.readline().split()]
        dusts.append(row)
        for c, dust in enumerate(row):
            if dust == PURIFIER_SYMBOL:
                purifier_spots.append(Spot(r, c))
    block_map = BlockMap(r_count, c_count, dusts, Purifier(*purifier_spots))
    remaining_dust = simulate_airflow(block_map, seconds)
    print(remaining_dust)


PURIFIER_SYMBOL = -1


class Spot(NamedTuple):
    r: int  # Row
    c: int  # Column


class Purifier(NamedTuple):
    up: Spot
    down: Spot


class BlockMap(NamedTuple):
    r_count: int
    c_count: int
    dusts: list[list[int]]
    purifier: Purifier


def simulate_airflow(block_map: BlockMap, seconds: int) -> int:
    r_count, c_count, dusts, _ = block_map

    for _ in range(seconds):
        spread_dust(block_map)
        blow_wind(block_map)

    remaining_dust = 0
    for r in range(r_count):
        for c in range(c_count):
            dust = dusts[r][c]
            if dust != PURIFIER_SYMBOL:
                remaining_dust += dust

    return remaining_dust


ADJACENTS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def spread_dust(block_map: BlockMap):
    r_count, c_count, dusts, _ = block_map

    dust_diffs = [[0] * c_count for _ in range(r_count)]

    for r in range(r_count):
        for c in range(c_count):
            if dusts[r][c] == PURIFIER_SYMBOL:
                continue
            spread_amount = dusts[r][c] // 5
            for r_diff, c_diff in ADJACENTS:
                r_new = r + r_diff
                c_new = c + c_diff
                if not 0 <= r_new < r_count or not 0 <= c_new < c_count:
                    continue
                if dusts[r_new][c_new] == PURIFIER_SYMBOL:
                    continue
                dust_diffs[r_new][c_new] += spread_amount
                dust_diffs[r][c] -= spread_amount

    for r in range(r_count):
        for c in range(c_count):
            if dusts[r][c] == PURIFIER_SYMBOL:
                continue
            dusts[r][c] += dust_diffs[r][c]


def blow_wind(block_map: BlockMap):
    r_count, c_count, dusts, purifier = block_map
    up_spot, down_spot = purifier

    r_now, c_now = up_spot
    r_now -= 1
    while r_now - 1 >= 0:
        r_before = r_now - 1
        dust_before = dusts[r_before][c_now]
        dusts[r_now][c_now] = dust_before
        r_now -= 1
    while c_now + 1 < c_count:
        c_before = c_now + 1
        dust_before = dusts[r_now][c_before]
        dusts[r_now][c_now] = dust_before
        c_now += 1
    while r_now + 1 <= up_spot[0]:
        r_before = r_now + 1
        dust_before = dusts[r_before][c_now]
        dusts[r_now][c_now] = dust_before
        r_now += 1
    while c_now - 1 > up_spot[1]:
        c_before = c_now - 1
        dust_before = dusts[r_now][c_before]
        dusts[r_now][c_now] = dust_before
        c_now -= 1
    dusts[r_now][c_now] = 0

    r_now, c_now = down_spot
    r_now += 1
    while r_now + 1 < r_count:
        r_before = r_now + 1
        dust_before = dusts[r_before][c_now]
        dusts[r_now][c_now] = dust_before
        r_now += 1
    while c_now + 1 < c_count:
        c_before = c_now + 1
        dust_before = dusts[r_now][c_before]
        dusts[r_now][c_now] = dust_before
        c_now += 1
    while r_now - 1 >= down_spot[0]:
        r_before = r_now - 1
        dust_before = dusts[r_before][c_now]
        dusts[r_now][c_now] = dust_before
        r_now -= 1
    while c_now - 1 > down_spot[1]:
        c_before = c_now - 1
        dust_before = dusts[r_now][c_before]
        dusts[r_now][c_now] = dust_before
        c_now -= 1
    dusts[r_now][c_now] = 0


main()
