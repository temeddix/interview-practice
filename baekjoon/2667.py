import sys
from collections import deque

BlockMap = list[list[bool]]

Block = tuple[
    int,  # Row
    int,  # Column
]


def choose_start_house(block_map: BlockMap) -> Block | None:
    for i, row in enumerate(block_map):
        for j, value in enumerate(row):
            if value:
                return (i, j)
    return None


def collect_group(block_map: BlockMap, start_house: Block) -> list[Block]:
    map_size = len(block_map)
    cursors = deque[Block]()
    cursors.append(start_house)
    group: list[Block] = [start_house]
    block_map[start_house[0]][start_house[1]] = False

    while cursors:
        current = cursors.popleft()
        for movement in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            new_row = current[0] + movement[0]
            new_col = current[1] + movement[1]
            if not 0 <= new_row < map_size:
                continue
            if not 0 <= new_col < map_size:
                continue
            if block_map[new_row][new_col]:
                block_map[new_row][new_col] = False
                new_block = (new_row, new_col)
                cursors.append(new_block)
                group.append(new_block)

    return group


def group_houses(block_map: BlockMap) -> list[list[Block]]:
    grouped_houses: list[list[Block]] = []

    while True:
        start_house = choose_start_house(block_map)
        if start_house is None:
            break
        group = collect_group(block_map, start_house)
        grouped_houses.append(group)

    return grouped_houses


def main():
    map_size = int(input())

    block_map: BlockMap = []
    for _ in range(map_size):
        row = [True if s == "1" else False for s in sys.stdin.readline().strip()]
        block_map.append(row)

    grouped_houses = group_houses(block_map)
    print(len(grouped_houses))
    group_sizes = sorted(len(g) for g in grouped_houses)
    for group_size in group_sizes:
        print(group_size)


main()
