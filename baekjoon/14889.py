from itertools import combinations
from typing import NamedTuple


def main():
    people_count = int(input())
    people = list(range(people_count))
    team_size = people_count // 2
    ability_table: list[list[int]] = []
    for _ in range(people_count):
        row = [int(s) for s in input().split()]
        ability_table.append(row)
    min_diff = INFINITY
    for home_team in combinations(people, team_size):
        result = calculate_ability_diff(
            people_count,
            list(home_team),
            ability_table,
        )
        min_diff = min(min_diff, result)
    print(min_diff)


class Job(NamedTuple):
    cleanup: bool
    is_ours: bool


INFINITY = 1_000_000_007


def calculate_ability_diff(
    people_count: int,
    home_team: list[int],
    ability_table: list[list[int]],
) -> int:
    team_size = len(home_team)

    other_team: list[int] = []
    cursor = 0
    for person_index in range(people_count):
        if cursor < team_size and home_team[cursor] == person_index:
            cursor += 1
            continue
        other_team.append(person_index)

    home_ability = 0
    for i, j in combinations(home_team, 2):
        home_ability += ability_table[i][j]
        home_ability += ability_table[j][i]

    other_ability = 0
    for i, j in combinations(other_team, 2):
        other_ability += ability_table[i][j]
        other_ability += ability_table[j][i]

    return abs(home_ability - other_ability)


main()
