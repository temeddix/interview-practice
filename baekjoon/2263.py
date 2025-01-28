from collections import deque

Node = tuple[
    int | None,  # Left child
    int | None,  # Right child
]
TreeExpression = tuple[
    list[int],  # Sorted by inorder traversal
    list[int],  # Sorted by postorder traversal
]
SplittedTree = tuple[
    int | None,
    TreeExpression,
    TreeExpression,
]


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


def split_tree(expression: TreeExpression) -> SplittedTree:
    inorder_list = expression[0]
    postorder_list = expression[1]

    if not postorder_list:
        return (None, ([], []), ([], []))

    parent = postorder_list[-1]
    parent_index = inorder_list.index(parent)

    left_inorder = inorder_list[:parent_index]
    right_inorder = inorder_list[parent_index + 1 :]

    left_postorder = postorder_list[:parent_index]
    right_postorder = postorder_list[parent_index:-1]

    return (
        parent,
        (left_inorder, left_postorder),
        (right_inorder, right_postorder),
    )


def build_tree(node_count: int, expression: TreeExpression) -> tuple[list[Node], int]:
    nodes: list[Node] = [(None, None) for _ in range(node_count)]

    whole_splitted = split_tree(expression)
    root, _, _ = whole_splitted
    if root is None:
        raise ValueError

    jobs = deque[SplittedTree]()
    jobs.append(whole_splitted)
    while jobs:
        parent, left_expression, right_expression = jobs.popleft()
        if parent is None:
            continue
        left_splitted = split_tree(left_expression)
        left_parent, _, _ = left_splitted
        right_splitted = split_tree(right_expression)
        right_parent, _, _ = right_splitted
        nodes[parent] = (left_parent, right_parent)
        jobs.append(left_splitted)
        jobs.append(right_splitted)

    return nodes, root


def main():
    node_count = int(input())
    inorder_list = [int(s) - 1 for s in input().split()]
    postorder_list = [int(s) - 1 for s in input().split()]

    expression: TreeExpression = (inorder_list, postorder_list)
    tree, root = build_tree(node_count, expression)
    preorder_list = do_preorder_traversal(tree, root)
    print(" ".join(str(i + 1) for i in preorder_list))


main()
