from sys import stdin
from typing import NamedTuple


def main():
    map_size, fire_ball_count, repeats = (int(s) for s in stdin.readline().split())
    fire_balls = [[list[FireBall]() for _ in range(map_size)] for _ in range(map_size)]
    for _ in range(fire_ball_count):
        r, c, m, s, d = (int(s) for s in stdin.readline().split())
        r, c = r - 1, c - 1
        fire_balls[r][c].append(FireBall(m, d, s))
    block_map = BlockMap(map_size, fire_balls)
    repeat_operations(block_map, repeats)
    total_mass = sum(sum(sum(b[0] for b in c) for c in r) for r in block_map.fire_balls)
    print(total_mass)


class FireBall(NamedTuple):
    mass: int
    direction: int
    speed: int


class Spot(NamedTuple):
    row: int
    column: int


class BufferItem(NamedTuple):
    spot: Spot
    fire_ball: FireBall


class BlockMap(NamedTuple):
    map_size: int
    fire_balls: list[list[list[FireBall]]]


DIRECTIONS = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def repeat_operations(block_map: BlockMap, repeats: int):
    for _ in range(repeats):
        move_fire_balls(block_map)
        make_interaction(block_map)


def move_fire_balls(block_map: BlockMap):
    map_size, fire_balls = block_map

    buffer: list[BufferItem] = []

    for r in range(map_size):
        for c in range(map_size):
            cell = fire_balls[r][c]
            for fire_ball in cell:
                mass, direction, speed = fire_ball
                r_unit, c_unit = DIRECTIONS[direction]
                r_new, c_new = r + r_unit * speed, c + c_unit * speed
                r_new, c_new = r_new % map_size, c_new % map_size
                buffer_item = BufferItem(
                    Spot(r_new, c_new),
                    FireBall(mass, direction, speed),
                )
                buffer.append(buffer_item)
            cell.clear()

    for spot, fire_ball in buffer:
        r, c = spot
        fire_balls[r][c].append(fire_ball)


INTERACTION_THRESHOLD = 2


def make_interaction(block_map: BlockMap):
    map_size, fire_balls = block_map

    for r in range(map_size):
        for c in range(map_size):
            cell = fire_balls[r][c]

            if len(cell) < INTERACTION_THRESHOLD:
                continue

            each_mass = sum(b[0] for b in cell) // 5
            if each_mass == 0:
                cell.clear()
                continue
            each_speed = sum(b[2] for b in cell) // len(cell)

            all_odd = True
            all_even = True
            for fire_ball in cell:
                if fire_ball[1] % 2 == 0:
                    all_odd = False
                else:
                    all_even = False
            go_diagonally = int(not (all_odd or all_even))
            new_directions = (i * 2 + go_diagonally for i in range(4))

            cell.clear()
            cell.extend(FireBall(each_mass, d, each_speed) for d in new_directions)


main()
