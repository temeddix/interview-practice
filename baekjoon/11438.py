from collections import deque
from math import ceil, floor, log2
from sys import stdin
from typing import NamedTuple


def main():
    node_count = int(input())
    equal_nodes: list[EqualNode] = [EqualNode([]) for _ in range(node_count)]
    for _ in range(node_count - 1):
        node_a, node_b = (int(s) for s in stdin.readline().split())
        node_a -= 1
        node_b -= 1
        equal_nodes[node_a][0].append(node_b)
        equal_nodes[node_b][0].append(node_a)
    node_pair_count = int(input())
    tree_nodes = build_tree(equal_nodes)
    ancestor_table = create_ancestor_table(tree_nodes)
    lca_list: list[int] = []
    for _ in range(node_pair_count):
        node_a, node_b = (int(s) for s in stdin.readline().split())
        node_a -= 1
        node_b -= 1
        node_pair = NodePair(node_a, node_b)
        lca = find_lca(tree_nodes, node_pair, ancestor_table)
        lca_list.append(lca)
    print("\n".join(str(i + 1) for i in lca_list))


ROOT_NODE = 0  # 1 in human index
INFINITY = 1_000_000_007


class NodePair(NamedTuple):
    node_a: int
    node_b: int


class EqualNode(NamedTuple):
    neighbors: list[int]


class TreeNode(NamedTuple):
    parent: int
    depth: int


class Cursor(NamedTuple):
    parent: int  # Node index
    current: int  # Node index
    depth: int


def build_tree(equal_nodes: list[EqualNode]) -> list[TreeNode]:
    optional_nodes: list[TreeNode | None] = [None] * len(equal_nodes)

    cursors = deque[Cursor]()
    cursors.append(Cursor(ROOT_NODE, ROOT_NODE, 0))

    while cursors:
        parent, current, depth = cursors.popleft()
        if optional_nodes[current] is not None:
            continue
        new_node = TreeNode(parent, depth)
        optional_nodes[current] = new_node
        for neighbor in equal_nodes[current][0]:
            cursors.append(Cursor(current, neighbor, depth + 1))

    tree_nodes = [n for n in optional_nodes if n is not None]
    return tree_nodes


def create_ancestor_table(tree_nodes: list[TreeNode]) -> list[list[int]]:
    # Adopts dynamic programming to find ancestor above "2^n" depth.
    node_count = len(tree_nodes)
    worst_case = node_count - 1
    worst_power = ceil(log2(worst_case))

    ancestor_table = [[-1] * (worst_power + 1) for _ in range(node_count)]

    for node in range(node_count):
        ancestor_table[node][0] = tree_nodes[node][0]

    for power in range(1, worst_power + 1):
        for node in range(node_count):
            mid_node = ancestor_table[node][power - 1]
            final_node = ancestor_table[mid_node][power - 1]
            ancestor_table[node][power] = final_node

    return ancestor_table


def find_lca(
    tree_nodes: list[TreeNode],
    node_pair: NodePair,
    ancestor_table: list[list[int]],
) -> int:
    # LCA stands for "lowest common ancestor".
    node_a, node_b = node_pair

    # Match the depth.
    depth_a = tree_nodes[node_a][1]
    depth_b = tree_nodes[node_b][1]
    while depth_a != depth_b:
        depth_diff = abs(depth_a - depth_b)
        depth_power = floor(log2(depth_diff))
        if depth_a > depth_b:
            node_a = ancestor_table[node_a][depth_power]
            depth_a -= 2**depth_power
        else:
            node_b = ancestor_table[node_b][depth_power]
            depth_b -= 2**depth_power

    # Just matching the depth could have made two equal.
    # if one node was an ancestor of the other.
    if node_a == node_b:
        return node_a

    # Find the ancestors of each right below the common one.
    depth_power = floor(log2(depth_a))
    while node_a != node_b:
        ancestor_a = ancestor_table[node_a][depth_power]
        ancestor_b = ancestor_table[node_b][depth_power]
        if ancestor_a == ancestor_b:
            # Should not be common.
            depth_power -= 1
            if depth_power < 0:
                break
            else:
                continue
        node_a = ancestor_a
        node_b = ancestor_b

    return tree_nodes[node_a][0]


main()
