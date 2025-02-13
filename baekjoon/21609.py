from typing import NamedTuple


def main():
    map_size, _ = (int(s) for s in input().split())
    blocks: list[list[int]] = []
    for _ in range(map_size):
        row = [int(s) for s in input().split()]
        blocks.append(row)
    score = play(map_size, blocks)
    print(score)


class Spot(NamedTuple):
    row: int
    column: int


class BlockGroup(NamedTuple):
    size: int
    rainbow_count: int
    base_spot: Spot
    spots: list[Spot]


EMPTY = -2
BLACK_COLOR = -1
RAINBOW_COLOR = 0


def play(map_size: int, blocks: list[list[int]]) -> int:
    score = 0

    while True:
        groups = group_blocks(map_size, blocks)
        if not groups:
            break
        chosen_group = max(groups)
        spots_to_remove = chosen_group.spots
        for r, c in spots_to_remove:
            blocks[r][c] = EMPTY
        blocks = apply_gravity(map_size, blocks)
        score += len(spots_to_remove) ** 2
        blocks = rotate_ccw(map_size, blocks)
        blocks = apply_gravity(map_size, blocks)

    return score


ADJACENTS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def group_blocks(map_size: int, blocks: list[list[int]]) -> list[BlockGroup]:
    block_groups: list[BlockGroup] = []
    normal_visited = [[False] * map_size for _ in range(map_size)]
    rainbow_visited = [[False] * map_size for _ in range(map_size)]

    for r_start in range(map_size):
        for c_start in range(map_size):
            # Get the start spot and group color.
            if normal_visited[r_start][c_start]:
                continue
            group_color = blocks[r_start][c_start]
            if group_color in (EMPTY, BLACK_COLOR, RAINBOW_COLOR):
                continue

            # Clear rainbow visited lists.
            clear_visited(map_size, rainbow_visited)

            # Collect group block spots.
            rainbow_collected: list[Spot] = []
            normal_collected: list[Spot] = []
            dfs_stack: list[Spot] = [Spot(r_start, c_start)]
            while dfs_stack:
                # Pop the current cursor from the stack.
                r, c = dfs_stack.pop()
                color = blocks[r][c]

                # Skip this spot if not collectable.
                if color in (EMPTY, BLACK_COLOR):
                    continue

                # Check the block and collect it if it belongs to the group.
                if color == RAINBOW_COLOR:
                    if rainbow_visited[r][c]:
                        continue
                    rainbow_collected.append(Spot(r, c))
                    rainbow_visited[r][c] = True
                else:
                    if color != group_color or normal_visited[r][c]:
                        continue
                    normal_collected.append(Spot(r, c))
                    normal_visited[r][c] = True

                # Continue DFS.
                for r_diff, c_diff in ADJACENTS:
                    r_next, c_next = r + r_diff, c + c_diff
                    if 0 <= r_next < map_size and 0 <= c_next < map_size:
                        dfs_stack.append(Spot(r_next, c_next))

            # Remember the group.
            all_collected = rainbow_collected + normal_collected
            group_size = len(all_collected)
            base_spot = min(s for s in normal_collected)
            block_group = BlockGroup(
                group_size,
                len(rainbow_collected),
                base_spot,
                all_collected,
            )
            block_groups.append(block_group)

    return [g for g in block_groups if g.size > 1]


def clear_visited(map_size: int, visited: list[list[bool]]):
    for r in range(map_size):
        for c in range(map_size):
            visited[r][c] = False


def rotate_ccw(map_size: int, blocks: list[list[int]]) -> list[list[int]]:
    buffer = [[EMPTY] * map_size for _ in range(map_size)]

    for r in range(map_size):
        for c in range(map_size):
            buffer[map_size - 1 - c][r] = blocks[r][c]

    return buffer


def rotate_cw(map_size: int, blocks: list[list[int]]) -> list[list[int]]:
    buffer = [[EMPTY] * map_size for _ in range(map_size)]

    for r in range(map_size):
        for c in range(map_size):
            buffer[c][map_size - 1 - r] = blocks[r][c]

    return buffer


def apply_gravity(map_size: int, blocks: list[list[int]]) -> list[list[int]]:
    buffer = rotate_cw(map_size, blocks)

    for row in buffer:
        find_pointer = 1
        drop_pointer = 0
        while True:
            while drop_pointer < map_size and row[drop_pointer] != EMPTY:
                drop_pointer += 1
                find_pointer = max(find_pointer, drop_pointer + 1)
            if find_pointer >= map_size:
                break
            found_color = row[find_pointer]
            if found_color == EMPTY:
                find_pointer += 1
            elif found_color == BLACK_COLOR:
                drop_pointer = find_pointer
            else:
                row[drop_pointer] = found_color
                row[find_pointer] = EMPTY

    return rotate_ccw(map_size, buffer)


main()
