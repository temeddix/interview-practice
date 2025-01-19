def get_nge_list(numbers: list[int]) -> list[int]:
    """Calculates "Next greater element" for each number"""

    nge_list: list[int] = []
    monotonic_stack: list[int] = []

    for number in reversed(numbers):
        while monotonic_stack and monotonic_stack[-1] <= number:
            monotonic_stack.pop()
        if not monotonic_stack:
            nge_list.append(-1)
            monotonic_stack.append(number)
            continue
        nge_list.append(monotonic_stack[-1])
        monotonic_stack.append(number)

    return list(reversed(nge_list))


def main():
    _ = input()
    numbers = [int(s) for s in input().split()]
    nge_list = get_nge_list(numbers)
    print(" ".join(str(i) for i in nge_list))


main()
