from sys import stdin, stdout
from typing import NamedTuple


def main():
    number_count, operation_count = (int(s) for s in input().split())
    numbers: list[int] = []
    for _ in range(number_count):
        number = int(stdin.readline().strip())
        numbers.append(number)
    tree = SegmentTree(numbers)
    min_max_list: list[MinMax] = []
    for _ in range(operation_count):
        start, end = (int(s) for s in stdin.readline().split())
        start -= 1
        min_max = tree.get_range_min_max(start, end)
        min_max_list.append(min_max)
    stdout.write("\n".join(f"{i[0]} {i[1]}" for i in min_max_list))


DIVIDER = 1_000_000_007


class MinMax(NamedTuple):
    min_value: int
    max_value: int


class Range(NamedTuple):
    start: int  # Inclusive
    end: int  # Exclusive


class NodeRange(NamedTuple):
    node: int  # Node number in the segment tree
    value_range: Range  # The range of values this node represents


class SegmentTree:
    def __init__(self, values: list[int]):
        self._value_count = len(values)
        self._values = values
        self._tree = [MinMax(-1, -1) for _ in range(self._value_count * 4)]

        self._build(NodeRange(0, Range(0, self._value_count)))

    def _get_children(self, node_range: NodeRange) -> tuple[NodeRange, NodeRange]:
        node, (start, end) = node_range
        mid = (start + end) // 2
        left_node_range = NodeRange(node * 2 + 1, Range(start, mid))
        right_node_range = NodeRange(node * 2 + 2, Range(mid, end))
        return left_node_range, right_node_range

    def _build(self, node_range: NodeRange):
        node, value_range = node_range
        start, end = value_range
        if start == end - 1:
            # Leaf node
            value = self._values[start]
            self._tree[node] = MinMax(value, value)
            return
        left_node_range, right_node_range = self._get_children(node_range)
        self._build(left_node_range)
        self._build(right_node_range)
        left_min_max = self._tree[left_node_range[0]]
        right_min_max = self._tree[right_node_range[0]]
        min_max = MinMax(
            min(left_min_max[0], right_min_max[0]),
            max(left_min_max[1], right_min_max[1]),
        )
        self._tree[node] = min_max

    def get_range_min_max(self, start: int, end: int) -> MinMax:
        min_max = self._get_range_min_max(
            Range(start, end),
            NodeRange(0, Range(0, self._value_count)),
        )
        if min_max is None:
            raise ValueError
        return min_max

    def _get_range_min_max(
        self, target_range: Range, node_range: NodeRange
    ) -> MinMax | None:
        node, value_range = node_range
        if value_range[0] >= target_range[0] and value_range[1] <= target_range[1]:
            # Inside
            return self._tree[node]
        if value_range[1] <= target_range[0]:
            # No intersection
            return None
        if value_range[0] >= target_range[1]:
            # No intersection
            return None
        left_node_range, right_node_range = self._get_children(node_range)
        left_min_max = self._get_range_min_max(target_range, left_node_range)
        right_min_max = self._get_range_min_max(target_range, right_node_range)
        if left_min_max is None:
            return right_min_max
        if right_min_max is None:
            return left_min_max
        min_max = MinMax(
            min(left_min_max[0], right_min_max[0]),
            max(left_min_max[1], right_min_max[1]),
        )
        return min_max


main()
