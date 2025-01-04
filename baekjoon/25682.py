import sys


def main():
    n, m, k = (int(s) for s in input().split(" "))

    rows: list[list[bool]] = []

    # Create the board grid from the input.
    for _ in range(n):
        input_line = str(sys.stdin.readline().strip())
        new_row = [True if s == "W" else False for s in input_line]
        rows.append(new_row)

    # Flip every other cells.
    # By doing this, we can simply search for different colors.
    for i, row in enumerate(rows):
        if i % 2 == 0:
            switch_range = range(0, m, 2)
        else:
            switch_range = range(1, m, 2)
        for column in switch_range:
            row[column] = not row[column]

    # Calculate sums.
    # This grid has an extra column and an extra row of zeros.
    sum_rows = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i, row in enumerate(rows):
        for j, color in enumerate(row):
            prev_sum = sum_rows[i + 1][j] + sum_rows[i][j + 1] - sum_rows[i][j]
            new_sum = prev_sum + 1 if color else prev_sum
            sum_rows[i + 1][j + 1] = new_sum

    # Find the minimum flip count.
    min_flip_count = 10000000
    for i in range(n - k + 1):
        for j in range(m - k + 1):
            flip_count = (
                sum_rows[i + k][j + k]
                - sum_rows[i][j + k]
                - sum_rows[i + k][j]
                + sum_rows[i][j]
            )
            flip_count = min(flip_count, k * k - flip_count)
            min_flip_count = min(flip_count, min_flip_count)

    print(min_flip_count)


main()
