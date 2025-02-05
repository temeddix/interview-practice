from typing import Generator, NamedTuple


def main():
    _ = int(input())
    numbers = [int(s) for s in input().split()]
    operation_count = OperationCount(*(int(s) for s in input().split()))
    min_result = INFINITY
    max_result = -INFINITY
    for operations in list_operations(operation_count):
        result = calculate_expression(numbers, operations)
        min_result = min(min_result, result)
        max_result = max(max_result, result)
    print(max_result)
    print(min_result)


class OperationCount(NamedTuple):
    addition: int
    subtraction: int
    multiplication: int
    division: int


class Job(NamedTuple):
    cleanup: bool
    operation: int


INFINITY = 1_000_000_007

ADDITION = 0
SUBTRACTION = 1
MULTIPLICATION = 2
DIVISION = 3

ALL_OPERATIONS = [ADDITION, SUBTRACTION, MULTIPLICATION, DIVISION]


def list_operations(
    operation_count: OperationCount,
) -> Generator[list[int], None, None]:
    # Goal counts
    goal_count = list(operation_count)
    goal_sum = sum(goal_count)
    # Current counts
    current_count = [0, 0, 0, 0]
    current_sum = 0
    # Actual operation list in order
    operations: list[int] = []

    dfs_stack: list[Job] = []
    for operation in ALL_OPERATIONS:
        if 0 < goal_count[operation]:
            dfs_stack.append(Job(True, operation))
            dfs_stack.append(Job(False, operation))

    while dfs_stack:
        cleanup, operation = dfs_stack.pop()

        if cleanup:
            operations.pop()
            current_count[operation] -= 1
            current_sum -= 1
            continue

        operations.append(operation)
        current_count[operation] += 1
        current_sum += 1

        if current_sum == goal_sum:
            yield operations
            continue

        for next in ALL_OPERATIONS:
            if current_count[next] == goal_count[next]:
                continue
            dfs_stack.append(Job(True, next))
            dfs_stack.append(Job(False, next))


def calculate_expression(numbers: list[int], operations: list[int]) -> int:
    result = numbers[0]

    for cursor in range(len(operations)):
        number = numbers[cursor + 1]
        operation = operations[cursor]

        if operation == ADDITION:
            result += number
        elif operation == SUBTRACTION:
            result -= number
        elif operation == MULTIPLICATION:
            result *= number
        elif operation == DIVISION:
            if result > 0:
                result = result // number
            else:
                result = -(-result // number)
        else:
            raise ValueError

    return result


main()
