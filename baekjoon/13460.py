from collections import deque
from typing import NamedTuple


def main():
    row_count, _ = (int(s) for s in input().split())
    row_strings: list[str] = []
    for _ in range(row_count):
        row_string = input()
        row_strings.append(row_string)
    block_map, start_state = construct_map(row_strings)
    min_attempts = find_min_attempts(block_map, start_state)
    print(-1 if min_attempts is None else min_attempts)


class Place(NamedTuple):
    row: int
    col: int


class BlockMap(NamedTuple):
    walls: list[list[bool]]
    hole: Place


class State(NamedTuple):
    red: Place
    blue: Place


class Direction(NamedTuple):
    vertical: int  # -1, 0, 1
    horizontal: int  # -1, 0, 1


class Turn(NamedTuple):
    prev_direction: Direction | None
    attempt: int
    state: State


class RedArrivedError(Exception):
    pass


class BlueArrivedError(Exception):
    pass


class BothArrivedError(Exception):
    pass


MAX_ATTEMPT = 10
DIRECTIONS = [
    Direction(-1, 0),
    Direction(1, 0),
    Direction(0, -1),
    Direction(0, 1),
]


def construct_map(row_strings: list[str]) -> tuple[BlockMap, State]:
    walls: list[list[bool]] = []
    hole: Place | None = None
    red: Place | None = None
    blue: Place | None = None

    for i, row_string in enumerate(row_strings):
        row: list[bool] = []
        for j, letter in enumerate(row_string):
            if letter == "#":
                row.append(True)
            else:
                row.append(False)
                if letter == "O":
                    hole = Place(i, j)
                elif letter == "R":
                    red = Place(i, j)
                elif letter == "B":
                    blue = Place(i, j)
        walls.append(row)

    if hole is None or red is None or blue is None:
        raise ValueError

    block_map = BlockMap(walls, hole)
    start_state = State(red, blue)

    return block_map, start_state


def find_min_attempts(block_map: BlockMap, start_state: State) -> int | None:
    # Use hashing to check if a state has already happend.
    visited = set[State]()

    # Note the minimum attempts possible.
    min_attempts: int | None = None

    # Use BFS.
    bfs_queue = deque[Turn]()
    bfs_queue.append(Turn(None, 0, start_state))
    visited.add(start_state)

    while bfs_queue:
        prev_direction, attempt, state = bfs_queue.popleft()
        if attempt == MAX_ATTEMPT or min_attempts is not None:
            # Give up on this scenario on too many attempts.
            continue
        next_attempt = attempt + 1
        for direction in DIRECTIONS:
            if direction == prev_direction:
                # There's no point of shifting marbles
                # to the same direction again.
                continue
            try:
                next_state = move_marbles(direction, block_map, state)
            except RedArrivedError:
                min_attempts = next_attempt
                break
            except (BlueArrivedError, BothArrivedError):
                continue
            if next_state not in visited:
                visited.add(next_state)
                bfs_queue.append(Turn(direction, next_attempt, next_state))

    return min_attempts


def move_marbles(direction: Direction, block_map: BlockMap, prev_state: State) -> State:
    walls, hole = block_map
    red: Place | None  # None if fallen into the hole
    blue: Place | None  # None if fallen into the hole
    red, blue = prev_state
    vertical, horizontal = direction

    red_finished = False
    blue_finished = False

    while not (red_finished and blue_finished):
        # Try moving both marbles at the same time,
        # only one block of distance per iteration.
        if red_finished or red is None:
            next_red = red
        else:
            next_red = Place(red[0] + vertical, red[1] + horizontal)
            if walls[next_red[0]][next_red[1]]:
                red_finished = True
                continue
        if blue_finished or blue is None:
            next_blue = blue
        else:
            next_blue = Place(blue[0] + vertical, blue[1] + horizontal)
            if walls[next_blue[0]][next_blue[1]]:
                blue_finished = True
                continue

        # Check that marbles doesn't overlap.
        if next_red == next_blue:
            red_finished = True
            blue_finished = True
            continue

        # Check any marble has reached a hole.
        if next_red == hole:
            red_finished = True
            next_red = None
        if next_blue == hole:
            blue_finished = True
            next_blue = None

        # Remember the state after moving.
        red = next_red
        blue = next_blue

    if blue is None:
        raise BothArrivedError if red is None else BlueArrivedError
    if red is None:
        raise RedArrivedError

    return State(red, blue)


main()
