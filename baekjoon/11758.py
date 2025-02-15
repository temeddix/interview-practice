from typing import NamedTuple


def main():
    a_x, a_y = (int(s) for s in input().split())
    b_x, b_y = (int(s) for s in input().split())
    c_x, c_y = (int(s) for s in input().split())

    vec_a = Vector(b_x - a_x, b_y - a_y)
    vec_b = Vector(c_x - b_x, c_y - b_y)
    cross_product = get_cross_product(vec_a, vec_b)
    print(-1 if cross_product < 0 else 1 if cross_product != 0 else 0)


class Vector(NamedTuple):
    x: int
    y: int


def get_cross_product(vec_a: Vector, vec_b: Vector) -> int:
    a_x, a_y = vec_a
    b_x, b_y = vec_b
    return a_x * b_y - b_x * a_y


main()
