import sys

Matrix = tuple[
    int,  # Row
    int,  # Column
]
DpCell = tuple[
    int,  # Cost
    Matrix,
]


def get_minimum_cost(matrices: list[Matrix]) -> int:
    count = len(matrices)

    dp_cells: list[list[DpCell]] = [
        [(0, (0, 0)) for _ in range(count)] for _ in range(count)
    ]
    for k in range(count):
        dp_cells[k][k] = (0, matrices[k])
    for interval in range(1, count):
        for i in range(count - interval):
            j = i + interval
            candidates: list[DpCell] = []
            for mid in range(i + 1, j + 1):
                before_part = dp_cells[i][mid - 1]
                after_part = dp_cells[mid][j]
                extra_cost = before_part[1][0] * before_part[1][1] * after_part[1][1]
                total_cost = before_part[0] + after_part[0] + extra_cost
                calculation = (total_cost, (before_part[1][0], after_part[1][1]))
                candidates.append(calculation)
            dp_cells[i][j] = min(candidates, key=lambda c: c[0])

    result_calculation = dp_cells[0][count - 1]
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
