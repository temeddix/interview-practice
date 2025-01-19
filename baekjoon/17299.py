MAX_VALUE = 1_000_000


CountNumber = tuple[
    int,  # Number value
    int,  # Frequency count
]


def get_frequency_count(numbers: list[int]) -> list[int]:
    frequency_count: list[int] = [0 for _ in range(MAX_VALUE)]

    for number in numbers:
        frequency_count[number - 1] += 1

    return frequency_count


def get_ngf_list(numbers: list[int]) -> list[int]:
    """Calculates "Next greater frequency" for each number"""

    frequency_count = get_frequency_count(numbers)
    ngf_list: list[int] = []
    stack: list[CountNumber] = []  # Monotonic stack

    for number in reversed(numbers):
        while stack and stack[-1][1] <= frequency_count[number - 1]:
            stack.pop()
        if not stack:
            ngf_list.append(-1)
            stack.append((number, frequency_count[number - 1]))
            continue
        ngf_list.append(stack[-1][0])
        stack.append((number, frequency_count[number - 1]))

    return list(reversed(ngf_list))


def main():
    _ = input()
    numbers = [int(s) for s in input().split()]
    ngf_list = get_ngf_list(numbers)
    print(" ".join(str(i) for i in ngf_list))


main()
