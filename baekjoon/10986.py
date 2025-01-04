import math
import sys


def find_range_count(numbers: list[int], divider: int) -> int:
    # Each value is between 0 and `divider`-1
    remainder_sums: list[int] = [0 for _ in range(len(numbers) + 1)]
    for i, number in enumerate(numbers):
        previous_sum = remainder_sums[i]
        current_sum = (previous_sum + number) % divider
        remainder_sums[i + 1] = current_sum
    remainder_sums = remainder_sums[1:]
    range_count = remainder_sums.count(0)  # Ranges that consist of only one number
    set_sizes = [0 for _ in range(divider)]
    for remainder_sum in remainder_sums:
        set_sizes[remainder_sum] += 1
    for remainder_sum in range(divider):
        set_size = set_sizes[remainder_sum]
        range_count += math.comb(set_size, 2)
    return range_count


def main():
    _, m = (int(s) for s in input().split(" "))
    numbers: list[int] = [int(s) for s in sys.stdin.readline().split(" ")]
    range_count = find_range_count(numbers, m)
    print(range_count)


main()
