from collections import deque
from itertools import combinations
from typing import NamedTuple

MIN_BRIDGE_LEN = 2
INFINITY_LEN = 1_000_000_007


class Edge(NamedTuple):
    weight: int
    node_a: int
    node_b: int


class Node(NamedTuple):
    parent: int


class Graph(NamedTuple):
    nodes: list[Node]
    edges: list[Edge]


class Block(NamedTuple):
    x: int
    y: int


class Island(NamedTuple):
    blocks: list[Block]


def find_root(nodes: list[Node], node_index: int) -> int:
    trail: list[int] = []

    current = node_index
    while nodes[current][0] != current:
        trail.append(current)
        (current,) = nodes[current]
    root = current

    for each in trail:
        nodes[each] = Node(root)

    return root


def union_nodes(nodes: list[Node], edge: Edge):
    _, node_a, node_b = edge
    root_a = find_root(nodes, node_a)
    root_b = find_root(nodes, node_b)
    # Choose the node with smaller index as root.
    if root_a < root_b:
        nodes[root_b] = Node(root_a)
    elif root_b < root_a:
        nodes[root_a] = Node(root_b)


def get_weight_sum(graph: Graph) -> int | None:
    nodes = graph.nodes
    edges = graph.edges

    node_count = len(nodes)
    target_edges = node_count - 1

    used_edges = 0
    weight_sum = 0
    for edge in sorted(edges):
        weight, node_a, node_b = edge
        root_a = find_root(nodes, node_a)
        root_b = find_root(nodes, node_b)
        if root_a == root_b:
            continue
        weight_sum += weight
        used_edges += 1
        union_nodes(nodes, edge)
        if used_edges == target_edges:
            break

    return weight_sum if used_edges == target_edges else None


def extract_block(map: list[list[bool]]) -> Block | None:
    for i, row in enumerate(map):
        for j, value in enumerate(row):
            if value:
                return Block(i, j)
    return None


def extract_island(map: list[list[bool]]) -> Island | None:
    height = len(map)
    width = len(map[0])

    first_block = extract_block(map)
    if first_block is None:
        return None
    cursors = deque[Block]()
    cursors.append(first_block)

    blocks: list[Block] = []
    while cursors:
        row, col = cursors.popleft()
        if not map[row][col]:
            continue
        blocks.append(Block(row, col))
        map[row][col] = False
        for shift in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            new_row = row + shift[0]
            new_col = col + shift[1]
            if not 0 <= new_row < height:
                continue
            if not 0 <= new_col < width:
                continue
            cursors.append(Block(new_row, new_col))

    return Island(blocks)


def extract_islands(map: list[list[bool]]) -> list[Island]:
    islands: list[Island] = []

    while True:
        island = extract_island(map)
        if island is None:
            break
        islands.append(island)

    return islands


def does_overlap(blocks_a: list[Block], blocks_b: list[Block]) -> bool:
    for block_a in blocks_a:
        for block_b in blocks_b:
            if block_a == block_b:
                return True
    return False


def abstract_islands(islands: list[Island]) -> Graph:
    all_blocks: list[Block] = []
    for island in islands:
        all_blocks.extend(island.blocks)

    island_count = len(islands)
    nodes: list[Node] = [Node(i) for i in range(island_count)]
    edges: list[Edge] = []

    pairs = combinations(enumerate(islands), 2)
    for (a_index, island_a), (b_index, island_b) in pairs:
        # The shorter the better, but should be at least 2
        bridge_len = INFINITY_LEN
        for block_a in island_a.blocks:
            for block_b in island_b.blocks:
                if block_a[0] == block_b[0]:
                    # Same row
                    start = min(block_a[1], block_b[1])
                    end = max(block_a[1], block_b[1])
                    if end - start < MIN_BRIDGE_LEN + 1:
                        continue
                    row = block_a[0]
                    bridge_blocks = [Block(row, i) for i in range(start + 1, end)]
                elif block_a[1] == block_b[1]:
                    # Same column
                    start = min(block_a[0], block_b[0])
                    end = max(block_a[0], block_b[0])
                    if end - start < MIN_BRIDGE_LEN + 1:
                        continue
                    col = block_a[1]
                    bridge_blocks = [Block(i, col) for i in range(start + 1, end)]
                else:
                    continue
                is_bridge_usable = not does_overlap(bridge_blocks, all_blocks)
                if is_bridge_usable:
                    bridge_len = min(bridge_len, len(bridge_blocks))
        if bridge_len != INFINITY_LEN:
            edge = Edge(bridge_len, a_index, b_index)
            edges.append(edge)

    graph = Graph(nodes, edges)
    return graph


def main():
    map_height, _ = (int(s) for s in input().split())
    map: list[list[bool]] = []
    for _ in range(map_height):
        row = [True if s == "1" else False for s in input().split()]
        map.append(row)
    islands = extract_islands(map)
    graph = abstract_islands(islands)
    weight_sum = get_weight_sum(graph)
    print(-1 if weight_sum is None else weight_sum)


main()
