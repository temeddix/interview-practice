import sys

ALL_NUMBERS = list(range(1, 10))


class SudokuSolver:
    def __init__(self, grid: list[list[int]]):
        self._grid = grid
        self._empty_cells = self._find_empty_cells()

    def _find_empty_cells(self) -> list[tuple[int, int]]:
        empty_cells: list[tuple[int, int]] = []
        for row in range(9):
            for column in range(9):
                if self._grid[row][column] == 0:
                    empty_cells.append((row, column))
        return empty_cells

    def _is_valid(self, number: int, row: int, column: int) -> bool:
        # Check if the number is inside the row.
        if number in self._grid[row]:
            return False
        # Check if the number is inside the column.
        if number in (self._grid[r][column] for r in range(9)):
            return False
        # Check if the number in inside the block.
        block_row, block_column = row // 3 * 3, column // 3 * 3
        for r in range(block_row, block_row + 3):
            for c in range(block_column, block_column + 3):
                if self._grid[r][c] == number:
                    return False
        return True

    def search(self, empty_cell_index: int = 0):
        if len(self._empty_cells) == empty_cell_index:
            return True
        row, column = self._empty_cells[empty_cell_index]

        for number in ALL_NUMBERS:
            if self._is_valid(number, row, column):
                self._grid[row][column] = number
                if self.search(empty_cell_index + 1):
                    return True
                # Backtrack.
                self._grid[row][column] = 0

        return False


def main():
    grid_data: list[list[int]] = []
    for _ in range(9):
        line = str(sys.stdin.readline()).strip()
        grid_data.append([int(t) for t in line.split(" ")])
    solver = SudokuSolver(grid_data)
    solver.search()
    for row in grid_data:
        print(" ".join(str(n) for n in row))


main()
