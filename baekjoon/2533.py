from collections import deque
from sys import stdin
from typing import NamedTuple


def main():
    node_count = int(input())
    edges: list[Edge] = []
    for _ in range(node_count - 1):
        node_a, node_b = (int(s) for s in stdin.readline().split())
        node_a -= 1
        node_b -= 1
        edges.append(Edge(node_a, node_b))
    dp_plan = build_tree(node_count, edges)
    min_influencers = get_min_influencers(dp_plan)
    print(min_influencers)


BEING_INFLUENCER = 1
BEING_NORMAL = 0


class Edge(NamedTuple):
    node_a: int
    node_b: int


class Node(NamedTuple):
    children: list[int]


class DpPlan(NamedTuple):
    nodes: list[Node]
    order: list[int]


def build_tree(node_count: int, edges: list[Edge]) -> DpPlan:
    neighbors_list: list[list[int]] = [[] for _ in range(node_count)]
    for node_a, node_b in edges:
        neighbors_list[node_a].append(node_b)
        neighbors_list[node_b].append(node_a)

    # The first node becomes the root.
    # The farthest node from the root goes last when doing DP.
    nodes: list[Node] = [Node([]) for _ in range(node_count)]
    cursors = deque[tuple[int, int]]()
    cursors.append((0, 0))
    dp_order: list[int] = [0 for _ in range(node_count)]
    index = 0
    while cursors:
        prev_node, curr_node = cursors.popleft()
        dp_order[index] = curr_node
        index += 1
        neighbors = neighbors_list[curr_node]
        for neighbor in neighbors:
            if neighbor != prev_node:
                nodes[curr_node][0].append(neighbor)
                cursors.append((curr_node, neighbor))
    dp_order.reverse()

    plan = DpPlan(nodes, dp_order)
    return plan


def get_min_influencers(plan: DpPlan) -> int:
    nodes = plan.nodes
    dp_order = plan.order

    node_count = len(nodes)

    # Use dynamic programming per extra node.
    # 0 index means non-influencer, 1 means influencer.
    memo: list[list[int]] = [[-1, -1] for _ in range(node_count)]

    for i in dp_order:
        node = nodes[i]
        children = node[0]

        if not children:
            memo[i][BEING_NORMAL] = 0
            memo[i][BEING_INFLUENCER] = 1
            continue

        children_sum = 0
        for child in children:
            children_sum += memo[child][BEING_INFLUENCER]
        memo[i][BEING_NORMAL] = children_sum

        children_sum = 0
        for child in children:
            children_sum += min(memo[child])
        memo[i][BEING_INFLUENCER] = children_sum + 1

    root = dp_order[-1]
    return min(memo[root])


main()
