from typing import NamedTuple


def main():
    map_power, _ = (int(s) for s in input().split())
    ices: list[list[int]] = []
    for _ in range(2**map_power):
        row = [int(s) for s in input().split()]
        ices.append(row)
    mix_powers = [int(s) for s in input().split()]
    block_map = BlockMap(map_power, ices)
    simulate(block_map, mix_powers)
    print(sum(sum(r) for r in block_map.ices))
    biggest_piece = find_biggest_piece(block_map)
    print(biggest_piece)


class BlockMap(NamedTuple):
    map_power: int
    ices: list[list[int]]


def simulate(block_map: BlockMap, mix_powers: list[int]):
    for mix_power in mix_powers:
        mix_ices(block_map, mix_power)
        melt_ices(block_map)


def mix_ices(block_map: BlockMap, mix_power: int):
    map_power, ices = block_map
    group_count: int = 2 ** (map_power - mix_power)
    group_size: int = 2**mix_power

    buffer = [[0] * group_size for _ in range(group_size)]

    for rg in range(group_count):
        for cg in range(group_count):
            r_base, c_base = rg * group_size, cg * group_size
            for rd in range(group_size):
                for cd in range(group_size):
                    ice = ices[r_base + rd][c_base + cd]
                    buffer[cd][group_size - 1 - rd] = ice
            for rd in range(group_size):
                for cd in range(group_size):
                    ice = buffer[rd][cd]
                    ices[r_base + rd][c_base + cd] = ice


ADJACENTS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
NEEDED_COLDNESS = 3


def melt_ices(block_map: BlockMap):
    map_power, ices = block_map
    map_size: int = 2**map_power
    does_melt = [[False] * map_size for _ in range(map_size)]

    for r in range(map_size):
        for c in range(map_size):
            if ices[r][c] == 0:
                continue
            adjacent_ices = 0
            for r_diff, c_diff in ADJACENTS:
                r_next = r + r_diff
                c_next = c + c_diff
                if 0 <= r_next < map_size and 0 <= c_next < map_size:
                    if ices[r_next][c_next]:
                        adjacent_ices += 1
            if adjacent_ices < NEEDED_COLDNESS:
                does_melt[r][c] = True

    for r in range(map_size):
        for c in range(map_size):
            if does_melt[r][c]:
                ices[r][c] -= 1


class Spot(NamedTuple):
    row: int
    column: int


def find_biggest_piece(block_map: BlockMap) -> int:
    map_power, ices = block_map
    map_size: int = 2**map_power

    visited = [[False] * map_size for _ in range(map_size)]

    biggest_piece = 0
    for r_start in range(map_size):
        for c_start in range(map_size):
            if visited[r_start][c_start]:
                continue
            if ices[r_start][c_start] == 0:
                continue
            piece = 0
            dfs_stack: list[Spot] = [Spot(r_start, c_start)]
            while dfs_stack:
                r, c = dfs_stack.pop()
                if visited[r][c]:
                    continue
                piece += 1
                visited[r][c] = True
                for r_diff, c_diff in ADJACENTS:
                    r_next, c_next = r + r_diff, c + c_diff
                    if 0 <= r_next < map_size and 0 <= c_next < map_size:
                        if ices[r_next][c_next] == 0:
                            continue
                        dfs_stack.append(Spot(r_next, c_next))
            biggest_piece = max(biggest_piece, piece)

    return biggest_piece


main()
