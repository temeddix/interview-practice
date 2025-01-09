import sys


def multiply_matrix(
    matrix_a: list[list[int]],
    matrix_b: list[list[int]],
) -> list[list[int]]:
    result_matrix: list[list[int]] = []
    matrix_size = len(matrix_a)

    for i in range(matrix_size):
        new_row: list[int] = []
        for j in range(matrix_size):
            value = 0
            for k in range(matrix_size):
                value_a = matrix_a[i][k]
                value_b = matrix_b[k][j]
                value += value_a * value_b
            new_row.append(value % 1000)
        result_matrix.append(new_row)

    return result_matrix


def raise_matrix_to_power(
    matrix: list[list[int]],
    power: int,
) -> list[list[int]]:
    # Initial multiplication
    powered_matrix = matrix
    power -= 1

    # Repeat multiplication
    base_matrix = matrix
    while power > 0:
        if power % 2 == 1:
            powered_matrix = multiply_matrix(powered_matrix, base_matrix)
        base_matrix = multiply_matrix(base_matrix, base_matrix)
        power = power // 2

    return powered_matrix


def main():
    matrix_size, power = (int(s) for s in input().split())

    matrix: list[list[int]] = []
    for _ in range(matrix_size):
        row = [int(s) % 1000 for s in sys.stdin.readline().split()]
        matrix.append(row)

    powered_matrix = raise_matrix_to_power(matrix, power)
    lines = [" ".join(str(i) for i in r) for r in powered_matrix]
    sys.stdout.write("\n".join(lines))


main()
