import sys
from queue import PriorityQueue

Edge = tuple[
    int,  # Next node
    int,  # Weight
]

Node = list[Edge]

Cost = tuple[
    int,  # Cost
    int,  # Destination node
]

INFINITE = 1_000_000


def get_costs(nodes: list[Node], start_node: int) -> list[int]:
    costs = [INFINITE for _ in nodes]
    p_queue = PriorityQueue[Cost]()

    costs[start_node] = 0
    p_queue.put((0, start_node))

    while not p_queue.empty():
        current_cost, current_node = p_queue.get()
        if costs[current_node] < current_cost:
            continue
        for next_node, weight in nodes[current_node]:
            old_cost = costs[next_node]
            new_cost = current_cost + weight
            if new_cost < old_cost:
                costs[next_node] = new_cost
                p_queue.put((new_cost, next_node))

    return costs


def main():
    node_count, edge_count = (int(s) for s in input().split())
    start_node = int(input()) - 1
    nodes: list[Node] = [[] for _ in range(node_count)]
    for _ in range(edge_count):
        from_node, to_node, weight = (int(s) for s in sys.stdin.readline().split())
        from_node -= 1
        to_node -= 1
        edge: Edge = (to_node, weight)
        nodes[from_node].append(edge)
    costs = get_costs(nodes, start_node)
    for cost in costs:
        sys.stdout.write((str(cost) if cost != INFINITE else "INF") + "\n")


main()
