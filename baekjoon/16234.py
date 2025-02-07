from sys import stdin
from typing import NamedTuple


def main():
    map_size, low_limit, high_limit = (int(s) for s in input().split())
    agreement = Agreement(low_limit, high_limit)
    people: list[list[int]] = []
    for _ in range(map_size):
        row = [int(s) for s in stdin.readline().split()]
        people.append(row)
    migration_days = count_migration_days(map_size, people, agreement)
    print(migration_days)


class Agreement(NamedTuple):
    low_limit: int
    high_limit: int


class Spot(NamedTuple):
    row: int
    column: int


MAX_DAYS = 2000


def count_migration_days(
    map_size: int, people: list[list[int]], agreement: Agreement
) -> int:
    visited: list[list[bool]] = [[False] * map_size for _ in range(map_size)]
    allies: list[list[list[Spot]]] = [
        [[] for _ in range(map_size)] for _ in range(map_size)
    ]

    migration_days = 0
    for _ in range(MAX_DAYS):
        create_agreements(map_size, allies, people, agreement)
        did_spread = spread_people(map_size, allies, people, visited)
        clear_record(map_size, allies, visited)
        if not did_spread:
            break
        migration_days += 1

    return migration_days


def create_agreements(
    map_size: int,
    allies: list[list[list[Spot]]],
    people: list[list[int]],
    agreement: Agreement,
):
    # Check vertical and horizontal borders.
    for i in range(map_size):
        for j in range(map_size - 1):
            left_people = people[i][j]
            right_people = people[i][j + 1]
            if is_ally(left_people, right_people, agreement):
                allies[i][j].append(Spot(i, j + 1))
                allies[i][j + 1].append(Spot(i, j))
    for i in range(map_size - 1):
        for j in range(map_size):
            up_people = people[i][j]
            down_people = people[i + 1][j]
            if is_ally(up_people, down_people, agreement):
                allies[i][j].append(Spot(i + 1, j))
                allies[i + 1][j].append(Spot(i, j))


def spread_people(
    map_size: int,
    allies: list[list[list[Spot]]],
    people: list[list[int]],
    visited: list[list[bool]],
) -> bool:
    did_spread = False

    # Group countries and spread the people.
    for i in range(map_size):
        for j in range(map_size):
            # Do nothing if this country was already checked.
            if visited[i][j]:
                continue

            # Use DFS.
            alliance: list[Spot] = []
            dfs_stack: list[Spot] = []
            dfs_stack.append(Spot(i, j))
            while dfs_stack:
                country = dfs_stack.pop()
                row, column = country
                if visited[row][column]:
                    continue
                alliance.append(country)
                visited[row][column] = True
                for ally in allies[row][column]:
                    dfs_stack.append(ally)
                    did_spread = True

            # Spread the people across countries.
            people_sum = sum(people[r][c] for r, c in alliance)
            people_each = people_sum // len(alliance)
            for row, column in alliance:
                people[row][column] = people_each

    return did_spread


def clear_record(
    map_size: int,
    allies: list[list[list[Spot]]],
    visited: list[list[bool]],
):
    for i in range(map_size):
        for j in range(map_size):
            allies[i][j].clear()
            visited[i][j] = False


def is_ally(people_a: int, people_b: int, agreement: Agreement) -> bool:
    low_limit, high_limit = agreement
    diff = abs(people_a - people_b)
    return low_limit <= diff <= high_limit


main()
