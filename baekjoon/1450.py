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
INFINITY = 1_000_000_007


def count_options(items: list[int], capacity: int) -> int:
    if len(items) < MIN_ITEMS_TO_SPLIT:
        return len(count_possible_sums(items, capacity))

    mid = len(items) // 2 + 1
    items_a = items[:mid]
    items_b = items[mid:]

    possible_sums_a = count_possible_sums(items_a, capacity)
    possible_sums_b = count_possible_sums(items_b, capacity)
    possible_sums_a.sort(reverse=True)
    possible_sums_b.sort()
    possible_sums_b.append(INFINITY)

    cursor = 0
    options = 0
    for sum_a in possible_sums_a:
        while True:
            if sum_a + possible_sums_b[cursor] <= capacity:
                cursor += 1
            else:
                break
        options += cursor

    return options


def main():
    _, capacity = (int(s) for s in input().split())
    items = [int(s) for s in input().split()]
    options = count_options(items, capacity)
    print(options)


main()
