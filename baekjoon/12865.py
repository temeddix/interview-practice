import sys
from dataclasses import dataclass


@dataclass
class Item:
    weight: int
    value: int


def get_max_value(capacity: int, items: list[Item]) -> int:
    dp_list = [0 for _ in range(capacity + 1)]

    for item in items:
        # Iterate backwards over capacities to avoid overwriting
        for curr_capacity in range(capacity, item.weight - 1, -1):
            other_capacity = curr_capacity - item.weight
            dp_list[curr_capacity] = max(
                dp_list[curr_capacity],
                dp_list[other_capacity] + item.value,
            )

    return dp_list[capacity]


def main():
    item_count, capacity = (int(s) for s in input().split(" "))
    items: list[Item] = []
    for _ in range(item_count):
        item_info = [int(s) for s in sys.stdin.readline().split(" ")]
        item = Item(weight=item_info[0], value=item_info[1])
        items.append(item)
    max_value = get_max_value(capacity, items)
    print(max_value)


main()
