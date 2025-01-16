import sys
from dataclasses import dataclass


@dataclass
class Matrix:
    row: int
    column: int


@dataclass
class Calculation:
    cost: int
    matrix: Matrix


def get_minimum_cost(matrices: list[Matrix]) -> int:
    count = len(matrices)

    costs: list[list[Calculation | None]] = [
        [None for _ in range(count)] for _ in range(count)
    ]
    for k in range(count):
        costs[k][k] = Calculation(cost=0, matrix=matrices[k])
    for interval in range(1, count):
        for i in range(count - interval):
            j = i + interval
            candidates: list[Calculation] = []
            for mid in range(i + 1, j + 1):
                before_part = costs[i][mid - 1]
                after_part = costs[mid][j]
                if before_part is None or after_part is None:
                    raise NotImplementedError
                extra_cost = (
                    before_part.matrix.row
                    * before_part.matrix.column
                    * after_part.matrix.column
                )
                calculation = Calculation(
                    cost=before_part.cost + after_part.cost + extra_cost,
                    matrix=Matrix(before_part.matrix.row, after_part.matrix.column),
                )
                candidates.append(calculation)
            costs[i][j] = min(candidates, key=lambda c: c.cost)

    result_matrix = costs[0][count - 1]
    if result_matrix is None:
        raise NotImplementedError
    return result_matrix.cost


def main():
    matrix_count = int(input())
    matrices: list[Matrix] = []
    for _ in range(matrix_count):
        row, column = (int(s) for s in sys.stdin.readline().split())
        matrix = Matrix(row=row, column=column)
        matrices.append(matrix)
    minimum_cost = get_minimum_cost(matrices)
    print(minimum_cost)


main()
