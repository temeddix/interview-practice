from collections import deque
from sys import stdin

Edge = tuple[
    int,  # Next node
    int,  # Distance
]
Node = list[Edge]  # Connecting edges
NodeInfo = tuple[
    int,  # Distance from the start
    int,  # Node number
]

NULL_NODE = -1
INFINITY = 1_000_000_007


def find_farthest_node(nodes: list[Node], start_index: int) -> NodeInfo:
    node_dists = [INFINITY for _ in nodes]
    farthest_node: NodeInfo = (0, NULL_NODE)

    cursors = deque[NodeInfo]()
    cursors.append((0, start_index))
    while cursors:
        dist, index = cursors.popleft()
        if not dist < node_dists[index]:
            continue
        node_dists[index] = dist
        farthest_node = max(farthest_node, (dist, index))
        for neighbor, weight in nodes[index]:
            cursors.append((dist + weight, neighbor))

    return farthest_node


def calculate_diameter(nodes: list[Node]) -> int:
    _, one_point = find_farthest_node(nodes, 0)
    diameter, _ = find_farthest_node(nodes, one_point)
    return diameter


def main():
    node_count = int(input())
    nodes: list[Node] = [[] for _ in range(node_count)]
    for _ in range(node_count):
        inputs = [int(s) for s in stdin.readline().split()]
        inputs.reverse()
        node_a = inputs.pop()
        node_a -= 1
        while inputs:
            node_b = inputs.pop()
            if node_b == -1:
                break
            node_b -= 1
            weight = inputs.pop()
            nodes[node_a].append((node_b, weight))
            nodes[node_b].append((node_a, weight))
    diameter = calculate_diameter(nodes)
    print(diameter)


main()
