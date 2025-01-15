import sys


def get_minimum_cost(sizes: list[int]):
    count = len(sizes)

    costs = [[0 for _ in range(count)] for _ in range(count)]
    for interval in range(1, count):
        for i in range(count - interval):
            j = i + interval
            prev_min = 10**9
            for mid in range(i + 1, j + 1):
                before_part = costs[i][mid - 1]
                after_part = costs[mid][j]
                prev_min = min(prev_min, before_part + after_part)
            costs[i][j] = prev_min + sum(sizes[i : j + 1])

    return costs[0][count - 1]


def main():
    repeat = int(input())
    for _ in range(repeat):
        _ = int(input())
        sizes = [int(s) for s in sys.stdin.readline().split()]
        minimum_cost = get_minimum_cost(sizes)
        print(minimum_cost)


main()
