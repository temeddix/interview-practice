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
    min_operations[1] = (0, INFINITY)

    explorers = deque[Explorer]()
    explorers.append((number, 0))
    for now_number in range(2, number + 1):
        prev_number = now_number - 1
        operations = min_operations[prev_number][0] + 1
        if now_number % 2 == 0:
            test_number = now_number // 2
            test_operations = min_operations[test_number][0] + 1
            if test_operations < operations:
                prev_number = test_number
                operations = test_operations
        if now_number % 3 == 0:
            test_number = now_number // 3
            test_operations = min_operations[test_number][0] + 1
            if test_operations < operations:
                prev_number = test_number
                operations = test_operations
        min_operations[now_number] = (operations, prev_number)

    current_footprint = min_operations[-1]
    footprints: list[int] = [number]
    while current_footprint[0] < number:
        prev_number = current_footprint[1]
        if prev_number == INFINITY:
            break
        footprints.append(prev_number)
        current_footprint = min_operations[prev_number]

    return min_operations[-1][0], footprints


def main():
    number = int(input())
    min_operation, footprints = find_min_operation(number)
    print(min_operation)
    print(" ".join(str(i) for i in footprints))


main()
