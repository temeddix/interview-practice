from sys import stdin

MAX_NODES = 1_000_000

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
    IndexRange,  # For original preorder list
]
SplittedTree = tuple[
    int | None,
    RangeExpression,
    RangeExpression,
]


def do_postorder_traversal(
    nodes: list[Node],
    root: int,
) -> list[int]:
    collected: list[int] = []
    stack: list[int] = [root]

    while stack:
        parent = stack.pop()
        for child in nodes[parent]:
            if child is not None:
                stack.append(child)
        collected.append(parent)

    collected.reverse()
    return collected


def split_tree(
    original: OriginalData,
    expression: RangeExpression,
) -> SplittedTree:
    inorder_list = original[0]
    preorder_list = original[1]

    inorder_range = expression[0]
    preorder_range = expression[1]

    if inorder_range[1] == inorder_range[0]:
        inorder_start = inorder_range[0]
        preorder_start = preorder_range[0]
        return (
            None,
            (
                (inorder_start, inorder_start),
                (preorder_start, preorder_start),
            ),
            (
                (inorder_start, inorder_start),
                (preorder_start, preorder_start),
            ),
        )

    parent = preorder_list[preorder_range[0]]
    inorder_parent_index = inorder_range[0]
    while inorder_list[inorder_parent_index] != parent:
        inorder_parent_index += 1

    left_inorder = (inorder_range[0], inorder_parent_index)
    right_inorder = (inorder_parent_index + 1, inorder_range[1])
    left_size = left_inorder[1] - left_inorder[0]

    preorder_start = preorder_range[0]
    left_preorder = (preorder_start + 1, preorder_start + left_size + 1)
    right_preorder = (preorder_start + left_size + 1, preorder_range[1])

    return (
        parent,
        (left_inorder, left_preorder),
        (right_inorder, right_preorder),
    )


def build_tree(original: OriginalData) -> tuple[list[Node], int]:
    nodes: list[Node] = [(None, None) for _ in range(MAX_NODES)]

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
    preorder_list: list[int] = []
    lines = stdin.read().splitlines()
    for line in lines:
        number = int(line)
        preorder_list.append(number)
    inorder_list = sorted(preorder_list)

    original: OriginalData = (inorder_list, preorder_list)
    tree, root = build_tree(original)
    postorder_list = do_postorder_traversal(tree, root)
    print(" ".join(str(i) for i in postorder_list))


main()
