from sys import stdin
from typing import NamedTuple


def main():
    dragon_count = int(input())
    dragons: list[Dragon] = []
    for _ in range(dragon_count):
        x, y, d, g = (int(s) for s in stdin.readline().split())
        dragon = create_dragon(Point(x, y), DIRECTIONS[d], g)
        dragons.append(dragon)
    full_squares = count_full_squares(dragons)
    print(full_squares)


class Point(NamedTuple):
    x: int
    y: int


class Vector(NamedTuple):
    x: int
    y: int


class Dragon(NamedTuple):
    generation: int
    points: list[Point]


DIRECTIONS = {
    0: Vector(1, 0),
    1: Vector(0, -1),
    2: Vector(-1, 0),
    3: Vector(0, 1),
}


# Rotates points 90 degrees clockwise.
def rotate_points(points: list[Point], base: Point) -> list[Point]:
    result: list[Point] = []
    for point in points:
        x_diff = point[0] - base[0]
        y_diff = point[1] - base[1]
        result.append(Point(base[0] - y_diff, base[1] + x_diff))
    return result


def create_dragon(base: Point, start_vector: Vector, generation: int) -> Dragon:
    # Zero generation status.
    next_point = Point(base[0] + start_vector[0], base[1] + start_vector[1])
    points: list[Point] = [base, next_point]

    # Repeat growing the dragon.
    for _ in range(generation):
        new_points = rotate_points(points[:-1], points[-1])
        points.extend(reversed(new_points))

    return Dragon(generation, points)


GRID_SIZE = 100


def count_full_squares(dragons: list[Dragon]) -> int:
    # Mark points where dragon curves exist.
    marks = [[False] * (GRID_SIZE + 1) for _ in range(GRID_SIZE + 1)]
    for dragon in dragons:
        for point in dragon.points:
            x, y = point
            marks[x][y] = True

    # Count squares with all vertices marked.
    full_squares = 0
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            is_full = (
                marks[x][y]
                and marks[x + 1][y]
                and marks[x][y + 1]
                and marks[x + 1][y + 1]
            )
            if is_full:
                full_squares += 1

    return full_squares


main()
