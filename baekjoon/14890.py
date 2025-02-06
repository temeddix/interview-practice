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
        column: list[int] = []
        for row in height_map:
            column.append(row[column_index])
        paths.append(column)

    return paths


def count_usable_paths(paths: list[list[int]], slope_length: int) -> int:
    count = 0
    for path in paths:
        if is_path_usable(path, slope_length):
            count += 1
    return count


def is_path_usable(path: list[int], slope_length: int) -> bool:
    flat_zones: list[FlatZone] = []

    # Prepare buffers.
    prev_left_elevated = False
    prev_height = path[0]
    prev_length = 0

    # Collect flat zones.
    for height in path:
        if height == prev_height:
            # Height did not change.
            prev_length += 1
        elif height == prev_height + 1:
            # Became higher.
            prev_zone = FlatZone(prev_length, prev_left_elevated, True)
            flat_zones.append(prev_zone)
            prev_left_elevated = False
            prev_height = height
            prev_length = 1
        elif height == prev_height - 1:
            # Became lower.
            prev_zone = FlatZone(prev_length, prev_left_elevated, False)
            flat_zones.append(prev_zone)
            prev_left_elevated = True
            prev_height = height
            prev_length = 1
        else:
            # Only possible to move one level at a time.
            return False

    # Collect the last flat zone.
    last_zone = FlatZone(prev_length, prev_left_elevated, False)
    flat_zones.append(last_zone)

    # Check if all flat zones have enough length.
    is_usable = True
    for flat_zone in flat_zones:
        needed_length = (int(flat_zone[1]) + int(flat_zone[2])) * slope_length
        if flat_zone[0] < needed_length:
            is_usable = False
            break

    return is_usable


main()
