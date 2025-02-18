from itertools import combinations
from math import gcd
from typing import Generator, NamedTuple


def main():
    number_count = int(input())
    numbers: list[str] = []
    for _ in range(number_count):
        numbers.append(input())
    divider = int(input())
    ten_remainders = get_ten_remainders(MAX_CHARS, divider)
    number_infos = [get_number_info(n, divider, ten_remainders) for n in numbers]
    fraction = get_success_ratio(number_infos, divider, ten_remainders)
    print(f"{fraction.numerator}/{fraction.denominator}")


MAX_CHARS = 50


class NumberInfo(NamedTuple):
    remainder: int
    digits: int


class Fraction(NamedTuple):
    numerator: int
    denominator: int


def get_success_ratio(
    number_infos: list[NumberInfo], divider: int, ten_remainders: list[int]
) -> Fraction:
    # The first level index is chosen indices represented in bits.
    # The second level index means if that remainder can be occur.
    number_count = len(number_infos)
    dp_array = [[0] * divider for _ in range(2**number_count)]
    dp_array[0][0] = 1

    # Find possible remainders per combination with dynamic programming.
    for i in range(number_count):
        for index in get_indices(number_count, i + 1):
            for prev_index, new_chosen in get_prev_indices(number_count, index):
                number_info = number_infos[new_chosen]
                remainder, digits = number_info
                ten_remainder = ten_remainders[digits]
                for d in range(divider):
                    prev_possibilities = dp_array[prev_index][d]
                    new_remainder = (d * ten_remainder + remainder) % divider
                    dp_array[index][new_remainder] += prev_possibilities

    success = dp_array[-1][0]
    all_possibilities = sum(dp_array[-1])
    gcd_value = gcd(success, all_possibilities)

    return Fraction(success // gcd_value, all_possibilities // gcd_value)


def get_indices(number_count: int, chosen_count: int) -> Generator[int, None, None]:
    for combination in combinations(range(number_count), chosen_count):
        index = 0
        for person in combination:
            index = index | (1 << person)
        yield index


class PrevInfo(NamedTuple):
    dp_index: int
    new_chosen: int


def get_prev_indices(number_count: int, index: int) -> Generator[PrevInfo, None, None]:
    for new_chosen in range(number_count):
        prev_index = index & ~(1 << new_chosen)
        if prev_index != index:
            yield PrevInfo(prev_index, new_chosen)


def get_number_info(
    raw_number: str, divider: int, ten_remainders: list[int]
) -> NumberInfo:
    remainder = 0
    for p, char in enumerate(reversed(raw_number)):
        ten_remainder = ten_remainders[p]
        remainder = (remainder + int(char) * ten_remainder) % divider
    digits = len(raw_number)
    return NumberInfo(remainder, digits)


def get_ten_remainders(max_power: int, divider: int) -> list[int]:
    ten_remainders: list[int] = [1]
    ten_remainder = 1
    for _ in range(max_power):
        ten_remainder = (ten_remainder * 10) % divider
        ten_remainders.append(ten_remainder)
    return ten_remainders


main()
