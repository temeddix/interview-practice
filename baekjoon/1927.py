import heapq
import sys


def main():
    count = int(input())
    numbers: list[int] = []
    for _ in range(count):
        number = int(sys.stdin.readline())
        if number == 0:
            if not numbers:
                sys.stdout.write("0\n")
            else:
                biggest = heapq.heappop(numbers)
                sys.stdout.write(f"{biggest}\n")
        else:
            heapq.heappush(numbers, number)


main()
