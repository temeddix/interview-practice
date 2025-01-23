import sys
from collections import deque

START_NODE = 0

Node = list[int]  # Neighboring nodes of this node


def go_dfs(
    nodes: list[Node],
    current_node: int,
    path: list[int],
    explored: list[int] | None = None,
):
    if explored is None:
        explored = [False for _ in nodes]
    explored[current_node] = True
    path.append(current_node)

    node = nodes[current_node]
    for neighboring_node in node:
        if explored[neighboring_node]:
            continue
        go_dfs(nodes, neighboring_node, path, explored)


def go_bfs(nodes: list[Node], start_node: int, path: list[int]):
    explored = [False for _ in nodes]
    explored[start_node] = True
    cursors = deque[int]()
    cursors.append(start_node)
    path.append(start_node)

    while cursors:
        cursor = cursors.popleft()
        node = nodes[cursor]
        for neighboring_node in node:
            if explored[neighboring_node]:
                continue
            explored[neighboring_node] = True
            cursors.append(neighboring_node)
            path.append(neighboring_node)


def main():
    node_count, connection_count, start_node = (int(s) for s in input().split())
    start_node -= 1
    nodes: list[Node] = [[] for _ in range(node_count)]
    for _ in range(connection_count):
        node_a, node_b = (int(s) for s in sys.stdin.readline().split())
        node_a -= 1
        node_b -= 1
        nodes[node_a].append(node_b)
        nodes[node_b].append(node_a)
    for node in nodes:
        node.sort()
    dfs_path: list[int] = []
    bfs_path: list[int] = []
    go_bfs(nodes, start_node, bfs_path)
    go_dfs(nodes, start_node, dfs_path)
    print(" ".join(str(i + 1) for i in dfs_path))
    print(" ".join(str(i + 1) for i in bfs_path))


main()
