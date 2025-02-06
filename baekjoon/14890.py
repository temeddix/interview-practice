from sys import stdin
from typing import NamedTuple


def main():
    map_size, slope_length = (int(s) for s in input().split())
    height_map: list[list[int]] = []
    for _ in range(map_size):
        row = [int(s) for s in stdin.readline().split()]
        height_map.append(row)
    paths = extract_paths(height_map)
    usable_paths = count_usable_paths(paths, slope_length)
    print(usable_paths)


class FlatZone(NamedTuple):
    length: int
    left_elevated: bool
    right_elevated: bool


def extract_paths(height_map: list[list[int]]) -> list[list[int]]:
    map_size = len(height_map)

    paths: list[list[int]] = []

    for row in height_map:
        paths.append(row.copy())

    for column_index in range(map_size):
        column = [r[column_index] for r in height_map]
        paths.append(column)

    return paths


def count_usable_paths(paths: list[list[int]], slope_length: int) -> int:
    count = 0
    for path in paths:
        if is_path_usable(path, slope_length):
            count += 1
    return count


def is_path_usable(path: list[int], slope_length: int) -> bool:
    # Prepare buffers.
    prev_left_elevated = False
    prev_height = path[0]
    prev_length = 0

    # Check flat zones.
    for height in path:
        if height == prev_height:
            # Height did not change.
            prev_length += 1
        elif height == prev_height + 1:
            # Became higher.
            prev_zone = FlatZone(prev_length, prev_left_elevated, True)
            if not is_flat_zone_usable(prev_zone, slope_length):
                return False
            prev_left_elevated = False
            prev_height = height
            prev_length = 1
        elif height == prev_height - 1:
            # Became lower.
            prev_zone = FlatZone(prev_length, prev_left_elevated, False)
            if not is_flat_zone_usable(prev_zone, slope_length):
                return False
            prev_left_elevated = True
            prev_height = height
            prev_length = 1
        else:
            # Only possible to move one level at a time.
            return False

    # Check the last flat zone.
    last_zone = FlatZone(prev_length, prev_left_elevated, False)
    if not is_flat_zone_usable(last_zone, slope_length):
        return False

    return True


def is_flat_zone_usable(flat_zone: FlatZone, slope_length: int) -> bool:
    length, left_elevated, right_elevated = flat_zone
    needed_length = (int(left_elevated) + int(right_elevated)) * slope_length
    return length >= needed_length


main()
