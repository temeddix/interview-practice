from sys import stdin

Node = tuple[
    int | None,
    int | None,
]

A_ASCII = ord("A")
ONE_BRANCH = 1
TWO_BRANCHES = 2


def do_preorder_traversal(
    nodes: list[Node],
    parent: int,
    collected: list[int] | None = None,
) -> list[int]:
    if collected is None:
        collected = []

    collected.append(parent)
    for child in nodes[parent]:
        if child is None:
            continue
        do_preorder_traversal(nodes, child, collected)

    return collected


def do_inorder_traversal(
    nodes: list[Node],
    parent: int,
    collected: list[int] | None = None,
) -> list[int]:
    if collected is None:
        collected = []

    children = nodes[parent]
    if children[0] is not None:
        do_inorder_traversal(nodes, children[0], collected)
    collected.append(parent)
    if children[1] is not None:
        do_inorder_traversal(nodes, children[1], collected)

    return collected


def do_postorder_traversal(
    nodes: list[Node],
    parent: int,
    collected: list[int] | None = None,
) -> list[int]:
    if collected is None:
        collected = []

    for child in nodes[parent]:
        if child is None:
            continue
        do_postorder_traversal(nodes, child, collected)
    collected.append(parent)

    return collected


def main():
    node_count = int(input())
    nodes: list[Node] = [(None, None) for _ in range(node_count)]
    for _ in range(node_count):
        parent, child_a, child_b = (s for s in stdin.readline().split())
        parent = ord(parent) - A_ASCII
        child_a = None if child_a == "." else ord(child_a) - A_ASCII
        child_b = None if child_b == "." else ord(child_b) - A_ASCII
        nodes[parent] = (child_a, child_b)

    result = do_preorder_traversal(nodes, 0)
    print("".join(chr(i + A_ASCII) for i in result))

    result = do_inorder_traversal(nodes, 0)
    print("".join(chr(i + A_ASCII) for i in result))

    result = do_postorder_traversal(nodes, 0)
    print("".join(chr(i + A_ASCII) for i in result))


main()
