def count_possible_sums(items: list[int], capacity: int) -> list[int]:
    if not items:
        return [0]

    first_item = items[0]
    possible_sums: list[int] = []

    new_sums = count_possible_sums(items[1:], capacity)
    possible_sums.extend(new_sums)
    for new_sum in new_sums:
        added_sum = new_sum + first_item
        if added_sum <= capacity:
            possible_sums.append(added_sum)

    return possible_sums


MIN_ITEMS_TO_SPLIT = 2


SumOption = tuple[
    int,  # Sum value
    int,  # Option count
]


def count_options(items: list[int], capacity: int) -> int:
    if len(items) < MIN_ITEMS_TO_SPLIT:
        return len(count_possible_sums(items, capacity))

    mid = len(items) // 2 + 1
    items_a = items[:mid]
    items_b = items[mid:]

    possible_sums_a = count_possible_sums(items_a, capacity)
    possible_sums_b = count_possible_sums(items_b, capacity)
    possible_sums_a.sort()
    possible_sums_b.sort()

    sum_options_a: list[SumOption] = []
    for sum_value in possible_sums_a:
        if sum_options_a and sum_options_a[-1][0] == sum_value:
            last_option = sum_options_a[-1]
            sum_options_a.pop()
            sum_options_a.append((last_option[0], last_option[1] + 1))
        else:
            sum_options_a.append((sum_value, 1))
    sum_options_b: list[SumOption] = []
    for sum_value in possible_sums_b:
        if sum_options_b and sum_options_b[-1][0] == sum_value:
            last_option = sum_options_b[-1]
            sum_options_b.pop()
            sum_options_b.append((last_option[0], last_option[1] + 1))
        else:
            sum_options_b.append((sum_value, 1))

    options = 0
    for sum_option_a in sum_options_a:
        for sum_option_b in sum_options_b:
            if sum_option_a[0] + sum_option_b[0] <= capacity:
                options += sum_option_a[1] * sum_option_b[1]

    return options


def main():
    _, capacity = (int(s) for s in input().split())
    items = [int(s) for s in input().split()]
    options = count_options(items, capacity)
    print(options)


main()
