from collections import deque
from typing import NamedTuple


def main():
    gears: list[Gear] = []
    for _ in range(4):
        gear_values = [True if s == "1" else False for s in input()]
        gear = Gear(gear_values)
        gears.append(gear)
    operation_count = int(input())
    operations: list[Operation] = []
    for _ in range(operation_count):
        input_a, input_b = input().split()
        operation = Operation(int(input_a) - 1, True if input_b == "1" else False)
        operations.append(operation)
    rotate_gears(gears, operations)
    score = calculate_score(gears)
    print(score)


GEAR_COUNT = 4
SAWTOOTH_COUNT = 8


class Operation(NamedTuple):
    gear_index: int
    direction: bool  # Clockwise if true, counterclockwise if false


class Gear:
    def __init__(self, values: list[bool]):
        # Values are expected to be written from the top
        # in clockwise order.
        # True means south, false means north.
        if len(values) != SAWTOOTH_COUNT:
            raise ValueError
        # Because Python's deque indexing has O(n) time complexity,
        # we use two deques.
        # The first index of the top half is the left sawtooth.
        # The first index of the bottom half is the right sawtooth.
        # Both deques are sorted in clockwise order.
        self._top_half = deque[bool](values[6:] + values[:2])
        self._bottom_half = deque[bool](values[2:6])

    def left_sawtooth(self) -> bool:
        return self._top_half[0]

    def right_sawtooth(self) -> bool:
        return self._bottom_half[0]

    def top_sawtooth(self) -> bool:
        return self._top_half[2]

    def rotate_cw(self):
        popped = self._top_half.pop()
        self._bottom_half.appendleft(popped)
        popped = self._bottom_half.pop()
        self._top_half.appendleft(popped)

    def rotate_ccw(self):
        popped = self._top_half.popleft()
        self._bottom_half.append(popped)
        popped = self._bottom_half.popleft()
        self._top_half.append(popped)


def rotate_gears(gears: list[Gear], operations: list[Operation]):
    for operation in operations:
        # Clockwise if true, counterclockwise if false.
        results: list[bool | None] = [None] * GEAR_COUNT

        gear_index, direction = operation
        results[gear_index] = direction

        # Go to left gears.
        cursor = gear_index - 1
        while cursor >= 0:
            prev_cursor = cursor + 1
            curr_gear = gears[cursor]
            prev_gear = gears[prev_cursor]
            if curr_gear.right_sawtooth() == prev_gear.left_sawtooth():
                break
            results[cursor] = not results[prev_cursor]
            cursor -= 1

        # Go to right gears.
        cursor = gear_index + 1
        while cursor < GEAR_COUNT:
            prev_cursor = cursor - 1
            curr_gear = gears[cursor]
            prev_gear = gears[prev_cursor]
            if curr_gear.left_sawtooth() == prev_gear.right_sawtooth():
                break
            results[cursor] = not results[prev_cursor]
            cursor += 1

        #  Rotate the gears.
        for gear_index, result in enumerate(results):
            if result is None:
                continue
            if result:
                gears[gear_index].rotate_cw()
            else:
                gears[gear_index].rotate_ccw()


def calculate_score(gears: list[Gear]) -> int:
    base = 1

    score = 0
    for gear in gears:
        score += int(gear.top_sawtooth()) * base
        base *= 2

    return score


main()
