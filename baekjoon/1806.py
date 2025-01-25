NEUTRAL = 0


def get_shortest_slice_len(sequence: list[int], goal: int) -> int:
    max_index = len(sequence) - 1

    left_cursor = 0  # Inclusive
    right_cursor = 0  # Inclusive
    current_sum = sum(sequence[left_cursor : right_cursor + 1])
    while current_sum < goal:
        if right_cursor == max_index:
            return 0
        right_cursor += 1
        current_sum += sequence[right_cursor]
    shortest_slice_len = right_cursor - left_cursor + 1

    current_sum = sum(sequence[left_cursor : right_cursor + 1])
    while True:
        if left_cursor == right_cursor:
            if right_cursor == max_index:
                break
            right_cursor += 1
            current_sum += sequence[right_cursor]
        elif current_sum - sequence[left_cursor] >= goal:
            current_sum -= sequence[left_cursor]
            left_cursor += 1
        else:
            if right_cursor == max_index:
                break
            right_cursor += 1
            current_sum += sequence[right_cursor]
        shortest_slice_len = min(
            shortest_slice_len,
            right_cursor - left_cursor + 1,
        )

    return shortest_slice_len


def main():
    _, goal = (int(s) for s in input().split())
    sequence = [int(s) for s in input().split()]
    longest_slice_len = get_shortest_slice_len(sequence, goal)
    print(longest_slice_len)


main()
