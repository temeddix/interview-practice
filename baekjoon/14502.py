from collections import deque
from itertools import combinations
from typing import NamedTuple


def main():
    map_height, map_width = (int(s) for s in input().split())
    map_size = MapSize(map_height, map_width)
    row_strings: list[str] = []
    for _ in range(map_height):
        row_strings.append(input())
    graph = construct_nodes(row_strings, map_size)
    max_safe_area = find_max_safe_area(graph, map_size)
    print(max_safe_area)


class MapSize(NamedTuple):
    height: int
    width: int


class Spot(NamedTuple):
    row: int
    column: int


class Node(NamedTuple):
    neighbors: list[Spot]


class Graph(NamedTuple):
    nodes: list[list[Node | None]]
    roots: list[Spot]
    empty: list[Spot]


WALL_COUNT = 3
EMPTY_SPOT = 0
START_SPOT = 2
MOVEMENT = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def construct_nodes(row_strings: list[str], map_size: MapSize) -> Graph:
    # Get the map info.
    map_height, map_width = map_size

    # Store the nodes. None means wall.
    nodes: list[list[Node | None]] = [[None] * map_width for _ in range(map_height)]

    # Where initial viruses are.
    roots: list[Spot] = []
    empty: list[Spot] = []

    # Prepare empty nodes.
    for row, row_string in enumerate(row_strings):
        for column, letter in enumerate(int(s) for s in row_string.split()):
            if letter == EMPTY_SPOT:
                nodes[row][column] = Node([])
                empty.append(Spot(row, column))
            elif letter == START_SPOT:
                nodes[row][column] = Node([])
                roots.append(Spot(row, column))

    # Use BFS to construct the graph.
    bfs_queue = deque[Spot]()
    for start_spot in roots:
        bfs_queue.append(start_spot)

    while bfs_queue:
        current_spot = bfs_queue.popleft()
        current_row, current_column = current_spot
        current_node = nodes[current_row][current_column]
        if current_node is None:
            raise ValueError

        for movement_v, movement_h in MOVEMENT:
            next_row = current_spot.row + movement_v
            next_column = current_spot.column + movement_h
            is_row_inside = 0 <= next_row < map_height
            is_column_inside = 0 <= next_column < map_width

            if not is_row_inside or not is_column_inside:
                continue
            next_node = nodes[next_row][next_column]
            if next_node is None:
                continue
            next_spot = Spot(next_row, next_column)
            if next_spot in current_node.neighbors:
                continue

            current_node.neighbors.append(next_spot)
            next_node.neighbors.append(current_spot)
            bfs_queue.append(next_spot)

    return Graph(nodes, roots, empty)


def find_max_safe_area(graph: Graph, map_size: MapSize) -> int:
    map_height, map_width = map_size
    nodes, roots, empty = graph

    visited = [[False] * map_width for _ in range(map_height)]

    max_safe_area = 0
    for new_walls in combinations(empty, WALL_COUNT):
        # Prepare the inititial state.
        unaffected_area = len(empty) - WALL_COUNT
        for row in range(map_height):
            for column in range(map_width):
                visited[row][column] = False
        for barrier in list(new_walls) + roots:
            row, column = barrier
            visited[row][column] = True

        # Prepare the BFS queue.
        bfs_queue = deque[Spot]()
        for root in roots:
            bfs_queue.append(root)

        # Search with BFS.
        while bfs_queue:
            current_spot = bfs_queue.popleft()
            current_row, current_column = current_spot
            current_node = nodes[current_row][current_column]
            if current_node is None:
                raise ValueError

            for neighbor_spot in current_node.neighbors:
                neighbor_row, neighbor_column = neighbor_spot
                if not visited[neighbor_row][neighbor_column]:
                    visited[neighbor_row][neighbor_column] = True
                    unaffected_area -= 1
                    bfs_queue.append(neighbor_spot)

        max_safe_area = max(max_safe_area, unaffected_area)

    return max_safe_area


main()
