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
    cleanup: bool
    spots: list[Spot]
    sum_value: int


CONNECT_SIZE = 4


def find_max_sum(block_map: list[list[int]]) -> int:
    # Simply use DFS to find the maximum sum of
    # connected 4 blocks.

    map_height = len(block_map)
    map_width = len(block_map[0])

    visited = [[False] * map_width for _ in range(map_height)]

    max_sum = 0
    for start_row in range(map_height):
        for start_column in range(map_width):
            max_sum_from_start = find_max_sum_from_start(
                Spot(start_row, start_column), block_map, visited
            )
            max_sum = max(max_sum, max_sum_from_start)
            visited[start_row][start_column] = True

    return max_sum


def find_max_sum_from_start(
    start_spot: Spot,
    block_map: list[list[int]],
    visited: list[list[bool]],
) -> int:
    map_height = len(block_map)
    map_width = len(block_map[0])

    max_sum = 0
    dfs_stack: list[Job] = [
        Job(True, [start_spot], block_map[start_spot[0]][start_spot[1]]),
        Job(False, [start_spot], block_map[start_spot[0]][start_spot[1]]),
    ]
    while dfs_stack:
        cleanup, spots, sum_value = dfs_stack.pop()
        last_spot = spots[-1]
        if cleanup:
            visited[last_spot[0]][last_spot[1]] = False
            continue
        if len(spots) == CONNECT_SIZE:
            max_sum = max(max_sum, sum_value)
            continue
        visited[last_spot[0]][last_spot[1]] = True
        for spot in spots:
            for row_shift, column_shift in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                next_spot = Spot(spot[0] + row_shift, spot[1] + column_shift)
                if not 0 <= next_spot[0] < map_height:
                    continue
                if not 0 <= next_spot[1] < map_width:
                    continue
                if visited[next_spot[0]][next_spot[1]]:
                    continue
                next_spots = spots + [next_spot]
                next_sum = sum_value + block_map[next_spot[0]][next_spot[1]]
                dfs_stack.append(Job(True, next_spots, next_sum))
                dfs_stack.append(Job(False, next_spots, next_sum))

    return max_sum


main()
