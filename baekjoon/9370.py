import sys
from queue import PriorityQueue

Edge = tuple[
    int,  # Cost
    int,  # Neighboring node
]

Node = list[Edge]

Cost = tuple[
    int,  # cost
    int,  # Destination node
    int,  # Whether has passed the road with the smell
]


INFINITE = 1_000_000_000


def filter_goals(
    nodes: list[Node],
    start_node: int,
    goals: list[int],
    stop: tuple[int, int],
) -> list[int]:
    costs = [[INFINITE, INFINITE] for _ in nodes]
    p_queue = PriorityQueue[Cost]()

    costs[start_node][0] = 0
    p_queue.put((0, start_node, 0))

    while not p_queue.empty():
        current_cost, current_node, current_use = p_queue.get()
        if costs[current_node][current_use] < current_cost:
            continue
        for weight, neighbor in nodes[current_node]:
            if stop in ((current_node, neighbor), (neighbor, current_node)):
                new_use = 1
            else:
                new_use = current_use
            old_cost = costs[neighbor][new_use]
            new_cost = current_cost + weight
            if new_cost < old_cost:
                costs[neighbor][new_use] = new_cost
                p_queue.put((new_cost, neighbor, new_use))

    filtered_goals: list[int] = []
    for goal in goals:
        cost_without_using = costs[goal][0]
        cost_while_using = costs[goal][1]
        if cost_while_using == INFINITE:
            continue
        if cost_while_using <= cost_without_using:
            filtered_goals.append(goal)
    filtered_goals.sort()

    return filtered_goals


def main():
    test_cases = int(input())
    for _ in range(test_cases):
        node_count, edge_count, goal_count = (int(s) for s in input().split())
        start_node, stop_a, stop_b = (int(s) for s in input().split())
        start_node -= 1
        stop_a -= 1
        stop_b -= 1
        stop = (stop_a, stop_b)
        nodes: list[Node] = [[] for _ in range(node_count)]
        for _ in range(edge_count):
            node_a, node_b, weight = (int(s) for s in sys.stdin.readline().split())
            node_a -= 1
            node_b -= 1
            nodes[node_a].append((weight, node_b))
            nodes[node_b].append((weight, node_a))
        goals: list[int] = []
        for _ in range(goal_count):
            goal = int(sys.stdin.readline().strip())
            goal -= 1
            goals.append(goal)
        filtered_goals = filter_goals(nodes, start_node, goals, stop)
        print(" ".join(str(i + 1) for i in filtered_goals))


main()
