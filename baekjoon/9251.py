import sys


def get_lcs_len(text_a: str, text_b: str) -> int:
    prev_row = [0] * (len(text_b) + 1)
    curr_row = [0] * (len(text_b) + 1)

    for char_a in text_a:
        for j, char_b in enumerate(text_b):
            j += 1
            if char_a == char_b:
                curr_row[j] = prev_row[j - 1] + 1
            else:
                curr_row[j] = max(prev_row[j], curr_row[j - 1])
        prev_row = curr_row.copy()

    return curr_row[-1]


def main():
    text_a = str(sys.stdin.readline().strip())
    text_b = str(sys.stdin.readline().strip())
    lcs_len = get_lcs_len(text_a, text_b)
    print(lcs_len)


main()
