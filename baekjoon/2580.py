import sys
from itertools import product
from typing import Generator

ALL_NUMBERS = set([1, 2, 3, 4, 5, 6, 7, 8, 9])


class NumberGroup:
    def __init__(self, grid_data: list[list[int]], locs: list[tuple[int, int]]):
        self._grid_data = grid_data
        self._locs = locs
        self._numbers = [self._grid_data[r][c] for r, c in self._locs]

    def try_filling(self) -> bool:
        unused_numbers = ALL_NUMBERS.copy()
        zero_index: tuple[int, int] | None = None
        for row_index, column_index in self._locs:
            number = self._grid_data[row_index][column_index]
            if number == 0:
                zero_index = row_index, column_index
                continue
            unused_numbers.remove(number)
        if len(unused_numbers) != 1:
            return False
        unused_number = unused_numbers.pop()
        if zero_index is None:
            raise NotImplementedError
        row_index, column_index = zero_index
        self._grid_data[row_index][column_index] = unused_number
        return True


class Grid:
    def __init__(self, data: list[list[int]]):
        self._data = data

    def rows(self) -> Generator[NumberGroup, None, None]:
        for row_index in range(9):
            yield NumberGroup(self._data, [(row_index, n) for n in range(9)])

    def columns(self) -> Generator[NumberGroup, None, None]:
        for column_index in range(9):
            yield NumberGroup(self._data, [(n, column_index) for n in range(9)])

    def blocks(self) -> Generator[NumberGroup, None, None]:
        for i in range(3):
            for j in range(3):
                start_row = i * 3
                start_column = j * 3
                locs = product(
                    range(start_row, start_row + 3),
                    range(start_column, start_column + 3),
                )
                yield NumberGroup(self._data, list(locs))

    def count_zeros(self) -> int:
        zero_count = 0
        for row in self._data:
            zero_count += row.count(0)
        return zero_count


def main():
    grid_data: list[list[int]] = []
    for _ in range(9):
        line: str = sys.stdin.readline().strip()
        grid_data.append([int(t) for t in line.split(" ")])
    grid = Grid(grid_data)
    zero_count = grid.count_zeros()
    while zero_count > 0:
        for group in grid.rows():
            success = group.try_filling()
            if success:
                zero_count -= 1
        for group in grid.columns():
            success = group.try_filling()
            if success:
                zero_count -= 1
        for group in grid.blocks():
            success = group.try_filling()
            if success:
                zero_count -= 1
    for row in grid_data:
        print(" ".join(str(n) for n in row))


main()
