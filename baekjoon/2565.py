import sys
from bisect import bisect_left
from dataclasses import dataclass


@dataclass
class Wire:
    left: int
    right: int


def get_lis_len(numbers: list[int]) -> int:
    """LIS means longest increasing subsequence"""
    if not numbers:
        return 0
    lis_numbers = [numbers[0]]  # Always sorted
    for number in numbers:
        if lis_numbers[-1] < number:
            lis_numbers.append(number)
        else:
            insert_index = bisect_left(lis_numbers, number)
            lis_numbers[insert_index] = number
    return len(lis_numbers)


def main():
    lines_count = int(sys.stdin.readline())
    wires: list[Wire] = []
    for _ in range(lines_count):
        pair_data = [int(s) for s in sys.stdin.readline().split(" ")]
        wire = Wire(left=pair_data[0], right=pair_data[1])
        wires.append(wire)
    wires.sort(key=lambda w: w.left)
    lis_len = get_lis_len([w.right for w in wires])
    print(lines_count - lis_len)


main()
