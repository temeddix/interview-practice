from typing import NamedTuple


def main():
    map_size, command_count = (int(s) for s in input().split())
    waters: list[list[int]] = []
    for _ in range(map_size):
        row = [int(s) for s in input().split()]
        waters.append(row)
    commands: list[Command] = []
    for _ in range(command_count):
        d, s = (int(s) for s in input().split())
        d -= 1
        commands.append(Command(d, s))
    block_map = BlockMap(map_size, waters, [])
    simulate(block_map, commands)
    total_water = sum(sum(r) for r in block_map.waters)
    print(total_water)


class Spot(NamedTuple):
    row: int
    column: int


class BlockMap(NamedTuple):
    map_size: int
    waters: list[list[int]]
    clouds: list[Spot]


class Command(NamedTuple):
    direction: int
    dist: int


DIRECTIONS = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]


def simulate(block_map: BlockMap, commands: list[Command]):
    map_size, _, clouds = block_map

    # Make initial clouds.
    initial_clouds = [
        Spot(map_size - 2, 0),
        Spot(map_size - 2, 1),
        Spot(map_size - 1, 0),
        Spot(map_size - 1, 1),
    ]
    clouds.extend(initial_clouds)

    for command in commands:
        # Move clouds.
        direction, dist = command
        r_unit, c_unit = DIRECTIONS[direction]
        clouds_buffer: list[Spot] = []
        for cloud in clouds:
            r, c = cloud
            r_new = (r + r_unit * dist) % map_size
            c_new = (c + c_unit * dist) % map_size
            clouds_buffer.append(Spot(r_new, c_new))
        clouds.clear()
        clouds.extend(clouds_buffer)

        # Wait for natural phenomenons.
        no_cloud_zones = pour_rain(block_map)
        copy_water(block_map, no_cloud_zones)
        create_clouds(block_map, no_cloud_zones)


def pour_rain(block_map: BlockMap) -> list[list[bool]]:
    map_size, waters, clouds = block_map

    no_cloud_zones = [[False] * map_size for _ in range(map_size)]
    for r, c in clouds:
        waters[r][c] += 1
        no_cloud_zones[r][c] = True
    clouds.clear()

    return no_cloud_zones


ADJACENTS = [(-1, -1), (-1, 1), (1, -1), (1, 1)]


def copy_water(block_map: BlockMap, no_cloud_zones: list[list[bool]]):
    map_size, waters, _ = block_map

    buffer: list[tuple[Spot, int]] = []

    for r in range(map_size):
        for c in range(map_size):
            if not no_cloud_zones[r][c]:
                continue
            extra_water = 0
            for r_diff, c_diff in ADJACENTS:
                r_near, c_near = r + r_diff, c + c_diff
                if 0 <= r_near < map_size and 0 <= c_near < map_size:
                    if waters[r_near][c_near]:
                        extra_water += 1
            if extra_water:
                buffer.append((Spot(r, c), extra_water))

    for spot, extra_water in buffer:
        r, c = spot
        waters[r][c] += extra_water


EVAPORIZATION = 2


def create_clouds(block_map: BlockMap, no_cloud_zones: list[list[bool]]):
    map_size, waters, clouds = block_map

    for r in range(map_size):
        for c in range(map_size):
            if no_cloud_zones[r][c]:
                continue
            water = waters[r][c]
            if water < EVAPORIZATION:
                continue
            waters[r][c] = water - 2
            clouds.append(Spot(r, c))


main()
