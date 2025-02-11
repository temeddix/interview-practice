from typing import NamedTuple


def main():
    map_size = int(input())
    blocks: list[list[int]] = []
    for _ in range(map_size):
        row = [int(s) for s in input().split()]
        blocks.append(row)
    block_map = BlockMap(map_size, blocks)
    min_population_diff = find_min_population_diff(block_map)
    print(min_population_diff)


class BlockMap(NamedTuple):
    map_size: int
    blocks: list[list[int]]


class Spot(NamedTuple):
    row: int
    column: int


class DiagonalDiff(NamedTuple):
    diff_a_doubled: int  # Down left axis
    diff_b_doubled: int  # Down right axis


class MidDistrict(NamedTuple):
    top: Spot
    depth_a: int  # Down left axis
    depth_b: int  # Down right axis


INFINITY = 1_000_000_007
DISTRICT_COUNT = 5


def find_min_population_diff(block_map: BlockMap) -> int:
    map_size, blocks = block_map
    min_population_diff = INFINITY

    for top_r in range(map_size - 2):
        for top_c in range(1, map_size - 1):
            top = Spot(top_r, top_c)
            depth_a_max = top_c
            depth_b_max = map_size - top_c - 1
            for depth_a in range(1, depth_a_max + 1):
                for depth_b in range(1, depth_b_max + 1):
                    populations = [0] * DISTRICT_COUNT
                    if not top_r + depth_a + depth_b < map_size:
                        continue
                    mid_district = MidDistrict(top, depth_a, depth_b)
                    for r in range(map_size):
                        for c in range(map_size):
                            district_number = get_district_number(
                                Spot(r, c), mid_district
                            )
                            populations[district_number] += blocks[r][c]
                    population_diff = max(populations) - min(populations)
                    min_population_diff = min(min_population_diff, population_diff)

    return min_population_diff


def get_district_number(spot: Spot, mid_district: MidDistrict) -> int:
    r, c = spot
    top, depth_a, depth_b = mid_district
    top_r, top_c = top

    diagonal_diff = get_diagonal_diff(spot, top)
    diff_a, diff_b = diagonal_diff
    if 0 <= diff_a <= depth_a * 2 and 0 <= diff_b <= depth_b * 2:
        return 4

    if r < top_r + depth_a and c <= top_c and diff_b < 0:
        return 0
    elif r <= top_r + depth_b and top_c < c and diff_a < 0:
        return 1
    elif top_r + depth_a <= r and c < top_c - depth_a + depth_b and diff_a > 0:
        return 2
    elif top_r + depth_b < r and top_c - depth_a + depth_b <= c and diff_b > 0:
        return 3

    raise ValueError


def get_diagonal_diff(spot: Spot, base: Spot) -> DiagonalDiff:
    spot_r, spot_c = spot
    base_r, base_c = base

    r_diff, c_diff = spot_r - base_r, spot_c - base_c
    diff_a_doubled, diff_b_doubled = 0, 0

    diff_a_doubled -= c_diff
    diff_b_doubled += c_diff

    diff_a_doubled += r_diff
    diff_b_doubled += r_diff

    return DiagonalDiff(diff_a_doubled, diff_b_doubled)


main()
