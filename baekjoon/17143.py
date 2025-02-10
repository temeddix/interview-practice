from sys import stdin
from typing import NamedTuple


def main():
    r_count, c_count, shark_count = (int(s) for s in input().split())
    blocks: list[list[Shark | None]] = [[None] * c_count for _ in range(r_count)]
    for _ in range(shark_count):
        r, c, s, d, z = (int(s) for s in stdin.readline().split())
        r, c, d = r - 1, c - 1, d - 1
        blocks[r][c] = Shark(z, s, DIRECTIONS[d])
    block_map = BlockMap(r_count, c_count, blocks)
    caught_sum = simulate_fishing(block_map)
    print(caught_sum)


class Spot(NamedTuple):
    row: int
    column: int


class Direction(NamedTuple):
    vertical: int  # -1, 0, 1
    horizontal: int  # -1, 0, 1


class Shark(NamedTuple):
    size: int
    speed: int
    direction: Direction


class SharkInfo(NamedTuple):
    shark: Shark
    spot: Spot


class BlockMap(NamedTuple):
    r_count: int
    c_count: int
    blocks: list[list[Shark | None]]


DIRECTIONS = [
    Direction(-1, 0),
    Direction(1, 0),
    Direction(0, 1),
    Direction(0, -1),
]


def simulate_fishing(block_map: BlockMap) -> int:
    r_count, c_count, blocks = block_map

    caught_sum = 0

    for fisherman in range(c_count):
        # Catch a shark.
        for r in range(r_count):
            exposed_shark = blocks[r][fisherman]
            if exposed_shark is not None:
                blocks[r][fisherman] = None
                caught_sum += exposed_shark.size
                break

        # Move sharks.
        moved_shark_infos: list[SharkInfo] = []
        for r in range(r_count):
            for c in range(c_count):
                # Get the shark.
                shark = blocks[r][c]
                if shark is None:
                    continue
                blocks[r][c] = None
                # Move the shark.
                shark_info = SharkInfo(shark, Spot(r, c))
                moved_shark_info = move_shark(shark_info, block_map)
                moved_shark_infos.append(moved_shark_info)
        for moved_shark, spot in moved_shark_infos:
            # Set the shark.
            r_new, c_new = spot
            existing_shark = blocks[r_new][c_new]
            if existing_shark is not None:
                chosen_shark = max(existing_shark, moved_shark)
            else:
                chosen_shark = moved_shark
            blocks[r_new][c_new] = chosen_shark

    return caught_sum


def move_shark(shark_info: SharkInfo, block_map: BlockMap) -> SharkInfo:
    r_count, c_count, _ = block_map
    r_max, c_max = r_count - 1, c_count - 1
    shark, spot = shark_info
    size, speed, direction = shark
    row, column = spot
    r_vec, c_vec = direction

    if r_vec == 0:  # Horizontal movement
        remaining_dist = speed % (c_count * 2 - 2)  # Avoid cycles
        while remaining_dist > 0:
            if c_vec < 0:  # Going left
                max_movement = column
                real_movement = min(remaining_dist, max_movement)
                column -= real_movement
                remaining_dist -= real_movement
                if column == 0:
                    c_vec *= -1
            else:  # Going right
                max_movement = c_max - column
                real_movement = min(remaining_dist, max_movement)
                column += real_movement
                remaining_dist -= real_movement
                if column == c_max:
                    c_vec *= -1
    else:  # Vertical movement
        remaining_dist = speed % (r_count * 2 - 2)  # Avoid cycles
        while remaining_dist > 0:
            if r_vec < 0:  # Going up
                max_movement = row
                real_movement = min(remaining_dist, max_movement)
                row -= real_movement
                remaining_dist -= real_movement
                if row == 0:
                    r_vec *= -1
            else:  # Going down
                max_movement = r_max - row
                real_movement = min(remaining_dist, max_movement)
                row += real_movement
                remaining_dist -= real_movement
                if row == r_max:
                    r_vec *= -1

    direction = Direction(r_vec, c_vec)
    spot = Spot(row, column)
    shark = Shark(size, speed, direction)
    return SharkInfo(shark, spot)


main()
