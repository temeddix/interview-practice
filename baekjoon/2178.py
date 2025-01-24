import sys
from collections import deque

BlockMap = list[list[bool]]
CountMap = list[list[int]]

Block = tuple[
    int,  # Row
    int,  # Column
]

START_BLOCK: Block = (0, 0)


def explore(block_map: BlockMap) -> int:
    map_width = len(block_map[0])
    map_height = len(block_map)

    count_map: CountMap = [[0 for _ in range(map_width)] for _ in range(map_height)]
    count_map[START_BLOCK[0]][START_BLOCK[1]] = 1
    explored = set[Block]()
    cursors = deque[Block]()
    explored.add(START_BLOCK)
    cursors.append(START_BLOCK)

    while cursors:
        current = cursors.popleft()
        current_count = count_map[current[0]][current[1]]
        for movement in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            new_row = current[0] + movement[0]
            new_col = current[1] + movement[1]
            if not 0 <= new_row < map_height:
                continue
            if not 0 <= new_col < map_width:
                continue
            new_block = (new_row, new_col)
            if new_block in explored:
                continue
            if block_map[new_row][new_col]:
                count_map[new_row][new_col] = current_count + 1
                explored.add(new_block)
                cursors.append(new_block)

    return count_map[-1][-1]


def main():
    row_count, _ = (int(s) for s in input().split())
    block_map: BlockMap = []
    for _ in range(row_count):
        row = [True if s == "1" else False for s in sys.stdin.readline().strip()]
        block_map.append(row)
    min_movement = explore(block_map)
    print(min_movement)


main()
