import sys
from bisect import bisect_left


def main():
    _ = int(input())
    numbers = [int(s) for s in sys.stdin.readline().split()]
    lis = [0]  # Longest increasing subsequence
    for number in numbers:
        if number > lis[-1]:
            lis.append(number)
        else:
            index = bisect_left(lis, number)
            lis[index] = number
    print(len(lis) - 1)


main()
