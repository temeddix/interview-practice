from sys import stdin
from typing import NamedTuple


def main():
    line_count, bridge_count, level_count = (int(s) for s in input().split())
    bridges: list[Bridge] = []
    for _ in range(bridge_count):
        level, left_line = (int(s) for s in stdin.readline().split())
        level -= 1
        left_line -= 1
        bridges.append(Bridge(level, left_line))
    structure = Structure(level_count, line_count, bridges)
    precomputed = precompute_result(structure)
    min_extras = find_min_extras(structure, precomputed)
    print(-1 if min_extras is None else min_extras)


class Bridge(NamedTuple):
    level: int
    left_line: int


class Structure(NamedTuple):
    level_count: int
    line_count: int
    bridges: list[Bridge]


class SwapPrediction(NamedTuple):
    left_value: int
    right_value: int


class Precomputed(NamedTuple):
    swap_predictions: list[list[SwapPrediction]]
    result_values: list[int]  # Index to value
    result_indices: list[int]  # Value to index


def precompute_result(structure: Structure) -> Precomputed:
    level_count, line_count, bridges = structure

    # The level and the left line becomes the key.
    # The value is none if extra bridge is not allowed there.
    swap_predictions: list[list[SwapPrediction]] = []

    # Sort bridges to pop from the top level zero.
    bridges = sorted(bridges, reverse=True)

    # Prepare the initial values.
    values = [i for i in range(line_count)]

    # Keep swapping and remembering predictions.
    for level in range(level_count):
        level_predictions: list[SwapPrediction] = []
        swap_predictions.append(level_predictions)

        while bridges and bridges[-1].level == level:
            bridge = bridges.pop()
            _, left_line = bridge
            right_line = left_line + 1
            pair = values[right_line], values[left_line]
            values[left_line], values[right_line] = pair

        for line in range(line_count - 1):
            left_value = values[line]
            right_value = values[line + 1]
            prediction = SwapPrediction(left_value, right_value)
            level_predictions.append(prediction)

    # Create the original indices.
    indices = [-1 for _ in range(line_count)]
    for index, value in enumerate(values):
        indices[value] = index

    return Precomputed(swap_predictions, values, indices)


class Job(NamedTuple):
    is_head: bool
    add_extra: bool
    cursor: Bridge


MAX_EXTRAS = 3
INFINITY = 1_000_000_007


def find_min_extras(structure: Structure, precomputed: Precomputed) -> int | None:
    # Get the structure.
    level_count, line_count, bridges = structure
    if is_sorted(precomputed.result_values):
        return 0

    # Create the bridge grid to check adjacency.
    bridge_grid: list[list[bool]] = [[False] * line_count for _ in range(level_count)]
    for bridge in bridges:
        level, left_line = bridge
        bridge_grid[level][left_line] = True

    # Perform DFS.
    dfs_stack: list[Job] = []
    start_cursor = Bridge(0, 0)
    if is_extra_placeable(bridge_grid, start_cursor):
        dfs_stack.append(Job(False, True, start_cursor))
        dfs_stack.append(Job(True, True, start_cursor))
    dfs_stack.append(Job(False, False, start_cursor))
    dfs_stack.append(Job(True, False, start_cursor))

    min_extras = INFINITY
    extras: list[Bridge] = []

    while dfs_stack:
        is_head, add_extra, cursor = dfs_stack.pop()

        if is_head:
            # Before child recursion.
            level, left_line = cursor
            if add_extra:
                bridge_grid[level][left_line] = True
                extras.append(cursor)

            if add_extra and is_working(extras, precomputed):
                min_extras = min(min_extras, len(extras))
                continue

            next_left_line = left_line + 2 if add_extra else left_line + 1
            next_level = level if next_left_line < line_count - 1 else level + 1
            next_left_line = next_left_line if next_left_line < line_count - 1 else 0
            if next_level == level_count:
                continue
            next_cursor = Bridge(next_level, next_left_line)

            if len(extras) < min(MAX_EXTRAS, min_extras - 1):
                if is_extra_placeable(bridge_grid, next_cursor):
                    dfs_stack.append(Job(False, True, next_cursor))
                    dfs_stack.append(Job(True, True, next_cursor))
                dfs_stack.append(Job(False, False, next_cursor))
                dfs_stack.append(Job(True, False, next_cursor))

        else:
            # After child recursion.
            level, left_line = cursor
            if add_extra:
                bridge_grid[level][left_line] = False
                extras.pop()

    return None if min_extras == INFINITY else min_extras


LINE_DIFFS = (-1, 1)


def is_extra_placeable(bridge_grid: list[list[bool]], extra: Bridge) -> bool:
    grid_width = len(bridge_grid[0])
    level, left_line = extra

    if bridge_grid[level][left_line]:
        return False

    for line_diff in LINE_DIFFS:
        adjacent_left_line = left_line + line_diff
        if not 0 <= adjacent_left_line < grid_width:
            continue
        if bridge_grid[level][adjacent_left_line]:
            return False

    return True


def is_working(extras: list[Bridge], precomputed: Precomputed) -> bool:
    swap_predictions, result_values, result_indices = precomputed

    # Prepare the list to store modified values.
    modified = result_values.copy()

    # Calculate the final modified values from adding extra bridges.
    # This assumes that extra bridges are sorted.
    for extra in extras:
        level, left_line = extra

        # Get the swap prediction in the middle of the ladder.
        swap_prediction = swap_predictions[level][left_line]
        left_swap_value, right_swap_value = swap_prediction

        # Get the swap index at the final result.
        final_index_a = result_indices[left_swap_value]
        final_index_b = result_indices[right_swap_value]

        # Swap the numbers in the modified values.
        pair = modified[final_index_b], modified[final_index_a]
        modified[final_index_a], modified[final_index_b] = pair

    # Check if the modified result is sorted.
    return is_sorted(modified)


def is_sorted(numbers: list[int]) -> bool:
    return all(numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1))


main()
