from sys import setrecursionlimit, stdin, stdout
from typing import NamedTuple


def main():
    setrecursionlimit(RECURSION_LIMIT)
    node_count, edge_count = (int(s) for s in input().split())
    nodes = [Node([]) for _ in range(node_count)]
    for _ in range(edge_count):
        node_a, node_b = (int(s) for s in stdin.readline().split())
        node_a -= 1
        node_b -= 1
        nodes[node_a][0].append(node_b)
    node_groups = collect_scc_groups(nodes)
    print(len(node_groups))
    for node_group in node_groups:
        stdout.write(" ".join(str(i + 1) for i in node_group) + " -1\n")


RECURSION_LIMIT = 10**5
UNVISITED = -1


class Node(NamedTuple):
    next_nodes: list[int]


class Job(NamedTuple):
    cleanup: bool
    node: int


class State(NamedTuple):
    nodes: list[Node]
    scc_groups: list[list[int]]
    stack: list[int]
    on_stack: list[bool]
    discoveries: list[int]
    discovery_counter: list[int]  # Single-sized cell.


def collect_scc_groups(nodes: list[Node]) -> list[list[int]]:
    node_count = len(nodes)
    discoveries = [UNVISITED for _ in range(node_count)]

    state = State(
        nodes=nodes,
        stack=[],
        on_stack=[False for _ in range(node_count)],
        discoveries=discoveries,
        scc_groups=[],
        discovery_counter=[0],
    )

    for start in range(node_count):
        if discoveries[start] == UNVISITED:
            search_next(start, state)

    sort_scc_groups(state.scc_groups)
    return state.scc_groups


def search_next(curr: int, state: State) -> int:
    # Uses DFS and Tarjan algorithm.
    nodes, scc_groups, stack, on_stack, discoveries, discovery_counter = state

    discovery = discovery_counter[0]
    discoveries[curr] = discovery
    discovery_counter[0] += 1
    stack.append(curr)
    on_stack[curr] = True

    parent = discoveries[curr]
    for next in nodes[curr][0]:
        if discoveries[next] == UNVISITED:
            parent = min(parent, search_next(next, state))
        elif on_stack[next]:
            # Visiting, but not processed yet.
            parent = min(parent, discoveries[next])

    if parent == discoveries[curr]:
        # Parent is the same as self.
        scc_group: list[int] = []
        while True:
            node = stack.pop()
            on_stack[node] = False
            scc_group.append(node)
            if curr == node:
                break
        scc_groups.append(scc_group)

    return parent


def sort_scc_groups(scc_groups: list[list[int]]):
    for scc_group in scc_groups:
        scc_group.sort()
    scc_groups.sort(key=lambda g: g[0])


main()
