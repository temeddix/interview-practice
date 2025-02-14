from sys import stdin
from typing import NamedTuple


def main():
    r_count, c_count, goal_heat = (int(s) for s in stdin.readline().split())
    test_spots: list[Spot] = []
    heaters: list[Heater] = []
    for r in range(r_count):
        line_input = (int(s) for s in stdin.readline().split())
        for c, value in enumerate(line_input):
            if value == EMPTY:
                pass
            elif value == TEST_SYMBOL:
                test_spots.append(Spot(r, c))
            else:
                heaters.append(Heater(Spot(r, c), value - 1))

    wall_count = int(stdin.readline().strip())
    cells = [[Cell(False, False, False, False)] * c_count for _ in range(r_count)]
    for _ in range(wall_count):
        x, y, t = (int(s) for s in stdin.readline().split())
        x, y = x - 1, y - 1
        if t == 0:
            w0, w1, _, w3 = cells[x][y]
            cells[x][y] = Cell(w0, w1, True, w3)  # Add up wall
            w0, w1, w2, _ = cells[x - 1][y]
            cells[x - 1][y] = Cell(w0, w1, w2, True)  # Add down wall
        else:
            _, w1, w2, w3 = cells[x][y]
            cells[x][y] = Cell(True, w1, w2, w3)  # Add right wall
            w0, _, w2, w3 = cells[x][y + 1]
            cells[x][y + 1] = Cell(w0, True, w2, w3)  # Add left wall

    heats = [[0] * c_count for _ in range(r_count)]
    block_map = BlockMap(r_count, c_count, cells, heats, heaters, test_spots)
    duration = simulate(block_map, goal_heat)
    print(duration)


EMPTY = 0
TEST_SYMBOL = 5


class Spot(NamedTuple):
    row: int
    column: int


class Heater(NamedTuple):
    spot: Spot
    direction: int


DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]


class Cell(NamedTuple):
    right_wall: bool
    left_wall: bool
    up_wall: bool
    down_wall: bool


class BlockMap(NamedTuple):
    r_count: int
    c_count: int
    cells: list[list[Cell]]
    heats: list[list[int]]
    heaters: list[Heater]
    test_spots: list[Spot]


def simulate(block_map: BlockMap, goal_heat: int) -> int:
    r_count, c_count, _, heats, _, test_spots = block_map
    influence = get_heater_influence(block_map)

    for i in range(100):
        # Make the machine work.
        for r in range(r_count):
            for c in range(c_count):
                heats[r][c] += influence[r][c]

        # Spread the heat.
        spread_heat(block_map)

        # Cool the exterior part.
        cool_exterior(block_map)

        # Check the temperature.
        is_finished = True
        for r, c in test_spots:
            heat = heats[r][c]
            if heat < goal_heat:
                is_finished = False
                break
        if is_finished:
            return i + 1

    return 101


class Cursor(NamedTuple):
    spot: Spot
    strength: int


INITIAL_STRENGTH = 5


def get_heater_influence(block_map: BlockMap) -> list[list[int]]:
    r_count, c_count, cells, _, heaters, _ = block_map
    influence = [[0] * c_count for _ in range(r_count)]

    for heater in heaters:
        visited = [[False] * c_count for _ in range(r_count)]

        heater_spot, heater_direction = heater
        r_heater, c_heater = heater_spot

        r_front, c_front = DIRECTIONS[heater_direction]  # Vector
        r_side, c_side = c_front, -r_front  # Vector

        r_start, c_start = r_heater + r_front, c_heater + c_front
        dfs_stack = [Cursor(Spot(r_start, c_start), INITIAL_STRENGTH)]
        while dfs_stack:
            spot, strength = dfs_stack.pop()
            r, c = spot
            if visited[r][c]:
                continue

            visited[r][c] = True
            influence[r][c] += strength

            next_strength = strength - 1
            if next_strength == 0:
                continue

            for flip_side in (-1, 1):
                r_go, c_go = r_side * flip_side, c_side * flip_side
                tween_direction = DIRECTIONS.index((r_go, c_go))
                r_tween, c_tween = r + r_go, c + c_go  # Middle spot of spreading
                if not (0 <= r_tween < r_count and 0 <= c_tween < c_count):
                    continue
                if cells[r][c][tween_direction]:  # Found a wall
                    continue
                if cells[r_tween][c_tween][heater_direction]:  # Found a wall
                    continue
                r_next, c_next = r_tween + r_front, c_tween + c_front
                if not (0 <= r_next < r_count and 0 <= c_next < c_count):
                    continue
                dfs_stack.append(Cursor(Spot(r_next, c_next), next_strength))

            if not cells[r][c][heater_direction]:  # No wall
                r_next, c_next = r + r_front, c + c_front
                if 0 <= r_next < r_count and 0 <= c_next < c_count:
                    dfs_stack.append(Cursor(Spot(r_next, c_next), next_strength))

    return influence


def spread_heat(block_map: BlockMap):
    r_count, c_count, cells, heats, _, _ = block_map

    buffer = [[0] * c_count for _ in range(r_count)]

    for r_diff, c_diff in ((1, 0), (0, 1)):
        for r_a in range(r_count - 1 if r_diff else r_count):
            for c_a in range(c_count - 1 if c_diff else c_count):
                if r_diff and cells[r_a][c_a][3]:
                    continue
                elif c_diff and cells[r_a][c_a][0]:
                    continue
                r_b, c_b = r_a + r_diff, c_a + c_diff
                heat_a = heats[r_a][c_a]
                heat_b = heats[r_b][c_b]
                exchange = abs(heat_a - heat_b) // 4
                if heat_a < heat_b:
                    buffer[r_a][c_a] += exchange
                    buffer[r_b][c_b] -= exchange
                else:
                    buffer[r_a][c_a] -= exchange
                    buffer[r_b][c_b] += exchange

    for r in range(r_count):
        for c in range(c_count):
            heats[r][c] += buffer[r][c]


def cool_exterior(block_map: BlockMap):
    r_count, c_count, _, heats, _, _ = block_map

    for r in (0, r_count - 1):
        for c in range(c_count):
            heat = heats[r][c]
            if heat > 0:
                heats[r][c] = heat - 1

    for r in range(1, r_count - 1):
        for c in (0, c_count - 1):
            heat = heats[r][c]
            if heat > 0:
                heats[r][c] = heat - 1


main()
