from collections import deque
from typing import NamedTuple


def main():
    map_size, passenger_count, initial_fuel = (int(s) for s in input().split())
    walls: list[list[bool]] = []
    for _ in range(map_size):
        row = [True if s == "1" else False for s in input().split()]
        walls.append(row)
    start_spot = Spot(*(int(s) - 1 for s in input().split()))
    passengers: list[Passenger] = []
    for _ in range(passenger_count):
        r_from, c_from, r_to, c_to = (int(s) - 1 for s in input().split())
        passengers.append(Passenger(Spot(r_from, c_from), Spot(r_to, c_to)))
    block_map = BlockMap(map_size, walls)
    remaining_fuel = drive_taxi(block_map, passengers, start_spot, initial_fuel)
    print(-1 if remaining_fuel is None else remaining_fuel)


class Spot(NamedTuple):
    row: int
    column: int


class Passenger(NamedTuple):
    go_from: Spot
    go_to: Spot


class BlockMap(NamedTuple):
    map_size: int
    walls: list[list[bool]]


def drive_taxi(
    block_map: BlockMap,
    passengers: list[Passenger],
    start_spot: Spot,
    initial_fuel: int,
) -> int | None:
    passenger_count = len(passengers)

    taxi_spot = start_spot
    taxi_fuel = initial_fuel

    for _ in range(passenger_count):
        dists = find_dists(block_map, [p[0] for p in passengers], taxi_spot)
        dist = min(dists)
        if dist == UNREACHABLE:
            return None
        min_dist_indices = [i for i in range(len(passengers)) if dists[i] == dist]
        passenger_index = min(min_dist_indices, key=lambda i: passengers[i].go_from)
        passenger = passengers[passenger_index]
        go_from, go_to = passenger
        taxi_spot = go_from
        taxi_fuel -= dist
        if taxi_fuel < 0:
            return None
        service_dist = find_dists(block_map, [go_to], go_from)[0]
        taxi_spot = go_to
        taxi_fuel -= service_dist
        if taxi_fuel < 0:
            return None
        taxi_fuel += service_dist * 2
        passengers.pop(passenger_index)

    return taxi_fuel


UNREACHABLE = -1
ADJACENTS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


class Job(NamedTuple):
    spot: Spot
    dist: int


def find_dists(block_map: BlockMap, spots: list[Spot], base: Spot) -> list[int]:
    map_size, walls = block_map
    dists = [[UNREACHABLE] * map_size for _ in range(map_size)]

    bfs_deque = deque[Job]()
    bfs_deque.append(Job(base, 0))

    while bfs_deque:
        spot, dist = bfs_deque.popleft()
        r, c = spot
        if dists[r][c] != UNREACHABLE:
            continue
        dists[r][c] = dist
        for r_diff, c_diff in ADJACENTS:
            r_new, c_new = r + r_diff, c + c_diff
            if not (0 <= r_new < map_size and 0 <= c_new < map_size):
                continue
            if walls[r_new][c_new] or dists[r_new][c_new] != UNREACHABLE:
                continue
            bfs_deque.append(Job(Spot(r_new, c_new), dist + 1))

    return [dists[r][c] for r, c in spots]


main()
