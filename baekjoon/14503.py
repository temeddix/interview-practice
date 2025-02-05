from typing import NamedTuple


def main():
    map_height, map_width = (int(s) for s in input().split())
    start_row, start_column, facing = (int(s) for s in input().split())
    robot = Robot(Spot(start_row, start_column), facing)

    walls: list[list[bool]] = []
    for _ in range(map_height):
        row = [True if s == "1" else False for s in input().split()]
        walls.append(row)
    map_info = MapInfo(map_height, map_width, walls)

    clean_block_count = count_clean_blocks(map_info, robot)
    print(clean_block_count)


class Spot(NamedTuple):
    row: int
    column: int


class MapInfo(NamedTuple):
    height: int
    width: int
    walls: list[list[bool]]


class Robot(NamedTuple):
    spot: Spot
    facing: int


FACING_NORTH = 0
FACING_EAST = 1
FACING_SOUTH = 2
FACING_WEST = 3

DIRECTIONS = {
    FACING_NORTH: (-1, 0),
    FACING_EAST: (0, 1),
    FACING_SOUTH: (1, 0),
    FACING_WEST: (0, -1),
}

ALL_DIRECTIONS = list(DIRECTIONS.values())


def count_clean_blocks(map_info: MapInfo, robot: Robot) -> int:
    map_height, map_width, _ = map_info

    clean_block_count = 0
    cleaned = [[False] * map_width for _ in range(map_height)]

    while True:
        (row, column), facing = robot

        if not cleaned[row][column]:
            clean_block_count += 1
            cleaned[row][column] = True

        near_spots = [Spot(row + v, column + h) for v, h in ALL_DIRECTIONS]
        near_spots = [s for s in near_spots if is_spot_available(map_info, s)]
        is_dirty = any(not cleaned[r][c] for r, c in near_spots)

        if is_dirty:
            for _ in range(4):
                facing = (facing - 1) % 4
                direction = DIRECTIONS[facing]
                front_spot = Spot(row + direction[0], column + direction[1])
                if not is_spot_available(map_info, front_spot):
                    continue
                if not cleaned[front_spot[0]][front_spot[1]]:
                    robot = Robot(front_spot, facing)
                    break

        else:
            direction = DIRECTIONS[facing]
            back_spot = Spot(row - direction[0], column - direction[1])
            if not is_spot_available(map_info, back_spot):
                break
            robot = Robot(back_spot, facing)

    return clean_block_count


def is_spot_available(map_info: MapInfo, spot: Spot) -> bool:
    map_height, map_width, walls = map_info
    row, column = spot
    if not 0 <= row < map_height:
        return False
    if not 0 <= column < map_width:
        return False
    if walls[row][column]:
        return False
    return True


main()
