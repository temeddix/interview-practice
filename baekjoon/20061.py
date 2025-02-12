from sys import stdin
from typing import NamedTuple


def main():
    repeat_count = int(input())
    new_blocks: list[NewBlock] = []
    for _ in range(repeat_count):
        t, x, y = (int(s) for s in stdin.readline().split())
        t -= 1
        new_blocks.append(NewBlock(t, Spot(x, y)))
    total_score, filled = add_blocks(new_blocks)
    print(total_score)
    print(filled)


class Spot(NamedTuple):
    row: int
    column: int


class NewBlock(NamedTuple):
    block_type: int
    base_spot: Spot


ROOM_HEIGHT = 6
ROOM_WIDTH = 4


class FinalStatus(NamedTuple):
    total_score: int
    filled_spots: int


def add_blocks(new_blocks: list[NewBlock]) -> FinalStatus:
    room_a = [[False] * ROOM_WIDTH for _ in range(ROOM_HEIGHT)]
    room_b = [[False] * ROOM_WIDTH for _ in range(ROOM_HEIGHT)]

    total_score = 0
    for new_block in new_blocks:
        block_spots_a, block_spots_b = get_block_spots(new_block)
        drop_block(block_spots_a, room_a)
        drop_block(block_spots_b, room_b)
        total_score += delete_full_rows(room_a)
        total_score += delete_full_rows(room_b)
        vacate_two_rows(room_a)
        vacate_two_rows(room_b)

    a_filled = sum(sum(r) for r in room_a)
    b_filled = sum(sum(r) for r in room_b)
    return FinalStatus(total_score, a_filled + b_filled)


def drop_block(block_spots: list[Spot], room: list[list[bool]]):
    while True:
        next_block_spots = [Spot(r + 1, c) for r, c in block_spots]
        if any(r >= ROOM_HEIGHT for r, _ in next_block_spots):
            break
        if any(room[r][c] for r, c in next_block_spots):
            break
        block_spots = next_block_spots
    for r, c in block_spots:
        room[r][c] = True


def delete_full_rows(room: list[list[bool]]) -> int:
    deleted_rows = 0

    while True:
        row_to_delete: int | None = None
        for r, row in enumerate(room):
            if all(row):
                row_to_delete = r
                break
        if row_to_delete is None:
            break
        room.pop(row_to_delete)
        deleted_rows += 1

    for _ in range(deleted_rows):
        room.insert(0, [False] * ROOM_WIDTH)

    return deleted_rows


def vacate_two_rows(room: list[list[bool]]):
    if any(room[0]):
        rows_to_shift = 2
    elif any(room[1]):
        rows_to_shift = 1
    else:
        return

    for _ in range(rows_to_shift):
        room.pop()
        room.insert(0, [False] * ROOM_WIDTH)


NEW_BLOCK_SHAPES = [
    [(0, 0)],
    [(0, 0), (0, 1)],
    [(0, 0), (1, 0)],
]


def get_block_spots(new_block: NewBlock) -> tuple[list[Spot], list[Spot]]:
    block_type, base_spot = new_block
    base_row, base_column = base_spot

    # Get spots in the common area in A coordinate system.
    raw_block_spots_a: list[Spot] = []
    for r_diff, c_diff in NEW_BLOCK_SHAPES[block_type]:
        raw_block_spot = Spot(base_row + r_diff, base_column + c_diff)
        raw_block_spots_a.append(raw_block_spot)

    # Get spots in the common area in B coordinate system.
    raw_block_spots_b = [rotate_spot(s) for s in raw_block_spots_a]

    # Move the blocks to 0 to 1 row range.
    # These represent spots in room A and B in their coordinate system.
    block_spots_a = [Spot(r - base_row, c) for r, c in raw_block_spots_a]
    block_spots_b = [Spot(r - base_column, c) for r, c in raw_block_spots_b]

    return block_spots_a, block_spots_b


def rotate_spot(spot: Spot) -> Spot:
    row, column = spot
    return Spot(column, ROOM_WIDTH - 1 - row)


main()
