from sys import stdin, stdout
from typing import NamedTuple


def main():
    number_count, replace_count, mul_count = (int(s) for s in input().split())
    operation_count = replace_count + mul_count
    numbers: list[int] = []
    for _ in range(number_count):
        number = int(stdin.readline().strip())
        numbers.append(number)
    tree = SegmentTree(numbers)
    range_muls: list[int] = []
    for _ in range(operation_count):
        operation, a, b = (int(s) for s in stdin.readline().split())
        if operation == 1:
            tree.replace(a - 1, b)
        else:
            range_mul = tree.get_range_mul(a - 1, b)
            range_muls.append(range_mul)
    stdout.write("\n".join(str(i) for i in range_muls))


DIVIDER = 1_000_000_007


class Range(NamedTuple):
    start: int  # Inclusive
    end: int  # Exclusive


class NodeRange(NamedTuple):
    node: int  # Node number in the segment tree
    value_range: Range  # The range of whose multiple this node represents


class SegmentTree:
    def __init__(self, values: list[int]):
        self._value_count = len(values)
        self._values = values
        self._muls = [0 for _ in range(self._value_count * 4)]

        self._build(NodeRange(0, Range(0, self._value_count)))

    def _split_range(self, slice_range: Range) -> tuple[Range, Range]:
        start, end = slice_range
        mid = (start + end) // 2
        return Range(start, mid), Range(mid, end)

    def _build(self, node_range: NodeRange):
        node, value_range = node_range
        start, end = value_range
        if start == end - 1:
            self._muls[node] = self._values[start]
            return
        left_range, right_range = self._split_range(value_range)
        self._build(NodeRange(node * 2 + 1, left_range))
        self._build(NodeRange(node * 2 + 2, right_range))
        mul = self._muls[node * 2 + 1] * self._muls[node * 2 + 2] % DIVIDER
        self._muls[node] = mul

    def replace(self, index: int, value: int):
        self._values[index] = value
        self._replace(value, index, NodeRange(0, Range(0, self._value_count)))

    def _replace(self, value: int, index: int, node_range: NodeRange):
        node, value_range = node_range
        start, end = value_range
        if not start <= index < end:
            return
        if start == end - 1:
            # Leaf node
            leaf_value = value % DIVIDER
            self._muls[node] = leaf_value
            return
        left_range, right_range = self._split_range(value_range)
        self._replace(value, index, NodeRange(node * 2 + 1, left_range))
        self._replace(value, index, NodeRange(node * 2 + 2, right_range))
        mul = self._muls[node * 2 + 1] * self._muls[node * 2 + 2] % DIVIDER
        self._muls[node] = mul

    def get_range_mul(self, start: int, end: int) -> int:
        return self._get_range_mul(
            Range(start, end),
            NodeRange(0, Range(0, self._value_count)),
        )

    def _get_range_mul(self, target_range: Range, node_range: NodeRange) -> int:
        node, value_range = node_range
        if value_range[0] >= target_range[0] and value_range[1] <= target_range[1]:
            # Inside
            return self._muls[node]
        if value_range[1] <= target_range[0]:
            # No intersection
            return 1
        if value_range[0] >= target_range[1]:
            # No intersection
            return 1
        left_range, right_range = self._split_range(value_range)
        left_mul = self._get_range_mul(
            target_range,
            NodeRange(node * 2 + 1, left_range),
        )
        right_mul = self._get_range_mul(
            target_range,
            NodeRange(node * 2 + 2, right_range),
        )
        return left_mul * right_mul % DIVIDER


main()
