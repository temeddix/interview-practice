from collections import deque
from typing import NamedTuple


def main():
    board_size = int(input())
    row_strings: list[str] = []
    for _ in range(board_size):
        row_string = input()
        row_strings.append(row_string)
    start_state = construct_start_state(row_strings)
    max_number = find_max_number(start_state)
    print(max_number)


class State(NamedTuple):
    numbers: list[list[int | None]]
    max_number: int


class Direction(NamedTuple):
    vertical: int  # -1, 0, 1
    horizontal: int  # -1, 0, 1


class Turn(NamedTuple):
    attempt: int
    state: State


class PushedNumbers(NamedTuple):
    moving_lines: list[list[int]]
    max_number: int


MAX_ATTEMPT = 5
DIRECTIONS = [
    Direction(-1, 0),
    Direction(1, 0),
    Direction(0, -1),
    Direction(0, 1),
]


def construct_start_state(row_strings: list[str]) -> State:
    max_number = 0
    numbers: list[list[int | None]] = []
    for row_string in row_strings:
        raw_row = [int(s) for s in row_string.split()]
        max_number = max(max_number, *raw_row)
        row = [None if i == 0 else i for i in raw_row]
        numbers.append(row)

    start_state = State(numbers, max_number)
    return start_state


def find_max_number(start_state: State) -> int:
    # Use BFS.
    bfs_queue = deque[Turn]()
    bfs_queue.append(Turn(0, start_state))
    max_number = start_state.max_number

    while bfs_queue:
        turn = bfs_queue.popleft()
        attempt, state = turn
        if attempt == MAX_ATTEMPT:
            # Stop using this scenario if attempted enough.
            continue
        next_attempt = attempt + 1
        for direction in DIRECTIONS:
            next_state = move_numbers(direction, state)
            max_number = max(max_number, next_state[1])
            next_turn = Turn(next_attempt, next_state)
            bfs_queue.append(next_turn)

    return max_number


def move_numbers(direction: Direction, state: State) -> State:
    numbers, _ = state
    board_size = len(numbers)

    # Convert grid numbers into moving lines.
    moving_lines: list[list[int]] = []
    if direction.horizontal == 0:
        # Flip the grid diagonally if direction is vertical.
        numbers = flip_diagonally(numbers)
    for row_index in range(board_size):
        row = numbers[row_index]
        moving_line = [i for i in row if i is not None]
        if direction.horizontal > 0 or direction.vertical > 0:
            moving_line.reverse()
        moving_lines.append(moving_line)

    # Push numbers inside moving lines.
    moving_lines, max_number = push_numbers(moving_lines)

    # Convert moving lines into grid numbers.
    result_numbers: list[list[int | None]] = []
    for row_index in range(board_size):
        moving_line = moving_lines[row_index]
        line_length = len(moving_line)
        empty_space = board_size - line_length
        row = moving_line + [None] * empty_space
        if direction.horizontal > 0 or direction.vertical > 0:
            row.reverse()
        result_numbers.append(row)
    if direction.horizontal == 0:
        # Flip the grid diagonally if direction was vertical.
        result_numbers = flip_diagonally(result_numbers)

    return State(result_numbers, max_number)


def flip_diagonally(numbers: list[list[int | None]]) -> list[list[int | None]]:
    board_size = len(numbers)
    flipped: list[list[int | None]] = [[None] * board_size for _ in range(board_size)]
    for i in range(board_size):
        for j in range(board_size):
            flipped[i][j] = numbers[j][i]
    return flipped


def push_numbers(moving_lines: list[list[int]]) -> PushedNumbers:
    merged_lines: list[list[int]] = []
    max_number = 0

    for moving_line in moving_lines:
        merged_line: list[int] = []
        merged_lines.append(merged_line)
        line_length = len(moving_line)

        cursor = 0
        while cursor < line_length:
            # Get the current number.
            number = moving_line[cursor]

            # Get the next number.
            next_cursor = cursor + 1
            if next_cursor < line_length:
                next_number = moving_line[next_cursor]
            else:
                next_number = None

            # Use the original or merged number and move on.
            if number == next_number:
                new_number = number * 2
                max_number = max(max_number, new_number)
                merged_line.append(new_number)
                cursor += 2
            else:
                max_number = max(max_number, number)
                merged_line.append(number)
                cursor += 1

    return PushedNumbers(merged_lines, max_number)


main()
