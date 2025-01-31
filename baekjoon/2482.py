def main():
    color_count = int(input())
    pick_count = int(input())
    possibilities = count_possibilities(color_count, pick_count)
    print(possibilities)


DIVIDER = 1_000_000_003


def count_possibilities(color_count: int, pick_count: int) -> int:
    dp_array = [[1] + [0] * (pick_count) for _ in range(color_count + 1)]

    dp_array[0][0] = 1
    dp_array[1][0] = 1
    dp_array[1][1] = 1

    for color in range(2, color_count + 1):
        possible_pick_count = color // 2
        limit_pick_count = min(pick_count, possible_pick_count)
        for pick in range(1, limit_pick_count + 1):
            selecting = dp_array[color - 2][pick - 1]
            not_selecting = dp_array[color - 1][pick]
            added = (selecting + not_selecting) % DIVIDER
            dp_array[color][pick] = added

    return dp_array[-1][-1]


main()
