from sys import stdin, stdout

Node = list[int]  # Neighboring nodes


def do_dfs(
    nodes: list[Node],
    start_node: int,
    visitied: list[bool],
) -> bool:
    edge_count = 0
    node_count = 1
    stack: list[int] = []
    stack.append(start_node)
    visitied[start_node] = True

    while stack:
        current = stack.pop()
        for neighbor in nodes[current]:
            edge_count += 1
            if not visitied[neighbor]:
                visitied[neighbor] = True
                node_count += 1
                stack.append(neighbor)

    is_tree = node_count - 1 == edge_count // 2
    return is_tree


def count_trees(nodes: list[Node]) -> int:
    visited = [False for _ in nodes]

    trees = 0
    for i in range(len(nodes)):
        if visited[i]:
            continue
        is_tree = do_dfs(nodes, i, visited)
        if is_tree:
            trees += 1

    return trees


def main():
    case_number = 0
    while True:
        case_number += 1
        node_count, edge_count = (int(s) for s in stdin.readline().split())
        if node_count == 0 and edge_count == 0:
            break
        nodes: list[Node] = [[] for _ in range(node_count)]
        for _ in range(edge_count):
            node_a, node_b = (int(s) for s in stdin.readline().split())
            node_a -= 1
            node_b -= 1
            nodes[node_a].append(node_b)
            nodes[node_b].append(node_a)
        trees = count_trees(nodes)
        if trees == 0:
            text = "No trees."
        elif trees == 1:
            text = "There is one tree."
        else:
            text = f"A forest of {trees} trees."
        stdout.write(f"Case {case_number}: {text}\n")


main()
