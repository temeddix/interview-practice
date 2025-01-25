NEUTRAL = 0


def get_best_pair(sequence: list[int]) -> tuple[int, int]:
    sequence = sorted(sequence)
    left_cursor = 0
    right_cursor = len(sequence) - 1

    best_pair = (sequence[left_cursor], sequence[right_cursor])
    best_abs = abs(sequence[left_cursor] + sequence[right_cursor])

    while left_cursor < right_cursor:
        sum_value = sequence[left_cursor] + sequence[right_cursor]
        abs_value = abs(sum_value)
        if abs_value < best_abs:
            best_abs = abs_value
            best_pair = (sequence[left_cursor], sequence[right_cursor])
        if sum_value < NEUTRAL:
            left_cursor += 1
        else:
            right_cursor -= 1

    return best_pair


def main():
    _ = input()
    sequence = [int(s) for s in input().split()]
    best_pair = get_best_pair(sequence)
    print(" ".join(str(i) for i in best_pair))


main()
