import sys

Location = tuple[int, int]
DpGrid = list[list[int]]
GridMap = list[list[int]]


def get_path_count(grid_map: GridMap) -> int:
    row_count = len(grid_map)
    column_count = len(grid_map[0])

    locations: list[Location] = []
    for row in range(row_count):
        if row == 0:
            locations.extend((row, c) for c in range(1, column_count))
            continue
        locations.extend((row, c) for c in range(column_count))
    locations.sort(key=lambda o: grid_map[o[0]][o[1]], reverse=True)

    dp_grid: DpGrid = [[0 for _ in range(column_count)] for _ in range(row_count)]
    dp_grid[0][0] = 1
    for location in locations:
        row = location[0]
        column = location[1]
        dp_value = 0
        for prev_step in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            prev_row = row + prev_step[0]
            prev_column = column + prev_step[1]
            if not 0 <= prev_row < row_count:
                continue
            if not 0 <= prev_column < column_count:
                continue
            prev_elevation = grid_map[prev_row][prev_column]
            if not prev_elevation > grid_map[row][column]:
                continue
            dp_value += dp_grid[prev_row][prev_column]
        dp_grid[row][column] = dp_value

    return dp_grid[-1][-1]


def main():
    row_count, _ = (int(s) for s in input().split())
    grid_map: GridMap = []
    for _ in range(row_count):
        row = [int(s) for s in sys.stdin.readline().split()]
        grid_map.append(row)
    path_count = get_path_count(grid_map)
    print(path_count)


main()
