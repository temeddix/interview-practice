from sys import stdin
from typing import NamedTuple


def main():
    map_size, shark_count, scent_duration = (int(s) for s in stdin.readline().split())

    shark_spots: list[Spot] = [Spot(-1, -1)] * shark_count
    for r in range(map_size):
        row = [int(s) for s in stdin.readline().split()]
        for c, shark_number in enumerate(row):
            if shark_number != 0:
                shark_spots[shark_number - 1] = Spot(r, c)
    shark_directions = [int(s) - 1 for s in stdin.readline().split()]

    sharks: list[list[list[Shark]]] = [
        [[] for _ in range(map_size)] for _ in range(map_size)
    ]
    for id, spot in enumerate(shark_spots):
        r, c = spot
        direction = shark_directions[id]
        direction_trait = [
            [int(s) - 1 for s in stdin.readline().split()]
            for _ in range(DIRECTION_COUNT)
        ]
        sharks[r][c].append(Shark(id, direction, direction_trait))

    scents: list[list[Scent | None]] = [[None] * map_size for _ in range(map_size)]
    environment = Environment(map_size, scent_duration, sharks, scents)
    seconds = simulate(environment)
    print(-1 if seconds is None else seconds)


class Spot(NamedTuple):
    row: int
    column: int


class Scent(NamedTuple):
    shark_id: int
    intensity: int


class Shark(NamedTuple):
    shark_id: int
    direction: int
    direction_trait: list[list[int]]


class Environment(NamedTuple):
    map_size: int
    scent_duration: int
    sharks: list[list[list[Shark]]]
    scents: list[list[Scent | None]]


DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
DIRECTION_COUNT = 4
MAX_SECONDS = 1000


def simulate(environment: Environment) -> int | None:
    _, _, sharks, _ = environment

    for i in range(MAX_SECONDS):
        move_sharks(environment)
        fade_scents(environment)
        shark_count = sum(sum(len(v) for v in r) for r in sharks)
        if shark_count == 1:
            return i + 1

    return None


def move_sharks(environment: Environment):
    map_size, scent_duration, sharks, scents = environment

    # Leave scent and move individual sharks.
    moved = set[int]()
    for r in range(map_size):
        for c in range(map_size):
            cell = sharks[r][c]
            if not cell:
                continue
            shark = cell[0]
            shark_id, direction, direction_trait = shark
            if shark_id in moved:
                continue

            scents[r][c] = Scent(shark_id, scent_duration)

            directions = [DIRECTIONS[i] for i in direction_trait[direction]]
            near_spots = [
                Spot(r + rd, c + cd)
                for rd, cd in directions
                if 0 <= r + rd < map_size and 0 <= c + cd < map_size
            ]
            near_clean_spots: list[Spot] = []
            near_self_spots: list[Spot] = []
            for nr, nc in near_spots:
                near_scent = scents[nr][nc]
                if near_scent is None:
                    near_clean_spots.append(Spot(nr, nc))
                elif near_scent.shark_id == shark_id:
                    near_self_spots.append(Spot(nr, nc))

            nr, nc = near_spots[0]
            if near_clean_spots:
                nr, nc = near_clean_spots[0]
            elif near_self_spots:
                nr, nc = near_self_spots[0]
            new_direction = DIRECTIONS.index((nr - r, nc - c))

            moved.add(shark_id)
            cell.pop(0)
            sharks[nr][nc].append(Shark(shark_id, new_direction, direction_trait))

    # Leave only one shark per cell.
    for r in range(map_size):
        for c in range(map_size):
            cell = sharks[r][c]
            if not cell:
                continue
            chosen_shark = min(cell)
            cell.clear()
            cell.append(chosen_shark)


def fade_scents(environment: Environment):
    map_size, _, _, scents = environment
    for r in range(map_size):
        for c in range(map_size):
            scent = scents[r][c]
            if scent is None:
                continue
            shark_id, intensity = scent
            intensity -= 1
            if intensity == 0:
                scents[r][c] = None
            else:
                scents[r][c] = Scent(shark_id, intensity)


main()
