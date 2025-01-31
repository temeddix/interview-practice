from sys import stdin, stdout
from typing import NamedTuple


def main():
    operation_count = int(input())
    bitmask = 0
    for _ in range(operation_count):
        operation = stdin.readline().strip()
        bitmask, checked = perform_operation(bitmask, operation)
        if checked is not None:
            stdout.write("1\n" if checked else "0\n")


MAX_BITMASK = (1 << 20) - 1
MIN_BITMASK = 0


class Output(NamedTuple):
    bitmask: int
    checked: bool | None


def perform_operation(bitmask: int, operation: str) -> Output:
    if operation.startswith("check"):
        number = extract_number(operation)
        checked = bool(bitmask & (1 << number))
        output = Output(bitmask, checked)
    elif operation.startswith("add"):
        number = extract_number(operation)
        bitmask = bitmask | (1 << number)
        output = Output(bitmask, None)
    elif operation.startswith("remove"):
        number = extract_number(operation)
        bitmask = bitmask & ~(1 << number)
        output = Output(bitmask, None)
    elif operation.startswith("toggle"):
        number = extract_number(operation)
        bitmask = bitmask ^ (1 << number)
        output = Output(bitmask, None)
    elif operation.startswith("all"):
        bitmask = MAX_BITMASK
        output = Output(bitmask, None)
    elif operation.startswith("empty"):
        bitmask = MIN_BITMASK
        output = Output(bitmask, None)
    else:
        raise ValueError

    return output


def extract_number(operation: str):
    splitted = operation.split()
    return int(splitted[-1]) - 1


main()
