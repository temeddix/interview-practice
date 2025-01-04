MOD = 1_000_000_007


def get_power(base: int, power: int) -> int:
    """This function returns the remainder of power modulo `MOD`."""
    result = 1
    base = base % MOD
    while power > 0:
        if power % 2 == 1:
            result = (result * base) % MOD
        base = (base * base) % MOD
        power //= 2
    return result


def get_factorial(n: int) -> int:
    """This function returns the remainder of factorial modulo `MOD`."""
    result = 1
    for i in range(1, n + 1):
        result = (result * i) % MOD
    return result


def get_remainder(n: int, k: int) -> int:
    """This function uses Fermat's Little Theorem."""
    # Calculate n! % MOD
    numerator = get_factorial(n)

    # Calculate k! and (n-k)! % MOD
    denominator_k = get_factorial(k)
    denominator_nk = get_factorial(n - k)

    # Using Fermat's Little Theorem to find modular inverses
    denominator = (denominator_k * denominator_nk) % MOD
    denominator_inv = get_power(denominator, MOD - 2)

    result = (numerator * denominator_inv) % MOD
    return result


def main():
    n, k = (int(s) for s in input().split())
    remainder = get_remainder(n, k)
    print(remainder)


main()
