def get_lcs(text_a: str, text_b: str) -> str:
    """LCS stands for "longest common subsequence"."""
    size_a = len(text_a)
    size_b = len(text_b)
    dp_array = [[0 for _ in range(size_b + 1)] for _ in range(size_a + 1)]

    for i, char_a in enumerate(text_a):
        index_a = i + 1
        row_prev = dp_array[index_a - 1]
        row_curr = dp_array[index_a]
        for j, char_b in enumerate(text_b):
            index_b = j + 1
            new_value = max(row_curr[index_b - 1], row_prev[index_b])
            if char_a == char_b:
                new_value = max(
                    row_prev[index_b - 1] + 1,
                    new_value,
                )
            row_curr[index_b] = new_value

    lcs_list: list[str] = []
    cursor_a = size_a
    cursor_b = size_b
    while cursor_a > 0 and cursor_b > 0:
        current = dp_array[cursor_a][cursor_b]
        if dp_array[cursor_a - 1][cursor_b] == current:
            cursor_a -= 1
        elif dp_array[cursor_a][cursor_b - 1] == current:
            cursor_b -= 1
        else:
            lcs_list.append(text_a[cursor_a - 1])
            cursor_a -= 1
            cursor_b -= 1

    return "".join(reversed(lcs_list))


def main():
    text_a = input()
    text_b = input()
    lcs = get_lcs(text_a, text_b)
    print(len(lcs))
    print(lcs)


main()
