import sys

Edge = tuple[
    int,  # Next node
    int,  # Weight
]

Node = list[Edge]

INFINITY = 2_000_000_000


def get_cost_table(nodes: list[Node]) -> list[list[int]]:
    node_count = len(nodes)
    cost_table = [[INFINITY for _ in range(node_count)] for _ in range(node_count)]

    # Fill initial values.
    for i, node in enumerate(nodes):
        cost_table[i][i] = 0
        for edge in node:
            j, weight = edge
            old_cost = cost_table[i][j]
            if weight < old_cost:
                cost_table[i][j] = weight

    # Repeat by mid stop nodes.
    for k in range(node_count):  # Mid node
        for i in range(node_count):  # From node
            for j in range(node_count):  # To node
                old_cost = cost_table[i][j]
                new_cost = cost_table[i][k] + cost_table[k][j]
                if new_cost < old_cost:
                    cost_table[i][j] = new_cost

    return cost_table


def main():
    node_count = int(input())
    edge_count = int(input())
    nodes: list[Node] = [[] for _ in range(node_count)]
    for _ in range(edge_count):
        node_from, node_to, weight = (int(s) for s in sys.stdin.readline().split())
        node_from -= 1
        node_to -= 1
        nodes[node_from].append((node_to, weight))
    cost_table = get_cost_table(nodes)
    for row in cost_table:
        sys.stdout.write(" ".join(str(i) if i != INFINITY else "0" for i in row))
        sys.stdout.write("\n")


main()
