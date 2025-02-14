from sys import stdin
from typing import Generator, NamedTuple


def main():
    fish_count, magic_count = (int(s) for s in stdin.readline().split())
    cells = [[Cell([], []) for _ in range(MAP_SIZE)] for _ in range(MAP_SIZE)]

    for _ in range(fish_count):
        x, y, d = (int(s) - 1 for s in stdin.readline().split())
        cells[x][y][0].append(Fish(d))

    x, y = (int(s) - 1 for s in stdin.readline().split())
    shark = Spot(x, y)

    simulate(cells, shark, magic_count)
    print(sum(sum(len(c[0]) for c in r) for r in cells))


MAP_SIZE = 4

FISH_DIRECTIONS = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
FISH_DIRECTION_COUNT = len(FISH_DIRECTIONS)


class Scent(NamedTuple):
    pass


class Spot(NamedTuple):
    row: int
    column: int


class Fish(NamedTuple):
    direction: int


SHARK_DIRECTIONS = [(-1, 0), (0, -1), (1, 0), (0, 1)]


class SharkMove(NamedTuple):
    fish_eaten: int
    first: int
    second: int
    third: int


class Cell(NamedTuple):
    fish: list[Fish]
    scents: list[Scent]


NEW_SCENT = 3


def simulate(cells: list[list[Cell]], shark: Spot, magic_count: int):
    magic_buffer = [[list[Fish]() for _ in range(MAP_SIZE)] for _ in range(MAP_SIZE)]

    for _ in range(magic_count):
        # Move all fish to the magic buffer.
        for r, c in iterate_map():
            magic_buffer[r][c].extend(cells[r][c][0])
            cells[r][c][0].clear()

        # Get fish from the magic buffer, changing their locations.
        for r, c in iterate_map():
            buffer_fish = magic_buffer[r][c]
            for fish in buffer_fish:
                moved_fish, spot = move_fish(fish, Spot(r, c), cells, shark)
                r_next, c_next = spot
                cells[r_next][c_next][0].append(moved_fish)

        # Move the shark.
        shark_move = move_shark(cells, shark)
        _, first_move, second_move, third_move = shark_move
        move_vecs = (SHARK_DIRECTIONS[i] for i in (first_move, second_move, third_move))
        for r_diff, c_diff in move_vecs:
            r_shark, c_shark = shark
            r_next, c_next = r_shark + r_diff, c_shark + c_diff
            shark = Spot(r_next, c_next)
            cell = cells[r_next][c_next]
            fish_list, scent_list = cell
            if fish_list:
                fish_list.clear()
                scent_list.clear()
                scent_list.extend(Scent() for _ in range(NEW_SCENT))

        # Fade scents.
        for r, c in iterate_map():
            scent_list = cells[r][c][1]
            if scent_list:
                scent_list.pop()

        # Copy fish from the previous state.
        for r, c in iterate_map():
            fish_list = cells[r][c][0]
            fish_list.extend(magic_buffer[r][c])
            magic_buffer[r][c].clear()


def iterate_map() -> Generator[Spot, None, None]:
    for r in range(MAP_SIZE):
        for c in range(MAP_SIZE):
            yield Spot(r, c)


def move_fish(
    fish: Fish, spot: Spot, cells: list[list[Cell]], shark: Spot
) -> tuple[Fish, Spot]:
    direction = fish[0]
    r, c = spot

    next_spot = spot
    next_direction = direction
    for _ in range(FISH_DIRECTION_COUNT):
        r_diff, c_diff = FISH_DIRECTIONS[direction]
        r_new, c_new = r + r_diff, c + c_diff
        new_spot = Spot(r_new, c_new)

        if 0 <= r_new < MAP_SIZE and 0 <= c_new < MAP_SIZE:
            avoids_shark = new_spot != shark
            avoids_smell = not cells[r_new][c_new][1]

            if avoids_shark and avoids_smell:
                next_direction = direction
                next_spot = new_spot
                break

        direction = (direction - 1) % FISH_DIRECTION_COUNT

    return Fish(next_direction), next_spot


class Job(NamedTuple):
    is_head: bool
    spot: Spot
    direction: int
    fish_eaten: int
    is_new_visit: bool


NO_DIRECTION = 1_000_000_007
SHARK_MOVEMENT = 3


def move_shark(cells: list[list[Cell]], shark: Spot) -> SharkMove:
    visited = [[False] * MAP_SIZE for _ in range(MAP_SIZE)]
    move_stack: list[int] = []

    shark_move = SharkMove(0, NO_DIRECTION, NO_DIRECTION, NO_DIRECTION)
    dfs_stack = [
        Job(False, shark, NO_DIRECTION, 0, False),
        Job(True, shark, NO_DIRECTION, 0, False),
    ]

    while dfs_stack:
        is_head, spot, direction, fish_eaten, is_new_visit = dfs_stack.pop()
        r, c = spot

        if is_head:
            move_stack.append(direction)
            if is_new_visit:
                visited[r][c] = True

            if len(move_stack) == SHARK_MOVEMENT + 1:
                new_move = SharkMove(
                    -fish_eaten,
                    move_stack[-3],
                    move_stack[-2],
                    move_stack[-1],
                )
                shark_move = min(shark_move, new_move)
                continue

            for next_direction, next_vec in enumerate(SHARK_DIRECTIONS):
                r_diff, c_diff = next_vec
                r_next, c_next = r + r_diff, c + c_diff
                if not (0 <= r_next < MAP_SIZE and 0 <= c_next < MAP_SIZE):
                    continue
                next_eaten = fish_eaten
                is_new_visit = not visited[r_next][c_next]
                if is_new_visit:
                    next_eaten += len(cells[r_next][c_next][0])
                next_spot = Spot(r_next, c_next)
                dfs_stack.append(
                    Job(False, next_spot, next_direction, next_eaten, is_new_visit)
                )
                dfs_stack.append(
                    Job(True, next_spot, next_direction, next_eaten, is_new_visit)
                )

        else:
            move_stack.pop()
            if is_new_visit:
                visited[r][c] = False

    return shark_move


main()
