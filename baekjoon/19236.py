from typing import NamedTuple


def main():
    fish_map: list[list[Fish | None]] = []
    for _ in range(4):
        input_row = (int(s) for s in input().split())
        fish_row: list[Fish | None] = []
        fish_map.append(fish_row)
        for _ in range(4):
            size, d = next(input_row), next(input_row)
            d -= 1
            fish_row.append(Fish(size, d))
    eaten = simulate(fish_map)
    print(eaten)


class Spot(NamedTuple):
    row: int
    column: int


class Fish(NamedTuple):
    size: int
    direction: int


class Shark(NamedTuple):
    spot: Spot
    direction: int


DIRECTIONS = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
DIRECTION_COUNT = len(DIRECTIONS)


class Situation(NamedTuple):
    shark: Shark
    fish_map: list[list[Fish | None]]
    eaten: int


def simulate(initial_fish_map: list[list[Fish | None]]) -> int:
    first_fish = initial_fish_map[0][0]
    if first_fish is None:
        raise ValueError
    first_size, first_direction = first_fish

    max_eaten = 0
    first_shark = Shark(Spot(0, 0), first_direction)
    first_fish_map = [r.copy() for r in initial_fish_map]
    first_fish_map[0][0] = None
    first_eaten = first_size
    first_situation = Situation(first_shark, first_fish_map, first_eaten)

    dfs_stack: list[Situation] = [first_situation]
    while dfs_stack:
        situation = dfs_stack.pop()
        move_fish(situation)
        next_situations = move_shark(situation)
        if next_situations:
            dfs_stack.extend(next_situations)
        else:
            max_eaten = max(max_eaten, situation.eaten)

    return max_eaten


MAP_SIZE = 4


def move_fish(situation: Situation):
    shark, fish_map, _ = situation

    # Collect fish spots and sort them by size.
    fish_spots: list[Spot | None] = [None for _ in range(MAP_SIZE**2)]
    for r in range(MAP_SIZE):
        for c in range(MAP_SIZE):
            fish = fish_map[r][c]
            if fish is None:
                continue
            size, _ = fish
            fish_index = size - 1
            fish_spots[fish_index] = Spot(r, c)

    # Move fish from smallest to biggest.
    for fish_spot in fish_spots:
        if fish_spot is None:
            continue
        r, c = fish_spot
        fish = fish_map[r][c]
        if fish is None:
            raise ValueError
        size, direction = fish
        for _ in range(DIRECTION_COUNT):
            r_diff, c_diff = DIRECTIONS[direction]
            r_new, c_new = r + r_diff, c + c_diff
            if can_fish_exist(Spot(r_new, c_new), shark):
                existing = fish_map[r_new][c_new]
                fish_map[r][c] = existing
                fish_map[r_new][c_new] = Fish(size, direction)
                fish_spots[size - 1] = Spot(r_new, c_new)
                if existing is not None:
                    existing_size, _ = existing
                    fish_spots[existing_size - 1] = Spot(r, c)
                break
            direction = (direction + 1) % DIRECTION_COUNT


def move_shark(situation: Situation) -> list[Situation]:
    shark, fish_map, eaten = situation
    spot, direction = shark
    r_diff, c_diff = DIRECTIONS[direction]

    next_situations: list[Situation] = []
    r, c = spot
    while 0 <= r < MAP_SIZE and 0 <= c < MAP_SIZE:
        existing_fish = fish_map[r][c]
        if existing_fish is not None:
            next_fish_map = [r.copy() for r in fish_map]
            next_fish_map[r][c] = None
            size, direction = existing_fish
            next_eaten = eaten + size
            next_shark = Shark(Spot(r, c), direction)
            next_situation = Situation(next_shark, next_fish_map, next_eaten)
            next_situations.append(next_situation)
        r, c = r + r_diff, c + c_diff

    return next_situations


def can_fish_exist(spot: Spot, shark: Shark) -> bool:
    shark_spot, _ = shark
    if spot == shark_spot:
        return False
    row, column = spot
    return 0 <= row < MAP_SIZE and 0 <= column < MAP_SIZE


main()
