from typing import NamedTuple


def main():
    map_size = int(input())
    sands: list[list[int]] = []
    for _ in range(map_size):
        row = [int(s) for s in input().split()]
        sands.append(row)
    block_map = BlockMap(map_size, sands, [])
    simulate(block_map)
    print(sum(block_map.escaped))


class Spot(NamedTuple):
    row: int
    column: int


class BlockMap(NamedTuple):
    map_size: int
    sands: list[list[int]]
    escaped: list[int]


DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]
DIRECTION_COUNT = len(DIRECTIONS)
SAME_EDGE_COUNT = 2


def simulate(block_map: BlockMap):
    map_size, _, _ = block_map

    direction = 0
    current_spot = Spot(map_size // 2, map_size // 2)

    edge_length = 1
    edge_reached = 0
    straight_dist = 0
    for _ in range(map_size**2 - 1):
        r_diff, c_diff = DIRECTIONS[direction]
        r_now, c_now = current_spot
        r_next, c_next = r_now + r_diff, c_now + c_diff
        next_spot = Spot(r_next, c_next)

        move_tornado(current_spot, next_spot, block_map)
        current_spot = Spot(r_next, c_next)

        straight_dist += 1
        if straight_dist == edge_length:
            edge_reached += 1
            straight_dist = 0
            direction = (direction + 1) % DIRECTION_COUNT
        if edge_reached == SAME_EDGE_COUNT:
            edge_length += 1
            edge_reached = 0
            straight_dist = 0


BOWL_DIST = (2, 0)
SPREAD_SHAPE = {
    (3, 0): 0.05,
    (2, 1): 0.10,
    (2, -1): 0.10,
    (1, 1): 0.07,
    (1, -1): 0.07,
    (1, 2): 0.02,
    (1, -2): 0.02,
    (0, 1): 0.01,
    (0, -1): 0.01,
}


def move_tornado(from_spot: Spot, to_spot: Spot, block_map: BlockMap):
    map_size, sands, escaped = block_map

    r_from, c_from = from_spot
    r_to, c_to = to_spot

    r_front, c_front = r_to - r_from, c_to - c_from  # Front direction vector
    r_side, c_side = c_front, -r_front  # Right direction vector

    sand = sands[r_to][c_to]
    remaining_sand = sand
    sands[r_to][c_to] = 0

    for dist, ratio in SPREAD_SHAPE.items():
        front, side = dist
        r_spread = r_from + (r_front * front) + (r_side * side)
        c_spread = c_from + (c_front * front) + (c_side * side)
        sand_taken = int(sand * ratio)
        remaining_sand -= sand_taken
        if 0 <= r_spread < map_size and 0 <= c_spread < map_size:
            sands[r_spread][c_spread] += sand_taken
        else:
            escaped.append(sand_taken)

    front, side = BOWL_DIST
    r_bowl = r_from + (r_front * front) + (r_side * side)
    c_bowl = c_from + (c_front * front) + (c_side * side)
    if 0 <= r_bowl < map_size and 0 <= c_bowl < map_size:
        sands[r_bowl][c_bowl] += remaining_sand
    else:
        escaped.append(remaining_sand)


main()
