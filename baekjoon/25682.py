import sys

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
# This has an extra column of 0 at the left.
sum_rows: list[list[int]] = []
for row in rows:
    sum_row = [0]
    sum = 0
    for color in row:
        if color:
            sum += 1
        sum_row.append(sum)
    sum_rows.append(sum_row)

# Find the minimum flip count.
min_flip_count = 10000000
for i in range(n - k + 1):
    for j in range(m - k + 1):
        flip_count = 0
        for sum_row in sum_rows[i : i + k]:
            flip_count += sum_row[j + k] - sum_row[j]
        flip_count = min(flip_count, k * k - flip_count)
        min_flip_count = min(flip_count, min_flip_count)


print(min_flip_count)
