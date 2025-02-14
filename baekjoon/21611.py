from sys import stdin
from typing import NamedTuple


def main():
    map_size, magic_count = (int(s) for s in stdin.readline().split())

    marble_grid: list[list[int]] = []
    for _ in range(map_size):
        row = [int(s) for s in stdin.readline().split()]
        marble_grid.append(row)

    magics: list[Magic] = []
    for _ in range(magic_count):
        d, s = (int(s) for s in stdin.readline().split())
        d -= 1
        magics.append(Magic(d, s))

    index_map = create_index_map(map_size)
    marbles = connect_marbles(map_size, marble_grid, index_map)
    shark = Spot(map_size // 2, map_size // 2)
    marble_map = MarbleMap(map_size, shark, index_map, marbles)

    explosion_score = simulate(marble_map, magics)
    print(explosion_score)


MAGIC_DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
EMPTY = 0


class Spot(NamedTuple):
    row: int
    column: int


class Magic(NamedTuple):
    direction: int
    distance: int


class IndexMap(NamedTuple):
    index_to_spot: list[Spot]
    spot_to_index: list[list[int]]


class MarbleMap(NamedTuple):
    map_size: int
    shark: Spot
    index_map: IndexMap
    marbles: list[int]


def simulate(marble_map: MarbleMap, magics: list[Magic]) -> int:
    marbles = marble_map.marbles

    explosion_score = 0
    for magic in magics:
        destroy_marbles(marble_map, magic)
        while True:
            new_explosion_score = blow_up_marbles(marbles)
            if new_explosion_score == 0:
                break
            explosion_score += new_explosion_score
        convert_marbles(marbles)

    return explosion_score


def pull_marbles(marbles: list[int]):
    buffer = [m for m in marbles if m != EMPTY]
    for i, m in enumerate(buffer):
        marbles[i] = m
    for i in range(len(buffer), len(marbles)):
        marbles[i] = EMPTY


def destroy_marbles(marble_map: MarbleMap, magic: Magic):
    _, shark, index_map, marbles = marble_map
    _, spot_to_index = index_map
    direction, distance = magic

    r_vec, c_vec = MAGIC_DIRECTIONS[direction]
    destroyed_spots: list[Spot] = []
    current_spot = shark
    for _ in range(distance):
        r, c = current_spot
        current_spot = Spot(r + r_vec, c + c_vec)
        destroyed_spots.append(current_spot)

    for i in (spot_to_index[r][c] for r, c in destroyed_spots):
        marbles[i] = EMPTY

    pull_marbles(marbles)


EXPLOSION_GROUP = 4


def blow_up_marbles(marbles: list[int]) -> int:
    bead_size = len(marbles)

    explosion_score = 0
    pointer = 0
    while pointer < bead_size:
        base_pointer = pointer
        base_marble = marbles[pointer]
        if base_marble == EMPTY:
            break
        while pointer < bead_size and marbles[pointer] == base_marble:
            pointer += 1
        group_size = pointer - base_pointer
        if group_size >= EXPLOSION_GROUP:
            explosion_score += base_marble * group_size
            for i in range(base_pointer, pointer):
                marbles[i] = EMPTY

    if explosion_score > 0:
        pull_marbles(marbles)

    return explosion_score


def convert_marbles(marbles: list[int]):
    bead_size = len(marbles)
    buffer: list[int] = []

    pointer = 0
    while pointer < bead_size:
        base_pointer = pointer
        base_marble = marbles[pointer]
        if base_marble == EMPTY:
            break
        streak = 0
        while pointer < bead_size and marbles[pointer] == base_marble:
            streak += 1
            pointer += 1
        group_size = pointer - base_pointer
        buffer.append(group_size)
        buffer.append(base_marble)

    overwrite = min(bead_size, len(buffer))
    for i in range(overwrite):
        marbles[i] = buffer[i]
    for i in range(overwrite, bead_size):
        marbles[i] = EMPTY


def connect_marbles(
    map_size: int,
    marble_grid: list[list[int]],
    index_map: IndexMap,
) -> list[int]:
    connected: list[int] = []
    index_to_spot, _ = index_map

    for i in range(map_size**2 - 1):
        r, c = index_to_spot[i]
        marble = marble_grid[r][c]
        connected.append(marble)

    return connected


SPIRAL_DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]
SPIRAL_DIRECTION_COUNT = len(SPIRAL_DIRECTIONS)
SAME_EDGE_COUNT = 2


def create_index_map(map_size: int) -> IndexMap:
    index_to_spot: list[Spot] = []
    spot_to_index = [[-1] * map_size for _ in range(map_size)]

    direction = 0
    current_spot = Spot(map_size // 2, map_size // 2)

    edge_length = 1
    edge_reached = 0
    straight_dist = 0
    for i in range(map_size**2 - 1):
        r_diff, c_diff = SPIRAL_DIRECTIONS[direction]
        r_prev, c_prev = current_spot
        r_now, c_now = r_prev + r_diff, c_prev + c_diff

        current_spot = Spot(r_now, c_now)
        index_to_spot.append(current_spot)
        spot_to_index[r_now][c_now] = i

        straight_dist += 1
        if straight_dist == edge_length:
            edge_reached += 1
            straight_dist = 0
            direction = (direction + 1) % SPIRAL_DIRECTION_COUNT
        if edge_reached == SAME_EDGE_COUNT:
            edge_length += 1
            edge_reached = 0
            straight_dist = 0

    return IndexMap(index_to_spot, spot_to_index)


main()
