import sys

LimitColumn = tuple[
    int,  # Column index
    int,  # Column height
]


def get_biggest_rect_area(columns: list[int]) -> int:
    limit_columns: list[LimitColumn] = []
    biggest_area = 0

    for index, column in enumerate(columns + [0]):
        limit_index = index
        while limit_columns and limit_columns[-1][1] >= column:
            popped_limit_column = limit_columns.pop()
            width = index - popped_limit_column[0]
            height = popped_limit_column[1]
            biggest_area = max(biggest_area, width * height)
            limit_index = popped_limit_column[0]
        limit_columns.append((limit_index, column))

    return biggest_area


def main():
    column_count = int(input())
    columns: list[int] = []
    for _ in range(column_count):
        columns.append(int(sys.stdin.readline()))
    biggest_rect_area = get_biggest_rect_area(columns)
    print(biggest_rect_area)


main()
