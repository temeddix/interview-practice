import sys

Edge = tuple[
    int,  # Next node
    int,  # Weight
]

Node = list[Edge]  # Next nodes

START_NODE = 0
INFINITY = 1_000_000_000


def get_costs(nodes: list[Node]) -> list[int] | None:
    costs = [INFINITY for _ in nodes]
    costs[START_NODE] = 0
    node_count = len(nodes)

    for check_negative_loop in (False, True):
        for _ in range(node_count - 1):
            for i, node in enumerate(nodes):
                cost = costs[i]
                if cost == INFINITY:
                    continue
                for edge in node:
                    j = edge[0]
                    weight = edge[1]
                    old_cost = costs[j]
                    new_cost = cost + weight
                    if new_cost < old_cost:
                        if check_negative_loop:
                            return None
                        else:
                            costs[j] = new_cost

    return costs


def main():
    node_count, edge_count = (int(s) for s in input().split())
    nodes: list[Node] = [[] for _ in range(node_count)]
    for _ in range(edge_count):
        node_from, node_to, weight = (int(s) for s in sys.stdin.readline().split())
        node_from -= 1
        node_to -= 1
        edge: Edge = (node_to, weight)
        nodes[node_from].append(edge)
    costs = get_costs(nodes)
    if costs is None:
        print("-1")
        return
    for cost in costs[1:]:
        sys.stdout.write((str(cost) if cost != INFINITY else "-1") + "\n")


main()
