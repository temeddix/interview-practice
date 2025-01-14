import heapq
import sys


def main():
    count = int(input())
    encoded_values: list[int] = []
    for _ in range(count):
        number = int(sys.stdin.readline())
        if number == 0:
            if not encoded_values:
                sys.stdout.write("0\n")
            else:
                encoded = heapq.heappop(encoded_values)
                number = (encoded + 1) // 2
                number *= -1 if encoded % 2 == 1 else 1
                sys.stdout.write(f"{number}\n")
        else:
            encoded = abs(number) * 2
            encoded -= 1 if number < 0 else 0
            heapq.heappush(encoded_values, encoded)


main()
