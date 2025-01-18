import sys
from collections import deque

Explorer = tuple[int, int]
GridMap = list[list[int]]


def get_path_count(grid_map: GridMap) -> int:
    explorers: deque[Explorer] = deque([(0, 0)])
    row_count = len(grid_map)
    column_count = len(grid_map[0])

    path_count = 0
    while explorers:
        explorer = explorers.popleft()
        elevation = grid_map[explorer[0]][explorer[1]]
        for next_step in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            next_row = explorer[0] + next_step[0]
            next_column = explorer[1] + next_step[1]
            if next_row == row_count - 1 and next_column == column_count - 1:
                path_count += 1
                continue
            if not 0 <= next_row < row_count:
                continue
            if not 0 <= next_column < column_count:
                continue
            if not grid_map[next_row][next_column] < elevation:
                continue
            next_explorer: Explorer = (next_row, next_column)
            explorers.append(next_explorer)

    return path_count


def main():
    row_count, _ = (int(s) for s in input().split())
    grid_map: GridMap = []
    for _ in range(row_count):
        row = [int(s) for s in sys.stdin.readline().split()]
        grid_map.append(row)
    path_count = get_path_count(grid_map)
    print(path_count)


main()
