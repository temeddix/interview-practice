from collections import deque

BLOCK_COUNT = 100_001


def explore(start: int, goal: int) -> int:
    blocks = [-1 for _ in range(BLOCK_COUNT)]
    blocks[start] = 0
    cursors = deque[int]()
    cursors.append(start)

    while cursors:
        current = cursors.popleft()
        current_seconds = blocks[current]
        if current == goal:
            return current_seconds
        for next in (current + 1, current - 1, current * 2):
            if not 0 <= next < BLOCK_COUNT:
                continue
            if blocks[next] == -1:
                blocks[next] = current_seconds + 1
                cursors.append(next)

    raise ValueError


def main():
    start, goal = (int(s) for s in input().split())
    min_seconds = explore(start, goal)
    print(min_seconds)


main()
