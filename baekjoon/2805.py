import sys
from dataclasses import dataclass


@dataclass
class Bounds:
    left: int  # Inclusive
    right: int  # Inclusive


def get_usable_len(trees: list[int], slice_len: int) -> int:
    usable_len = 0
    for tree in trees:
        if tree > slice_len:
            usable_len += tree - slice_len
    return usable_len


def get_max_slice_len(trees: list[int], needed_len: int) -> int:
    # Bisect right
    bounds = Bounds(1, sum(trees))

    slice_len = 1
    while bounds.left <= bounds.right:
        mid = (bounds.left + bounds.right) // 2
        usable_len = get_usable_len(trees, mid)
        if usable_len < needed_len:
            slice_len = mid - 1
            bounds.right = mid - 1
        else:
            bounds.left = mid + 1

    return slice_len


def main():
    _, needed_len = (int(s) for s in input().split())
    trees = [int(s) for s in sys.stdin.readline().split()]
    max_slice_len = get_max_slice_len(trees, needed_len)
    print(max_slice_len)


main()
