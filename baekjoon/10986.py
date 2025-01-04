import math
import sys


def find_range_count(numbers: list[int], divider: int) -> int:
    remainder_sums: list[int] = []  # Each value is between 0 and `divider`-1
    for number in numbers:
        previous_sum = 0 if not remainder_sums else remainder_sums[-1]
        current_sum = (previous_sum + number) % divider
        remainder_sums.append(current_sum)
    range_count = remainder_sums.count(0)  # Ranges that consist of only one number
    for remainder_sum in range(divider):
        set_size = remainder_sums.count(remainder_sum)
        range_count += math.comb(set_size, 2)
    return range_count


def main():
    _, m = (int(s) for s in input().split(" "))
    numbers: list[int] = [int(s) for s in sys.stdin.readline().split(" ")]
    range_count = find_range_count(numbers, m)
    print(range_count)


main()
