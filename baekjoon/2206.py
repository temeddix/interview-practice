import sys
from collections import deque

BlockMap = list[list[bool]]
CountMap = list[list[list[int]]]

Block = tuple[
    int,  # Row
    int,  # Column
    int,  # Whether has broken a wall, 0 or 1
]

START_BLOCK: Block = (0, 0, 0)
UNEXPLORED = -1
MOVEMENT_CANDIDATES = (
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
)


def explore(block_map: BlockMap) -> int:
    map_width = len(block_map[0])
    map_height = len(block_map)

    count_map: CountMap = [
        [[UNEXPLORED, UNEXPLORED] for _ in range(map_width)] for _ in range(map_height)
    ]
    count_map[START_BLOCK[0]][START_BLOCK[1]][START_BLOCK[2]] = 1
    cursors = deque[Block]()
    cursors.append(START_BLOCK)

    while cursors:
        current = cursors.popleft()
        current_count = count_map[current[0]][current[1]][current[2]]
        for movement in MOVEMENT_CANDIDATES:
            new_row = current[0] + movement[0]
            new_col = current[1] + movement[1]
            if not 0 <= new_row < map_height:
                continue
            if not 0 <= new_col < map_width:
                continue
            if block_map[new_row][new_col]:
                if current[2] == 1:
                    continue
                new_sts = 1
            else:
                new_sts = current[2]
            if count_map[new_row][new_col][new_sts] == UNEXPLORED:
                count_map[new_row][new_col][new_sts] = current_count + 1
                new_block = (new_row, new_col, new_sts)
                cursors.append(new_block)

    minimum = count_map[-1][-1][1]
    if minimum == UNEXPLORED:
        minimum = count_map[-1][-1][0]
    return minimum


def main():
    row_count, _ = (int(s) for s in input().split())
    block_map: BlockMap = []
    for _ in range(row_count):
        row = [True if s == "1" else False for s in sys.stdin.readline().strip()]
        block_map.append(row)
    min_movement = explore(block_map)
    print(min_movement)


main()
