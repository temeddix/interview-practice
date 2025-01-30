from sys import stdin
from typing import NamedTuple


def main():
    point_count = int(input())
    points: list[Point] = []
    for _ in range(point_count):
        x, y = (int(s) for s in stdin.readline().split())
        point = Point(x, y)
        points.append(point)
    area = get_polygon_area(points)
    print(f"{area:.1f}")


class Point(NamedTuple):
    x: int
    y: int


def get_polygon_area(points: list[Point]) -> float:
    base_point = points[0]

    total_area = 0.0
    for i in range(len(points) - 2):
        point_a = points[i + 1]
        point_b = points[i + 2]
        new_area = get_triangle_area(point_a, point_b, base_point)
        total_area += new_area

    return abs(total_area)


def get_triangle_area(a: Point, b: Point, c: Point) -> float:
    result = (a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1])) / 2
    return result


main()
