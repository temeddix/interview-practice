Node = tuple[
    int | None,  # Left child
    int | None,  # Right child
]
IndexRange = tuple[
    int,  # Start, inclusive
    int,  # End, exclusive
]
OriginalData = tuple[
    list[int],
    list[int],
]
RangeExpression = tuple[
    IndexRange,  # For original inorder list
    IndexRange,  # For original postorder list
]
SplittedTree = tuple[
    int | None,
    RangeExpression,
    RangeExpression,
]


def do_preorder_traversal(
    nodes: list[Node],
    root: int,
) -> list[int]:
    collected: list[int] = []
    stack: list[int] = [root]

    while stack:
        parent = stack.pop()
        collected.append(parent)
        for child in reversed(nodes[parent]):
            if child is not None:
                stack.append(child)

    return collected


def split_tree(
    original: OriginalData,
    expression: RangeExpression,
) -> SplittedTree:
    inorder_list = original[0]
    postorder_list = original[1]

    inorder_range = expression[0]
    postorder_range = expression[1]

    if inorder_range[1] == inorder_range[0]:
        inorder_start = inorder_range[0]
        postorder_start = postorder_range[0]
        return (
            None,
            (
                (inorder_start, inorder_start),
                (postorder_start, postorder_start),
            ),
            (
                (inorder_start, inorder_start),
                (postorder_start, postorder_start),
            ),
        )

    parent = postorder_list[postorder_range[1] - 1]
    inorder_parent_index = inorder_range[0]
    while inorder_list[inorder_parent_index] != parent:
        inorder_parent_index += 1

    left_inorder = (inorder_range[0], inorder_parent_index)
    right_inorder = (inorder_parent_index + 1, inorder_range[1])
    left_size = left_inorder[1] - left_inorder[0]

    postorder_start = postorder_range[0]
    left_postorder = (postorder_start, postorder_start + left_size)
    right_postorder = (postorder_start + left_size, postorder_range[1] - 1)

    return (
        parent,
        (left_inorder, left_postorder),
        (right_inorder, right_postorder),
    )


def build_tree(node_count: int, original: OriginalData) -> tuple[list[Node], int]:
    nodes: list[Node] = [(None, None) for _ in range(node_count)]

    tree_size = len(original[0])
    start_expression: RangeExpression = (
        (0, tree_size),
        (0, tree_size),
    )

    whole_splitted = split_tree(original, start_expression)
    root, _, _ = whole_splitted
    if root is None:
        raise ValueError

    jobs: list[SplittedTree] = []
    jobs.append(whole_splitted)
    while jobs:
        parent, left_expression, right_expression = jobs.pop()
        if parent is None:
            continue
        left_splitted = split_tree(original, left_expression)
        left_parent, _, _ = left_splitted
        right_splitted = split_tree(original, right_expression)
        right_parent, _, _ = right_splitted
        nodes[parent] = (left_parent, right_parent)
        jobs.append(left_splitted)
        jobs.append(right_splitted)

    return nodes, root


def main():
    node_count = int(input())
    inorder_list = [int(s) - 1 for s in input().split()]
    postorder_list = [int(s) - 1 for s in input().split()]

    original: OriginalData = (inorder_list, postorder_list)
    tree, root = build_tree(node_count, original)
    preorder_list = do_preorder_traversal(tree, root)
    print(" ".join(str(i + 1) for i in preorder_list))


main()
