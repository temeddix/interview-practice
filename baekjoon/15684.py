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
    new_candidate: Bridge | None


MAX_EXTRAS = 3
INFINITY = 1_000_000_007


def find_min_extras(structure: Structure, precomputed: Precomputed) -> int | None:
    # Get the structure.
    level_count, line_count, bridges = structure
    if not bridges:
        return 0

    # Create the bridge grid to check adjacency.
    bridge_grid: list[list[bool]] = [[False] * line_count for _ in range(level_count)]
    for bridge in bridges:
        level, left_line = bridge
        bridge_grid[level][left_line] = True

    # Prepare extra brige candidates.
    extra_candidates = create_extra_candidates(structure, bridge_grid)
    if not extra_candidates:
        return None
    candidate_count = len(extra_candidates)

    # Perform DFS.
    dfs_stack: list[Job] = []
    dfs_stack.append(Job(False, extra_candidates[0]))
    dfs_stack.append(Job(True, extra_candidates[0]))
    dfs_stack.append(Job(False, None))
    dfs_stack.append(Job(True, None))

    min_extras = INFINITY
    candidate_cursor = 0
    extras: list[Bridge] = []

    while dfs_stack:
        is_head, new_candidate = dfs_stack.pop()

        if is_head:
            # Before child recursion.
            if new_candidate is not None:
                level, left_line = new_candidate
                bridge_grid[level][left_line] = True
                extras.append(new_candidate)

            should_check = new_candidate is not None
            if should_check and are_extras_usable(extras, precomputed):
                min_extras = min(min_extras, len(extras))
                continue

            candidate_cursor += 1
            if candidate_cursor == candidate_count:
                continue

            if len(extras) < min(MAX_EXTRAS, min_extras - 1):
                next_extra = extra_candidates[candidate_cursor]
                if is_extra_available(bridge_grid, next_extra):
                    dfs_stack.append(Job(False, next_extra))
                    dfs_stack.append(Job(True, next_extra))
                dfs_stack.append(Job(False, None))
                dfs_stack.append(Job(True, None))

        else:
            # After child recursion.
            if new_candidate is not None:
                level, left_line = new_candidate
                bridge_grid[level][left_line] = False
                extras.pop()

            candidate_cursor -= 1

    return None if min_extras == INFINITY else min_extras


LINE_DIFFS = (-1, 1)


def create_extra_candidates(
    structure: Structure, bridge_grid: list[list[bool]]
) -> list[Bridge]:
    level_count, line_count, _ = structure

    extra_candidates: list[Bridge] = []
    for level in range(level_count):
        level_candidates = [Bridge(level, n) for n in range(line_count - 1)]
        extra_candidates.extend(
            c for c in level_candidates if is_extra_available(bridge_grid, c)
        )

    return extra_candidates


def is_extra_available(bridge_grid: list[list[bool]], extra: Bridge) -> bool:
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


def are_extras_usable(extras: list[Bridge], precomputed: Precomputed) -> bool:
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
    is_sorted = all(modified[i] <= modified[i + 1] for i in range(len(modified) - 1))
    return is_sorted


main()
