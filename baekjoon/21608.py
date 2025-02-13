from sys import stdin
from typing import NamedTuple


def main():
    map_size = int(input())
    students: list[Student] = []
    for _ in range(map_size**2):
        line_input = (int(s) - 1 for s in stdin.readline().split())
        id = next(line_input)
        favorites = [next(line_input) for _ in range(4)]
        students.append(Student(id, favorites))
    placed = place_students(map_size, students)
    satisfaction_score = ask_satisfaction_score(map_size, placed)
    print(satisfaction_score)


class Student(NamedTuple):
    id: int
    favorites: list[int]


class Spot(NamedTuple):
    row: int
    column: int


class Placing(NamedTuple):
    near_favorites: int
    near_empty: int
    spot: Spot


ADJACENTS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def place_students(map_size: int, students: list[Student]) -> list[list[Student]]:
    blocks: list[list[Student | None]] = [[None] * map_size for _ in range(map_size)]

    for student in students:
        # Collect placing scores.
        placings: list[Placing] = []
        for r in range(map_size):
            for c in range(map_size):
                if blocks[r][c] is not None:
                    continue
                near_favorites = 0
                near_empty = 0
                for r_diff, c_diff in ADJACENTS:
                    r_next, c_next = r + r_diff, c + c_diff
                    if 0 <= r_next < map_size and 0 <= c_next < map_size:
                        friend = blocks[r_next][c_next]
                        if friend is None:
                            near_empty += 1
                        elif friend.id in student.favorites:
                            near_favorites += 1
                placings.append(Placing(-near_favorites, -near_empty, Spot(r, c)))

        # Choose the best placing option by preference.
        placings.sort()
        placing = placings[0]
        _, _, spot = placing

        # Place the student.
        r, c = spot
        blocks[r][c] = student

    return [[s for s in r if s is not None] for r in blocks]


def ask_satisfaction_score(map_size: int, placed: list[list[Student]]) -> int:
    satisfaction_score = 0

    for r in range(map_size):
        for c in range(map_size):
            student = placed[r][c]
            near_favorites = 0
            for r_diff, c_diff in ADJACENTS:
                r_next, c_next = r + r_diff, c + c_diff
                if 0 <= r_next < map_size and 0 <= c_next < map_size:
                    friend = placed[r_next][c_next]
                    if friend.id in student.favorites:
                        near_favorites += 1
            score = 10 ** (near_favorites - 1) if near_favorites else 0
            satisfaction_score += score

    return satisfaction_score


main()
