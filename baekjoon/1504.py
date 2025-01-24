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

INFINITE = 1_000_000_000


def get_cost(nodes: list[Node], start_node: int, end_nodes: list[int]) -> list[int]:
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

    return [costs[i] for i in end_nodes]


def get_combined_cost(nodes: list[Node], stop_a: int, stop_b: int):
    last = len(nodes) - 1
    to_a, to_b = get_cost(nodes, 0, [stop_a, stop_b])
    from_a, from_b = get_cost(nodes, last, [stop_a, stop_b])
    between_a_b = get_cost(nodes, stop_a, [stop_b])[0]

    result = min(to_a + between_a_b + from_b, to_b + between_a_b + from_a)
    return -1 if INFINITE <= result else result


def main():
    node_count, edge_count = (int(s) for s in input().split())
    nodes: list[Node] = [[] for _ in range(node_count)]
    for _ in range(edge_count):
        node_a, node_b, weight = (int(s) for s in sys.stdin.readline().split())
        node_a -= 1
        node_b -= 1
        nodes[node_a].append((node_b, weight))
        nodes[node_b].append((node_a, weight))
    stop_a, stop_b = (int(s) for s in input().split())
    stop_a -= 1
    stop_b -= 1
    cost = get_combined_cost(nodes, stop_a, stop_b)
    print(cost)


main()
