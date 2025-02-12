from typing import NamedTuple


def main():
    numbers = [int(s) for s in input().split()]
    max_score_sum = move_pieces(numbers)
    print(max_score_sum)


class Node(NamedTuple):
    next_red: int | None
    next_blue: int | None
    score: int


NODES = [
    Node(1, None, 0),  # Start (Index 0)
    Node(2, None, 2),
    Node(3, None, 4),
    Node(4, None, 6),
    Node(5, None, 8),
    Node(6, 23, 10),
    Node(7, None, 12),
    Node(8, None, 14),
    Node(9, None, 16),
    Node(10, None, 18),
    Node(11, 26, 20),
    Node(12, None, 22),
    Node(13, None, 24),
    Node(14, None, 26),
    Node(15, None, 28),
    Node(16, 28, 30),
    Node(17, None, 32),
    Node(18, None, 34),
    Node(19, None, 36),
    Node(20, None, 38),
    Node(21, None, 40),
    Node(None, None, 0),  # End (Index 21)
    Node(31, None, 25),  # Middle (Index 22)
    Node(24, None, 13),  # Left bridge
    Node(25, None, 16),  # Left bridge
    Node(22, None, 19),  # Left bridge
    Node(27, None, 22),  # Down bridge
    Node(22, None, 24),  # Down bridge
    Node(29, None, 28),  # Right bridge
    Node(30, None, 27),  # Right bridge
    Node(22, None, 26),  # Right bridge
    Node(32, None, 30),  # Up bridge
    Node(20, None, 35),  # Up bridge
]

END_INDEX = 21


class Status(NamedTuple):
    moves: int
    score_sum: int
    piece_a: int
    piece_b: int
    piece_c: int
    piece_d: int


def move_pieces(numbers: list[int]) -> int:
    number_count = len(numbers)
    first_status = Status(0, 0, 0, 0, 0, 0)
    dfs_stack: list[Status] = [first_status]

    max_score = 0
    while dfs_stack:
        moves, score_sum, piece_a, piece_b, piece_c, piece_d = dfs_stack.pop()
        if moves == number_count:
            max_score = max(max_score, score_sum)
            continue
        number = numbers[moves]
        pieces = [piece_a, piece_b, piece_c, piece_d]
        for i, piece in enumerate(pieces):
            # Limit the first three pieces for performance.
            if i > moves:
                continue

            # Prepare moving.
            current = piece

            # Perform the first move.
            next_red, next_blue, _ = NODES[current]
            if next_blue is not None:
                current = next_blue
            elif next_red is not None:
                current = next_red

            # Perform other moves.
            for _ in range(number - 1):
                next_red, _, _ = NODES[current]
                if next_red is not None:
                    current = next_red

            # Check that there's no other piece here.
            if current != END_INDEX and current in pieces:
                continue

            # Add the score and move on.
            _, _, score = NODES[current]
            new_score_sum = score_sum + score
            new_pieces = pieces.copy()
            new_pieces[i] = current
            new_status = Status(moves + 1, new_score_sum, *new_pieces)
            dfs_stack.append(new_status)

    return max_score


main()
