import sys
from bisect import bisect_left


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
    _ = int(sys.stdin.readline())
    numbers = [int(s) for s in input().split(" ")]
    max_bitonic_len = -1
    for i in range(len(numbers)):
        left_part = numbers[: i + 1]
        right_part = [-n for n in numbers[i:]]
        bitonic_len = get_lis_len(left_part) + get_lis_len(right_part) - 1
        max_bitonic_len = max(max_bitonic_len, bitonic_len)
    print(max_bitonic_len)


main()
