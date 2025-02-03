from sys import stdin, stdout
from typing import NamedTuple


def main():
    number_count, replace_count, sum_count = (int(s) for s in input().split())
    operation_count = replace_count + sum_count
    numbers: list[int] = []
    for _ in range(number_count):
        number = int(stdin.readline().strip())
        numbers.append(number)
    tree = SegmentTree(numbers)
    range_sums: list[int] = []
    for _ in range(operation_count):
        operation, a, b = (int(s) for s in stdin.readline().split())
        if operation == 1:
            tree.replace(a - 1, b)
        else:
            range_sum = tree.get_range_sum(a - 1, b)
            range_sums.append(range_sum)
    stdout.write("\n".join(str(i) for i in range_sums))


class Range(NamedTuple):
    start: int  # Inclusive
    end: int  # Exclusive


class NodeRange(NamedTuple):
    node: int  # Node number in the segment tree
    value_range: Range  # The range of whose sum this node represents


class SegmentTree:
    def __init__(self, values: list[int]):
        self._value_count = len(values)
        self._values = values
        self._sums = [0 for _ in range(self._value_count * 4)]

        self._build(NodeRange(0, Range(0, self._value_count)))

    def _split_range(self, slice_range: Range) -> tuple[Range, Range]:
        start, end = slice_range
        mid = (start + end) // 2
        return Range(start, mid), Range(mid, end)

    def _build(self, node_range: NodeRange):
        node, value_range = node_range
        start, end = value_range
        if start == end - 1:
            self._sums[node] = self._values[start]
            return
        left_range, right_range = self._split_range(value_range)
        self._build(NodeRange(node * 2 + 1, left_range))
        self._build(NodeRange(node * 2 + 2, right_range))
        self._sums[node] = self._sums[node * 2 + 1] + self._sums[node * 2 + 2]

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
        left_range, right_range = self._split_range(value_range)
        self._replace(diff, index, NodeRange(node * 2 + 1, left_range))
        self._replace(diff, index, NodeRange(node * 2 + 2, right_range))

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
        left_range, right_range = self._split_range(value_range)
        left_sum = self._get_range_sum(
            target_range,
            NodeRange(node * 2 + 1, left_range),
        )
        right_sum = self._get_range_sum(
            target_range,
            NodeRange(node * 2 + 2, right_range),
        )
        return left_sum + right_sum


main()
