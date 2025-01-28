from collections import deque

MAX_INDEX = 100_000

NO_PREV = -1
EMPTY = 1_000_000_007


Record = tuple[
    int,  # Steps
    int,  # Previous
]

Cursor = tuple[
    int,  # Current
    int,  # Steps
    int,  # Previous
]


def find_shortest_path(start: int, goal: int) -> list[int]:
    # Point records with previous values.
    records: list[Record] = [(EMPTY, NO_PREV) for _ in range(MAX_INDEX + 1)]

    cursors = deque[Cursor]()
    cursors.append((start, 0, NO_PREV))

    while cursors:
        current, steps, previous = cursors.popleft()
        if not steps < records[current][0]:
            continue
        records[current] = (steps, previous)
        next = current - 1
        if 0 <= next <= MAX_INDEX:
            cursors.append((next, steps + 1, current))
        next = current + 1
        if 0 <= next <= MAX_INDEX:
            cursors.append((next, steps + 1, current))
        next = current * 2
        if 0 <= next <= MAX_INDEX:
            cursors.append((next, steps + 1, current))

    shortest_path: list[int] = [goal]
    backtracker = goal
    while backtracker != start:
        backtracker = records[backtracker][1]
        shortest_path.append(backtracker)
    shortest_path.reverse()

    return shortest_path


def main():
    start, goal = (int(s) for s in input().split())
    shortest_path = find_shortest_path(start, goal)
    print(len(shortest_path) - 1)
    print(" ".join(str(i) for i in shortest_path))


main()
