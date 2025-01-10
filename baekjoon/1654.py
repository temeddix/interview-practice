import sys
from dataclasses import dataclass


@dataclass
class Bounds:
    left: int  # Inclusive
    right: int  # Inclusive


def get_slice_count(cables: list[int], slice_len: int) -> int:
    slice_count = 0
    for cable in cables:
        slice_count += cable // slice_len
    return slice_count


def get_max_slice_len(cables: list[int], slice_needed: int) -> int:
    # Bisect right
    bounds = Bounds(1, sum(cables))

    slice_len = 1
    while bounds.left <= bounds.right:
        mid = (bounds.left + bounds.right) // 2
        slice_count = get_slice_count(cables, mid)
        if slice_count < slice_needed:
            slice_len = mid - 1
            bounds.right = mid - 1
        else:
            bounds.left = mid + 1

    return slice_len


def main():
    cable_count, slice_needed = (int(s) for s in input().split())
    cables: list[int] = []
    for _ in range(cable_count):
        cable = int(sys.stdin.readline())
        cables.append(cable)
    max_slice_len = get_max_slice_len(cables, slice_needed)
    print(max_slice_len)


main()
