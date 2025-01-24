import sys
from collections import deque

Node = list[int]  # Neighboring nodes


UP = 1
UNEXPLORED = 0
DOWN = -1


def determine_bipartite(nodes: list[Node]) -> bool:
    unexplored_nodes = set(range(len(nodes)))
    result = [UNEXPLORED for _ in nodes]
    cursors = deque[int]()

    while unexplored_nodes:
        start_node = unexplored_nodes.pop()
        result[start_node] = UP
        cursors.append(start_node)
        while cursors:
            current = cursors.popleft()
            value = result[current]
            for neighbor in nodes[current]:
                if result[neighbor] == value:
                    return False
                new_value = value * -1
                if result[neighbor] == new_value:
                    continue
                unexplored_nodes.remove(neighbor)
                result[neighbor] = new_value
                cursors.append(neighbor)

    return True


def main():
    test_cases = int(input())
    for _ in range(test_cases):
        node_count, edge_count = (int(s) for s in input().split())
        nodes: list[Node] = [[] for _ in range(node_count)]
        for _ in range(edge_count):
            node_a, node_b = (int(s) for s in sys.stdin.readline().split())
            node_a -= 1
            node_b -= 1
            nodes[node_a].append(node_b)
            nodes[node_b].append(node_a)
        is_bipartite = determine_bipartite(nodes)
        print("YES" if is_bipartite else "NO")


main()
