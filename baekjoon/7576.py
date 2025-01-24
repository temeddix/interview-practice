import sys
from collections import deque

BlockMap = list[list[int]]

Block = tuple[
    int,  # Row
    int,  # Column
]

NO_TOMATO = -2
UNRIPE_TOMATO = -1


def get_ripening_days(block_map: BlockMap) -> int:
    row_count = len(block_map)
    column_count = len(block_map[0])
    cursors = deque[Block]()

    unripe_tomatos = 0
    for i, row in enumerate(block_map):
        for j, value in enumerate(row):
            if value == 0:
                cursors.append((i, j))
            elif value == UNRIPE_TOMATO:
                unripe_tomatos += 1

    current_day = 0
    while cursors:
        current = cursors.popleft()
        current_day = block_map[current[0]][current[1]]
        for movement in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            next_row = current[0] + movement[0]
            next_column = current[1] + movement[1]
            if not 0 <= next_row < row_count:
                continue
            if not 0 <= next_column < column_count:
                continue
            if block_map[next_row][next_column] == NO_TOMATO:
                continue
            if block_map[next_row][next_column] == UNRIPE_TOMATO:
                block_map[next_row][next_column] = current_day + 1
                cursors.append((next_row, next_column))
                unripe_tomatos -= 1

    if unripe_tomatos:
        return -1
    else:
        return current_day


def main():
    _, row_count = (int(s) for s in input().split())
    block_map: BlockMap = []
    for _ in range(row_count):
        row = [int(s) - 1 for s in sys.stdin.readline().split()]
        block_map.append(row)
    ripening_days = get_ripening_days(block_map)
    print(ripening_days)


main()
