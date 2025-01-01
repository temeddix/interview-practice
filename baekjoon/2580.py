import sys
from itertools import product

ALL_NUMBERS = set([1, 2, 3, 4, 5, 6, 7, 8, 9])


class SudokuSolver:
    def __init__(self, grid: list[list[int]]):
        self._grid = grid

    def _find_empty_cell(self) -> tuple[int, int] | None:
        for row in range(9):
            for column in range(9):
                if self._grid[row][column] == 0:
                    return row, column
        return None

    def _is_valid(self, number: int, row: int, column: int) -> bool:
        # Check if the number is inside the row.
        if number in self._grid[row]:
            return False
        # Check if the number is inside the column.
        if number in (self._grid[i][column] for i in range(9)):
            return False
        # Check if the number in inside theh block.
        block_row, block_column = row // 3 * 3, column // 3 * 3
        locs = product(
            range(block_row, block_row + 3),
            range(block_column, block_column + 3),
        )
        for row, column in locs:
            if self._grid[row][column] == number:
                return False
        return True

    def solve(self):
        empty_cell = self._find_empty_cell()
        if empty_cell is None:
            return True
        row, column = empty_cell

        for number in ALL_NUMBERS:
            if self._is_valid(number, row, column):
                self._grid[row][column] = number
                if self.solve():
                    return True
                # Backtrack.
                self._grid[row][column] = 0

        return False


def main():
    grid_data: list[list[int]] = []
    for _ in range(9):
        line: str = sys.stdin.readline().strip()
        grid_data.append([int(t) for t in line.split(" ")])
    solver = SudokuSolver(grid_data)
    solver.solve()
    for row in grid_data:
        print(" ".join(str(n) for n in row))


main()
