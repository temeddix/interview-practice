from collections import deque
from typing import NamedTuple


def main():
    belt_size, stop_threshold = (int(s) for s in input().split())
    durabilities = [int(s) for s in input().split()]
    exposed = durabilities[:belt_size]
    hidden = deque(reversed(durabilities[belt_size:]))
    belt = Belt(belt_size, exposed, hidden)
    turns = operate(belt, stop_threshold)
    print(turns)


class Belt(NamedTuple):
    size: int
    exposed: list[int]
    hidden: deque[int]


def operate(belt: Belt, stop_threshold: int) -> int:
    size, exposed, hidden = belt
    turn = 0

    retired_cells = 0
    robots: list[bool] = [False] * size
    while True:
        # Add a turn
        turn += 1

        # Rotate the belt and remove the last robot.
        hidden.append(exposed.pop())
        exposed.insert(0, hidden.popleft())
        robots.pop()
        robots.insert(0, False)
        robots[-1] = False

        # Move all robots.
        cursor = size - 1
        while cursor > 0:
            if robots[cursor - 1] and not robots[cursor] and exposed[cursor]:
                robots[cursor - 1] = False
                robots[cursor] = True
                exposed[cursor] -= 1
                if exposed[cursor] == 0:
                    retired_cells += 1
                robots[-1] = False
            cursor -= 1

        # Add the robot to the first cell.
        if exposed[0]:
            robots[0] = True
            exposed[0] -= 1
            if exposed[0] == 0:
                retired_cells += 1

        # Check retired cells and stop if enough.
        if retired_cells >= stop_threshold:
            return turn


main()
