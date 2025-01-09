DIVIDER = 1_000_000_007


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
            new_row.append(value % DIVIDER)
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


def get_pivonacci(n: int) -> int:
    multiplier_matrix = raise_matrix_to_power([[0, 1], [1, 1]], n - 1)
    return multiplier_matrix[1][1]


def main():
    n = int(input().strip())
    result = get_pivonacci(n)
    print(result)


main()
