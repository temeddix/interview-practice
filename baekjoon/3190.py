from collections import deque
from sys import stdin
from typing import NamedTuple


def main():
    board_size = int(input())
    apple_count = int(input())
    apples = set[Spot]()
    for _ in range(apple_count):
        row, column = (int(s) for s in stdin.readline().split())
        row -= 1
        column -= 1
        apple = Spot(row, column)
        apples.add(apple)
    rotate_count = int(input())
    rotations: list[Rotation] = []
    for _ in range(rotate_count):
        time, alphabet = (s for s in stdin.readline().split())
        is_right = alphabet == "D"
        rotation = Rotation(int(time), is_right)
        rotations.append(rotation)
    seconds = move_until_collision(board_size, apples, rotations)
    print(seconds)


class Spot(NamedTuple):
    row: int
    column: int


class Rotation(NamedTuple):
    time: int
    is_right: bool  # Left if false, right if true


class Direction(NamedTuple):
    vertical: int  # -1, 0, 1
    horizontal: int  # -1, 0, 1


START_SPOT = Spot(0, 0)


def move_until_collision(
    board_size: int,
    apples: set[Spot],
    rotations: list[Rotation],
) -> int:
    snake_direction = Direction(0, 1)
    snake_space = set[Spot]([Spot(0, 0)])
    snake_shape = deque[Spot]([Spot(0, 0)])

    # Prepare to pop rotations in ascending time order.
    rotations.sort(reverse=True)

    seconds = 0
    while True:
        # Add a second.
        seconds += 1

        # Move the snake.
        last_head = snake_shape[-1]
        head = Spot(
            last_head[0] + snake_direction[0],
            last_head[1] + snake_direction[1],
        )
        if not 0 <= head[0] < board_size or not 0 <= head[1] < board_size:
            break
        if head in snake_space:
            break
        snake_shape.append(head)
        snake_space.add(head)
        if head in apples:
            apples.remove(head)
        else:
            tail = snake_shape.popleft()
            snake_space.remove(tail)

        # Rotate the snake.
        if rotations and rotations[-1][0] == seconds:
            rotation = rotations.pop()
            snake_direction = rotate_direction(snake_direction, rotation[1])

    return seconds


def rotate_direction(direction: Direction, is_right: bool) -> Direction:
    vertical, horizontal = direction
    if is_right:
        rotated = Direction(horizontal, -vertical)
    else:
        rotated = Direction(-horizontal, vertical)
    return rotated


main()
