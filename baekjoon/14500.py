from typing import NamedTuple


def main():
    row_count, _ = (int(s) for s in input().split())
    block_map: list[list[int]] = []
    for _ in range(row_count):
        row = [int(s) for s in input().split()]
        block_map.append(row)
    max_sum = find_max_sum(block_map)
    print(max_sum)


class Spot(NamedTuple):
    row: int
    column: int


class Job(NamedTuple):
    spots: list[Spot]
    sum_value: int


CONNECT_SIZE = 4


def find_max_sum(block_map: list[list[int]]) -> int:
    # Simply use DFS to find the maximum sum of
    # connected 4 blocks.

    map_height = len(block_map)
    map_width = len(block_map[0])

    started_spots = [[False] * map_width for _ in range(map_height)]

    max_sum = 0
    for start_row in range(map_height):
        for start_column in range(map_width):
            max_sum_from_start = find_max_sum_from_start(
                Spot(start_row, start_column), block_map, started_spots
            )
            max_sum = max(max_sum, max_sum_from_start)
            started_spots[start_row][start_column] = True

    return max_sum


def find_max_sum_from_start(
    start_spot: Spot,
    block_map: list[list[int]],
    visited_spots: list[list[bool]],
) -> int:
    map_height = len(block_map)
    map_width = len(block_map[0])

    max_sum = 0
    start_job = Job([start_spot], block_map[start_spot[0]][start_spot[1]])
    dfs_stack: list[Job] = [start_job]
    while dfs_stack:
        spots, sum_value = dfs_stack.pop()
        if len(spots) == CONNECT_SIZE:
            max_sum = max(max_sum, sum_value)
            continue
        for spot in spots:
            for row_shift, column_shift in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                next_spot = Spot(spot[0] + row_shift, spot[1] + column_shift)
                if not 0 <= next_spot[0] < map_height:
                    continue
                if not 0 <= next_spot[1] < map_width:
                    continue
                if visited_spots[next_spot[0]][next_spot[1]]:
                    continue
                if next_spot in spots:
                    continue
                job = Job(
                    spots + [next_spot],
                    sum_value + block_map[next_spot[0]][next_spot[1]],
                )
                dfs_stack.append(job)

    return max_sum


main()
