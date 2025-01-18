import sys

MAX_COST = 2**31 - 1

Matrix = tuple[
    int,  # Row
    int,  # Column
]


def get_minimum_cost(matrices: list[Matrix]) -> int:
    count = len(matrices)
    dp_costs = [[0 for _ in range(count)] for _ in range(count)]

    for interval in range(1, count):
        for i in range(count - interval):
            j = i + interval
            dp_cost = MAX_COST
            for mid in range(i + 1, j + 1):
                cost = (
                    dp_costs[i][mid - 1]
                    + dp_costs[mid][j]
                    + matrices[i][0] * matrices[mid][0] * matrices[j][1]
                )
                dp_cost = min(dp_cost, cost)
            dp_costs[i][j] = dp_cost

    return dp_costs[0][count - 1]


def main():
    matrix_count = int(input())
    matrices: list[Matrix] = []
    for _ in range(matrix_count):
        row, column = (int(s) for s in sys.stdin.readline().split())
        matrix = (row, column)
        matrices.append(matrix)
    minimum_cost = get_minimum_cost(matrices)
    print(minimum_cost)


main()
