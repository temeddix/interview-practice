from bisect import bisect_left

Backtracker = tuple[
    int,  # Index
    int,  # Number
]


def get_lis(numbers: list[int]) -> list[int]:
    """LIS stands for "longest increasing subsequence"."""
    dp_list: list[int] = [numbers[0]]  # Sorted in ascending order
    backtrackers: list[Backtracker] = [(0, numbers[0])]

    for number in numbers[1:]:
        last_value = dp_list[-1]
        if number > last_value:
            dp_list.append(number)
            backtrackers.append((len(dp_list) - 1, number))
        else:
            index = bisect_left(dp_list, number)
            dp_list[index] = number
            backtrackers.append((index, number))

    lis: list[int] = []
    last_index = len(dp_list) - 1
    for backtracker in reversed(backtrackers):
        if backtracker[0] == last_index:
            lis.append(backtracker[1])
            last_index -= 1
    lis.reverse()

    return lis


def main():
    _ = input()
    numbers = [int(s) for s in input().split()]
    increasing = get_lis(numbers)
    print(len(increasing))
    print(" ".join(str(i) for i in increasing))


main()
