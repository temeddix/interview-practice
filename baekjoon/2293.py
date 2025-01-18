import sys


def get_combinations(goal_value: int, coins: set[int]) -> int:
    value_combinations: list[int] = [0 for _ in range(goal_value + 1)]
    value_combinations[0] = 1

    for coin in sorted(coins, reverse=True):
        for value in range(1, goal_value + 1):
            value_combination = 0
            prev_value = value - coin
            if prev_value < 0:
                continue
            prev_combination = value_combinations[prev_value]
            value_combination += prev_combination
            value_combinations[value] += value_combination

    return value_combinations[-1]


def main():
    coin_count, goal_value = (int(s) for s in input().split())
    coins = set[int]()
    for _ in range(coin_count):
        coin = int(sys.stdin.readline())
        coins.add(coin)
    combintations = get_combinations(goal_value, coins)
    print(combintations)


main()
