import sys
from bisect import bisect_left


def is_inside(value: int, sorted_data: list[int]) -> bool:
    index = bisect_left(sorted_data, value)
    if index >= len(sorted_data):
        return False
    return sorted_data[index] == value


def main():
    _ = int(input())
    data = [int(s) for s in sys.stdin.readline().split()]
    sorted_data = sorted(data)
    _ = int(input())
    values = [int(s) for s in sys.stdin.readline().split()]
    for value in values:
        result = is_inside(value, sorted_data)
        sys.stdout.write("1\n" if result else "0\n")


main()
