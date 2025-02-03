from typing import NamedTuple

# Using bubble sort here is not appropriate
# because the problem asked us to utilize segment tree.


def main():
    _ = int(input())
    numbers = [int(s) for s in input().split()]
    swap_count = calculate_swap_count(numbers)
    print(swap_count)


def calculate_swap_count(numbers: list[int]) -> int:
    number_count = len(numbers)
    sorted_numbers = sorted(numbers)

    sorted_indices: dict[int, int] = {}
    for sorted_index, number in enumerate(sorted_numbers):
        sorted_indices[number] = sorted_index

    originals = [Original([]) for _ in range(number_count)]
    for unsorted_index, number in enumerate(numbers):
        sorted_index = sorted_indices[number]
        originals[sorted_index][0].append(unsorted_index)

    swap_count = fill_segment_tree(originals)
    return swap_count


EMPTY = -1


class Original(NamedTuple):
    unsorted_indeces: list[int]  # Grouped by number value


class Range(NamedTuple):
    start: int  # Inclusive
    end: int  # Exclusive


class NodeRange(NamedTuple):
    node: int  # Node number in the segment tree
    value_range: Range  # The range of whose sum this node represents


def fill_segment_tree(originals: list[Original]) -> int:
    number_count = len(originals)
    swap_count = 0

    tree = SegmentTree(number_count)
    for original in originals:
        unsorted_indices = original[0]
        for unsorted_index in unsorted_indices:
            swap_count += tree.get_range_sum(unsorted_index, number_count)
            tree.replace(unsorted_index, 1)

    return swap_count


class SegmentTree:
    def __init__(self, value_count: int):
        self._value_count = value_count
        self._values = [0 for _ in range(value_count)]
        self._sums = [0 for _ in range(value_count * 4)]

    def _get_children(self, node_range: NodeRange) -> tuple[NodeRange, NodeRange]:
        node, (start, end) = node_range
        mid = (start + end) // 2
        left_node_range = NodeRange(node * 2 + 1, Range(start, mid))
        right_node_range = NodeRange(node * 2 + 2, Range(mid, end))
        return left_node_range, right_node_range

    def replace(self, index: int, value: int):
        prev_value = self._values[index]
        self._values[index] = value
        diff = value - prev_value
        self._replace(diff, index, NodeRange(0, Range(0, self._value_count)))

    def _replace(self, diff: int, index: int, node_range: NodeRange):
        node, value_range = node_range
        start, end = value_range
        if not start <= index < end:
            return
        self._sums[node] += diff
        if start == end - 1:
            # Leaf node
            return
        left_node_range, right_node_range = self._get_children(node_range)
        self._replace(diff, index, left_node_range)
        self._replace(diff, index, right_node_range)

    def get_range_sum(self, start: int, end: int) -> int:
        return self._get_range_sum(
            Range(start, end),
            NodeRange(0, Range(0, self._value_count)),
        )

    def _get_range_sum(self, target_range: Range, node_range: NodeRange) -> int:
        node, value_range = node_range
        if value_range[0] >= target_range[0] and value_range[1] <= target_range[1]:
            # Inside
            return self._sums[node]
        if value_range[1] <= target_range[0]:
            # No intersection
            return 0
        if value_range[0] >= target_range[1]:
            # No intersection
            return 0
        left_node_range, right_node_range = self._get_children(node_range)
        left_sum = self._get_range_sum(target_range, left_node_range)
        right_sum = self._get_range_sum(target_range, right_node_range)
        return left_sum + right_sum


main()
