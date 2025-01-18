import sys

Matrix = tuple[
    int,  # Row
    int,  # Column
]
Cell = tuple[
    int,  # Cost
    Matrix,
]


def get_minimum_cost(matrices: list[Matrix]) -> int:
    count = len(matrices)

    costs: list[list[Cell | None]] = [
        [None for _ in range(count)] for _ in range(count)
    ]
    for k in range(count):
        costs[k][k] = (0, matrices[k])
    for interval in range(1, count):
        for i in range(count - interval):
            j = i + interval
            candidates: list[Cell] = []
            for mid in range(i + 1, j + 1):
                before_part = costs[i][mid - 1]
                after_part = costs[mid][j]
                if before_part is None or after_part is None:
                    raise NotImplementedError
                extra_cost = before_part[1][0] * before_part[1][1] * after_part[1][1]
                calculation = (
                    before_part[0] + after_part[0] + extra_cost,
                    (before_part[1][0], after_part[1][1]),
                )
                candidates.append(calculation)
            costs[i][j] = min(candidates, key=lambda c: c[0])

    result_calculation = costs[0][count - 1]
    if result_calculation is None:
        raise NotImplementedError
    return result_calculation[0]


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
