from sys import stdin, stdout


def main():
    operation_count = int(input())
    number_set = [False for _ in range(SET_SIZE)]
    for _ in range(operation_count):
        operation = stdin.readline().strip()
        result = perform_operation(number_set, operation)
        if result is not None:
            stdout.write("1\n" if result else "0\n")


SET_SIZE = 20


def perform_operation(number_set: list[bool], operation: str) -> bool | None:
    if operation.startswith("add"):
        number = extract_number(operation)
        number_set[number] = True
    elif operation.startswith("remove"):
        number = extract_number(operation)
        number_set[number] = False
    elif operation.startswith("check"):
        number = extract_number(operation)
        return number_set[number]
    elif operation.startswith("toggle"):
        number = extract_number(operation)
        number_set[number] = not number_set[number]
    elif operation.startswith("all"):
        for i in range(len(number_set)):
            number_set[i] = True
    elif operation.startswith("empty"):
        for i in range(len(number_set)):
            number_set[i] = False


def extract_number(operation: str):
    splitted = operation.split()
    return int(splitted[-1]) - 1


main()
