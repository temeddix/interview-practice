import sys
from collections import deque

BlockMap = list[list[bool]]

Block = tuple[
    int,  # Row
    int,  # Column
]


def choose_start_cabbage(block_map: BlockMap) -> Block | None:
    for i, row in enumerate(block_map):
        for j, value in enumerate(row):
            if value:
                return (i, j)
    return None


def collect_group(block_map: BlockMap, start_cabbage: Block) -> list[Block]:
    map_width = len(block_map[0])
    map_height = len(block_map)
    cursors = deque[Block]()
    cursors.append(start_cabbage)
    group: list[Block] = [start_cabbage]
    block_map[start_cabbage[0]][start_cabbage[1]] = False

    while cursors:
        current = cursors.popleft()
        for movement in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            new_row = current[0] + movement[0]
            new_col = current[1] + movement[1]
            if not 0 <= new_row < map_height:
                continue
            if not 0 <= new_col < map_width:
                continue
            if block_map[new_row][new_col]:
                block_map[new_row][new_col] = False
                new_block = (new_row, new_col)
                cursors.append(new_block)
                group.append(new_block)

    return group


def group_cabbages(block_map: BlockMap) -> list[list[Block]]:
    grouped_cabbages: list[list[Block]] = []

    while True:
        start_cabbage = choose_start_cabbage(block_map)
        if start_cabbage is None:
            break
        group = collect_group(block_map, start_cabbage)
        grouped_cabbages.append(group)

    return grouped_cabbages


def main():
    test_cases = int(input())
    for _ in range(test_cases):
        column_count, row_count, cabbage_count = (int(s) for s in input().split())
        block_map: BlockMap = [
            [False for _ in range(column_count)] for _ in range(row_count)
        ]
        for _ in range(cabbage_count):
            column, row = (int(s) for s in sys.stdin.readline().split())
            block_map[row][column] = True
        groups = group_cabbages(block_map)
        print(len(groups))


main()
