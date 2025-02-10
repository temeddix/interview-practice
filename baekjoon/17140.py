from typing import NamedTuple


def main():
    r, c, goal_value = (int(s) for s in input().split())
    r, c = r - 1, c - 1
    interest = Element(r, c)
    array_data: list[list[int]] = []
    for _ in range(3):
        row = [int(s) for s in input().split()]
        array_data.append(row)
    array = Array(array_data)
    repeats = repeat_operation(array, interest, goal_value)
    print(-1 if repeats is None else repeats)


class Element(NamedTuple):
    row: int
    column: int


class Occurence(NamedTuple):
    found: int
    number: int


MAX_NUMBER = 100
TRY_COUNT = 100


class Array:
    def __init__(self, data: list[list[int]]):
        self._row_primary: bool = True
        self._data = data

    def _switch_primary_direction(self):
        old_data = self._data
        r_count, c_count = len(old_data[0]), len(old_data)
        new_data = [[0] * c_count for _ in range(r_count)]

        for r in range(r_count):
            for c in range(c_count):
                new_data[r][c] = old_data[c][r]

        self._row_primary = not self._row_primary
        self._data = new_data

    def _prepare_sorting(self):
        primary_len = len(self._data)
        secondary_len = len(self._data[0])
        if primary_len == secondary_len and not self._row_primary:
            self._switch_primary_direction()
        elif primary_len < secondary_len:
            self._switch_primary_direction()

    def sort_with_occurence(self):
        self._prepare_sorting()

        new_data: list[list[int]] = []
        for row in self._data:
            counter = [0 for _ in range(MAX_NUMBER)]
            for number in row:
                if number == 0:
                    continue
                counter[number - 1] += 1
            occurences: list[Occurence] = []
            for index, count in enumerate(counter):
                occurences.append(Occurence(count, index + 1))
            occurences.sort()
            new_row: list[int] = []
            for found, number in occurences:
                if not found:
                    continue
                new_row.append(number)
                new_row.append(found)
            new_data.append(new_row)

        max_size = max(len(t) for t in new_data)
        max_size = min(100, max_size)
        for row in new_data:
            while len(row) > max_size:
                row.pop()
            row.extend(0 for _ in range(max_size - len(row)))

        self._data = new_data

    def get_value(self, row: int, column: int) -> int | None:
        primary_len = len(self._data)
        secondary_len = len(self._data[0])

        if self._row_primary:
            if primary_len > row and secondary_len > column:
                return self._data[row][column]
            return None
        else:
            if secondary_len > row and primary_len > column:
                return self._data[column][row]
            return None


def repeat_operation(array: Array, interest: Element, goal_value: int) -> int | None:
    row, column = interest

    if array.get_value(row, column) == goal_value:
        return 0

    for i in range(TRY_COUNT):
        array.sort_with_occurence()
        if array.get_value(row, column) == goal_value:
            return i + 1

    return None


main()
