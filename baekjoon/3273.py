def count_pairs(sequence: list[int], goal: int) -> int:
    sequence = sorted(sequence)
    left_cursor = 0
    right_cursor = len(sequence) - 1
    pair_count = 0

    while left_cursor < right_cursor:
        sum = sequence[left_cursor] + sequence[right_cursor]
        if sum == goal:
            pair_count += 1
            right_cursor -= 1
        elif sum < goal:
            left_cursor += 1
        else:
            right_cursor -= 1

    return pair_count


def main():
    _ = input()
    sequence = [int(s) for s in input().split()]
    goal = int(input())
    pair_count = count_pairs(sequence, goal)
    print(pair_count)


main()
