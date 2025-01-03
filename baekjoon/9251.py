import sys


def get_lcs_len(text_a: str, text_b: str) -> int:
    grid: list[list[int]] = [
        [0 for _ in range(len(text_b) + 1)] for _ in range(len(text_a) + 1)
    ]
    for i, char_a in enumerate(text_a):
        i += 1
        for j, char_b in enumerate(text_b):
            j += 1
            if char_a == char_b:
                grid[i][j] = grid[i - 1][j - 1] + 1
            else:
                grid[i][j] = max(grid[i - 1][j], grid[i][j - 1])
    return grid[-1][-1]


def main():
    text_a = str(sys.stdin.readline().strip())
    text_b = str(sys.stdin.readline().strip())
    lcs_len = get_lcs_len(text_a, text_b)
    print(lcs_len)


main()
