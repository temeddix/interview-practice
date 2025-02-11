from dataclasses import dataclass
from typing import Generator, NamedTuple


def main():
    map_size, piece_count = (int(s) for s in input().split())
    cells: list[list[int]] = []
    for _ in range(map_size):
        row = [int(s) for s in input().split()]
        cells.append(row)
    pieces: list[Piece] = []
    for _ in range(piece_count):
        r, c, m = (int(s) for s in input().split())
        r, c, m = r - 1, c - 1, m - 1
        pieces.append(Piece(Spot(r, c), None, None, DIRECTIONS[m]))
    block_map = BlockMap(map_size, cells)
    turns = move_pieces(pieces, block_map)
    print(-1 if turns is None else turns + 1)


class Direction(NamedTuple):
    row: int
    column: int


DIRECTIONS = [
    Direction(0, 1),
    Direction(0, -1),
    Direction(-1, 0),
    Direction(1, 0),
]

WHITE_SYMBOL = 0
RED_SYMBOL = 1
BLUE_SYMBOL = 2

GOAL_STACK = 4


class Spot(NamedTuple):
    row: int
    column: int


@dataclass
class Piece:
    spot: Spot
    above: "Piece | None"
    below: "Piece | None"
    direction: Direction


class BlockMap(NamedTuple):
    map_size: int
    cells: list[list[int]]


ATTEMPTS = 1000
MAX_FLIP = 2


def move_pieces(pieces: list[Piece], block_map: BlockMap) -> int | None:
    map_size, cells = block_map

    tracker: list[list[Piece | None]] = [[None for _ in r] for r in cells]
    for piece in pieces:
        r, c = piece.spot
        tracker[r][c] = piece

    for i in range(ATTEMPTS):
        for piece in pieces:
            # Get the information of the piece.
            r, c = piece.spot
            r_move, c_move = piece.direction
            r_next, c_next = r + r_move, c + c_move

            # Flip the direction if there's no space.
            is_inside = 0 <= r_next < map_size and 0 <= c_next < map_size
            if not is_inside or cells[r_next][c_next] == BLUE_SYMBOL:
                r_move, c_move = r_move * -1, c_move * -1
                r_next, c_next = r + r_move, c + c_move
                piece.direction = Direction(r_move, c_move)
            is_inside = 0 <= r_next < map_size and 0 <= c_next < map_size
            if not is_inside or cells[r_next][c_next] == BLUE_SYMBOL:
                continue

            # Pick up the piece.
            below_piece = piece.below
            if below_piece is None:
                tracker[r][c] = None
            else:
                below_piece.above = None
                piece.below = None

            # Reverse the upper stack if the new spot is red.
            color = cells[r_next][c_next]
            base_piece = reverse_upper_stack(piece) if color == RED_SYMBOL else piece

            # Put down the piece.
            for stack_piece in get_upper_stack(base_piece):
                stack_piece.spot = Spot(r_next, c_next)
            existing_piece = tracker[r_next][c_next]
            if existing_piece is not None:
                top_piece = get_stack_top(existing_piece)
                top_piece.above = base_piece
                base_piece.below = top_piece
            else:
                tracker[r_next][c_next] = base_piece

            # Check the stack size
            bottom_piece = tracker[r_next][c_next]
            if bottom_piece is None:
                raise ValueError
            if count_upper_stack(bottom_piece) >= GOAL_STACK:
                return i

    return None


def get_upper_stack(piece: Piece) -> Generator[Piece, None, None]:
    current_piece = piece
    while current_piece is not None:
        yield current_piece
        current_piece = current_piece.above


def get_stack_top(piece: Piece) -> Piece:
    current_piece = piece
    while True:
        if current_piece.above is None:
            return current_piece
        current_piece = current_piece.above


def count_upper_stack(piece: Piece) -> int:
    count = 0
    current_piece = piece
    while current_piece is not None:
        count += 1
        current_piece = current_piece.above
    return count


def reverse_upper_stack(piece: Piece) -> Piece:
    chain: list[Piece] = []
    current_piece = piece
    while current_piece is not None:
        chain.append(current_piece)
        current_piece = current_piece.above
    chain.reverse()

    chain[0].below = chain[-1].below
    chain[-1].above = None

    for p in range(len(chain) - 1):
        this_piece = chain[p]
        above_piece = chain[p + 1]
        above_piece.below = this_piece
        this_piece.above = above_piece

    return chain[0]


main()
