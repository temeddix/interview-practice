def count_pairs(number: int, primes: list[int]) -> int:
    if not primes:
        return 0

    prime_count = len(primes)
    max_cursor = prime_count - 1
    left_cursor = 0
    right_cursor = 0

    sum_value = primes[0]
    pair_count = 0
    while True:
        if sum_value < number:
            if right_cursor == max_cursor:
                break
            right_cursor += 1
            sum_value += primes[right_cursor]
        elif sum_value > number:
            sum_value -= primes[left_cursor]
            left_cursor += 1
        else:
            pair_count += 1
            if right_cursor == max_cursor:
                break
            right_cursor += 1
            sum_value += primes[right_cursor]

    return pair_count


def sieve_primes(number: int) -> list[int]:
    is_prime = [True for _ in range(number + 1)]
    is_prime[0] = False
    is_prime[1] = False

    divider = 1
    while divider < number:
        divider += 1
        if not is_prime[divider]:
            continue
        for i in range(2, number // divider + 1):
            is_prime[i * divider] = False

    primes: list[int] = []
    for i, is_prime in enumerate(is_prime):
        if is_prime:
            primes.append(i)

    return primes


def main():
    number = int(input())
    primes = sieve_primes(number)
    pair_count = count_pairs(number, primes)
    print(pair_count)


main()
