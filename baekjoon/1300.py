def get_index(size: int, value: int):
    """
    Counts how many numbers are
    smaller or equal to this value.
    If there are multiple same values,
    this function returns the index of the last one.
    """
    index = 0
    for i in range(size):
        index += min(size, value // (i + 1))
    return index - 1


def get_value_with_bisect(size: int, index: int) -> int:
    left = 1  # Inclusive
    right = size**2  # Inclusive

    result_value = None
    while left <= right:
        mid = (right + left) // 2
        test_index = get_index(size, mid)
        if test_index >= index:
            result_value = mid
            right = mid - 1
        else:
            left = mid + 1

    if result_value is None:
        raise NotImplementedError

    return result_value


def main():
    size = int(input())
    index = int(input()) - 1
    value = get_value_with_bisect(size, index)
    print(value)


main()
