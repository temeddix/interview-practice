import sys
from dataclasses import dataclass


@dataclass
class BaseReachCount:
    recursive: int
    dynamic: int


base_reach_count = BaseReachCount(recursive=0, dynamic=0)


def fib_recursive(n: int) -> int:
    if n in (1, 2):
        base_reach_count.recursive += 1
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_dynamic(n: int) -> int:
    values: list[int] = []
    values.append(1)
    values.append(1)
    for i in range(2, n):
        base_reach_count.dynamic += 1
        new_value = values[i - 1] + values[i - 2]
        values.append(new_value)
    return values[-1]


def main():
    n = int(sys.stdin.readline())
    value = fib_dynamic(n)
    print(f"{value} {base_reach_count.dynamic}")


main()
