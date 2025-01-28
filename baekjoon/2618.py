import sys

# On the map
Point = tuple[
    int,  # Row
    int,  # Column
]

# Inside the DP grid
DpCell = tuple[
    int,  # Row
    int,  # Column
]


INFINITY = 1_000_000_000


def get_move(case_a: Point, case_b: Point):
    row_diff = abs(case_a[0] - case_b[0])
    col_diff = abs(case_a[1] - case_b[1])
    return row_diff + col_diff


def backtrack(
    min_moves: list[list[int]],
    prev_cells: list[list[DpCell]],
    case_count: int,
) -> tuple[int, list[int]]:
    min_move = INFINITY
    last_cell: DpCell | None = None
    for i, found_move in enumerate(min_moves[-1]):
        if found_move < min_move:
            min_move = min(min_move, found_move)
            last_cell = (case_count, i)
    for i, found_move in enumerate(r[-1] for r in min_moves):
        if found_move < min_move:
            min_move = min(min_move, found_move)
            last_cell = (i, case_count)
    if last_cell is None:
        raise ValueError

    car_actions: list[int] = []  # 1 or 2
    dp_cursor: DpCell = last_cell
    for _ in range(case_count):
        prev_cell = prev_cells[dp_cursor[0]][dp_cursor[1]]
        if prev_cell[0] == dp_cursor[0]:
            # Car B has moved.
            car_actions.append(2)
        else:
            # Car A has moved.
            car_actions.append(1)
        dp_cursor = prev_cell
    car_actions.reverse()

    return min_move, car_actions


def get_min_move(map_size: int, cases: list[Point]) -> tuple[int, list[int]]:
    case_count = len(cases)
    min_moves: list[list[int]] = [
        [INFINITY for _ in range(case_count + 1)] for _ in range(case_count + 1)
    ]
    prev_cells: list[list[DpCell]] = [
        [(0, 0) for _ in range(case_count + 1)] for _ in range(case_count + 1)
    ]
    min_moves[0][0] = 0

    start_a: Point = (1, 1)
    start_b: Point = (map_size, map_size)

    # Search diagonally inside the DP array.
    for row_col_sum in range(1, case_count * 2 + 1):
        for row in range(0, row_col_sum + 1):
            col = row_col_sum - row
            if row > case_count or col > case_count:
                continue
            if row == col:
                # Two police cars cannot be on the same case.
                continue
            min_move = INFINITY
            prev_cell = (0, 0)
            this_case = max(row, col)
            this_point = cases[this_case - 1]
            if row > col:
                i_range = range(row) if row == col + 1 else range(row - 1, row)
                for i in i_range:
                    # `i` means "last case of car A".
                    last_case = max(i, col)  # This means "last case of both cars".
                    if not this_case == last_case + 1:
                        continue
                    last_point = start_a if i == 0 else cases[i - 1]
                    new_move = get_move(last_point, this_point) + min_moves[i][col]
                    if new_move < min_move:
                        min_move = new_move
                        prev_cell = (i, col)
            else:
                i_range = range(col) if col == row + 1 else range(col - 1, col)
                for i in i_range:
                    # `i` means "last case of car B".
                    last_case = max(row, i)  # This means "last case of both cars".
                    if not this_case == last_case + 1:
                        continue
                    last_point = start_b if i == 0 else cases[i - 1]
                    new_move = get_move(last_point, this_point) + min_moves[row][i]
                    if new_move < min_move:
                        min_move = new_move
                        prev_cell = (row, i)
            min_moves[row][col] = min_move
            prev_cells[row][col] = prev_cell

    return backtrack(min_moves, prev_cells, case_count)


def main():
    map_size = int(input())
    case_count = int(input())
    cases: list[Point] = []
    for _ in range(case_count):
        row, column = (int(s) for s in sys.stdin.readline().split())
        cases.append((row, column))
    min_move, car_actions = get_min_move(map_size, cases)
    print(min_move)
    for car_action in car_actions:
        sys.stdout.write(str(car_action) + "\n")


main()
