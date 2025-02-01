from sys import stdin, stdout
from typing import NamedTuple


def main():
    node_count, edge_count = (int(s) for s in input().split())
    nodes = [Node([]) for _ in range(node_count)]
    for _ in range(edge_count):
        node_a, node_b = (int(s) for s in stdin.readline().split())
        node_a -= 1
        node_b -= 1
        nodes[node_a][0].append(node_b)
    node_groups = collect_scc(nodes)
    print(len(node_groups))
    for node_group in node_groups:
        stdout.write(" ".join(str(i + 1) for i in node_group[0]) + " -1\n")


class Node(NamedTuple):
    next_nodes: list[int]


class NodeGroup(NamedTuple):
    nodes: list[int]


class Job(NamedTuple):
    cleanup: bool
    node: int


def choose_start_node(grouped: list[bool]) -> int | None:
    for node, value in enumerate(grouped):
        if not value:
            return node
    return None


def collect_scc(nodes: list[Node]) -> list[NodeGroup]:
    # SCC stands for "strongly connected components".
    node_count = len(nodes)
    parent_nodes: list[int] = [i for i in range(node_count)]
    grouped = [False for _ in range(node_count)]

    # Collect SCC groups.
    while True:
        # This works like a recursive function call.
        dfs_jobs: list[Job] = []

        # Remember where in which order were visited.
        visited = [False for _ in nodes]
        node_stack: list[int] = []

        # Choose the first node that hasn't been visited yet.
        start_node = choose_start_node(grouped)
        if start_node is None:
            break

        dfs_jobs.append(Job(True, start_node))
        dfs_jobs.append(Job(False, start_node))

        while dfs_jobs:
            cleanup, node = dfs_jobs.pop()
            if cleanup:
                # This simulates the cleanup process
                # after typical recursion function call.
                visited[node] = False
                node_stack.pop()
                continue
            # Remember that we visited this node.
            visited_before = visited[node]
            visited[node] = True
            node_stack.append(node)
            # If we've visited this node before,
            # we've found a cycle.
            if visited_before:
                for i, footprint in enumerate(reversed(node_stack)):
                    if i == 0:
                        continue
                    grouped[footprint] = True
                    parent_nodes[footprint] = node
                    if footprint == node:
                        break
                continue
            # Prepare to visit next nodes.
            for next_node in nodes[node][0]:
                dfs_jobs.append(Job(True, next_node))
                dfs_jobs.append(Job(False, next_node))

        # Always mark the start node as grouped.
        grouped[start_node] = True

    node_groups = convert_to_groups(parent_nodes)
    return node_groups


def get_root_node(parent_nodes: list[int], node: int) -> int:
    current = node

    trail = [current]
    while True:
        parent = parent_nodes[current]
        if parent == current:
            break
        current = parent
        trail.append(current)
    root = current

    for footprint in trail:
        parent_nodes[footprint] = root

    return root


def convert_to_groups(parent_nodes: list[int]) -> list[NodeGroup]:
    node_count = len(parent_nodes)

    groups: dict[int, NodeGroup] = {}
    for node in range(node_count):
        root_node = get_root_node(parent_nodes, node)
        group = groups.get(root_node)
        if group is None:
            group = NodeGroup([])
            groups[root_node] = group
        group[0].append(node)

    list_groups = list(groups.values())
    list_groups.sort(key=lambda g: g[0][0])
    for group in list_groups[0]:
        group.sort()
    return list_groups


main()
