from collections import deque

INFINITY = 1_000_000_000


Footprint = tuple[
    int,  # Operation count
    int,  # Previous number
]

Explorer = tuple[
    int,  # Current number
    int,  # Operation count
]


def find_min_operation(number: int) -> tuple[int, list[int]]:
    min_operations: list[Footprint] = [(INFINITY, INFINITY) for _ in range(number + 1)]
    min_operations[number] = (0, INFINITY)

    explorers = deque[Explorer]()
    explorers.append((number, 0))
    while explorers:
        explorer = explorers.pop()
        now_number = explorer[0]
        operations = explorer[1]
        new_operations = operations + 1
        if now_number % 3 == 0:
            new_number = now_number // 3
            if new_operations < min_operations[new_number][0]:
                min_operations[new_number] = (new_operations, now_number)
                explorers.append((new_number, new_operations))
        if now_number % 2 == 0:
            new_number = now_number // 2
            if new_operations < min_operations[new_number][0]:
                min_operations[new_number] = (new_operations, now_number)
                explorers.append((new_number, new_operations))
        if now_number > 1:
            new_number = now_number - 1
            if new_operations < min_operations[new_number][0]:
                min_operations[new_number] = (new_operations, now_number)
                explorers.append((new_number, new_operations))

    current_footprint = min_operations[1]
    footprints: list[int] = [1]
    while current_footprint[0] < number:
        prev_number = current_footprint[1]
        if prev_number == INFINITY:
            break
        footprints.append(prev_number)
        current_footprint = min_operations[prev_number]
    footprints.reverse()

    return min_operations[1][0], footprints


def main():
    number = int(input())
    min_operation, footprints = find_min_operation(number)
    print(min_operation)
    print(" ".join(str(i) for i in footprints))


main()
