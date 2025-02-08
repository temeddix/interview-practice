from collections import deque
from typing import NamedTuple


def main():
    map_size = int(input())
    shark: Shark | None = None
    fish_map: list[list[int]] = []
    for r in range(map_size):
        row = [int(s) for s in input().split()]
        fish_row: list[int] = []
        fish_map.append(fish_row)
        for c, value in enumerate(row):
            if value != SHARK_SYMBOL:
                fish_row.append(value)
            else:
                shark = Shark(Spot(r, c), SHARK_SIZE)
                fish_row.append(0)
    if shark is None:
        raise ValueError
    seconds = count_seconds(fish_map, shark)
    print(seconds)


class Spot(NamedTuple):
    row: int
    column: int


class Shark(NamedTuple):
    spot: Spot
    size: int


SHARK_SYMBOL = 9
SHARK_SIZE = 2
INFINITY = 1_000_000_007


def count_seconds(fish_map: list[list[int]], shark: Shark) -> int:
    map_size = len(fish_map)
    distances: list[list[int]] = [[INFINITY] * map_size for _ in range(map_size)]

    fish_eaten = 0
    seconds = 0
    while True:
        food = find_closest_food(fish_map, distances, shark)
        if food is None:
            break
        spot, dist = food
        r, c = spot
        fish_map[r][c] = 0
        fish_eaten += 1
        _, size = shark
        if fish_eaten == size:
            shark = Shark(spot, size + 1)
            fish_eaten = 0
        else:
            shark = Shark(spot, size)
        seconds += dist

    return seconds


MOVEMENTS = [(-1, 0), (0, -1), (0, 1), (1, 0)]


class Job(NamedTuple):
    spot: Spot
    dist: int


class Food(NamedTuple):
    spot: Spot
    dist: int


def find_closest_food(
    fish_map: list[list[int]], distances: list[list[int]], shark: Shark
) -> Food | None:
    # Analyze basic values.
    map_size = len(fish_map)
    shark_spot, shark_size = shark

    # Reset all values.
    for r in range(map_size):
        for c in range(map_size):
            distances[r][c] = INFINITY

    # Use BFS to get the distances to fish.
    closest_spots: list[Spot] = []
    closest_dist = INFINITY
    bfs_queue = deque[Job]()
    bfs_queue.append(Job(shark_spot, 0))
    while bfs_queue:
        spot, dist = bfs_queue.popleft()
        r, c = spot
        fish_size = fish_map[r][c]
        if fish_size > shark_size:
            continue
        if 0 < fish_size < shark_size:
            if dist < closest_dist:
                closest_spots.clear()
                closest_dist = dist
            if dist == closest_dist:
                closest_spots.append(spot)
            else:
                continue
        if distances[r][c] < INFINITY:
            continue
        distances[r][c] = dist
        for r_diff, c_diff in MOVEMENTS:
            r_new, c_new = r + r_diff, c + c_diff
            if 0 <= r_new < map_size and 0 <= c_new < map_size:
                bfs_queue.append(Job(Spot(r_new, c_new), dist + 1))

    return Food(min(closest_spots), closest_dist) if closest_spots else None


main()
