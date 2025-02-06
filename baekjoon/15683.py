from typing import NamedTuple


def main():
    map_height, map_width = (int(s) for s in input().split())
    map_size = MapSize(map_height, map_width)
    input_lines: list[str] = []
    for _ in range(map_height):
        input_lines.append(input())
    block_map = construct_block_map(input_lines, map_size)
    min_blind_spots = find_min_blind_spots(block_map)
    print(min_blind_spots)


class View(NamedTuple):
    north: bool
    east: bool
    south: bool
    west: bool


class Spot(NamedTuple):
    row: int
    col: int


class Camera(NamedTuple):
    spot: Spot
    views: list[View]


class MapSize(NamedTuple):
    height: int
    width: int


class BlockMap(NamedTuple):
    walls: list[list[bool]]
    cameras: list[Camera]
    size: MapSize


INITIAL_VIEWS = {
    1: View(False, True, False, False),
    2: View(False, True, False, True),
    3: View(True, True, False, False),
    4: View(True, True, False, True),
    5: View(True, True, True, True),
}

WALL = 6


def construct_block_map(input_lines: list[str], map_size: MapSize) -> BlockMap:
    walls: list[list[bool]] = []
    cameras: list[Camera] = []

    for i, input_line in enumerate(input_lines):
        int_row = [int(s) for s in input_line.split()]
        wall_row: list[bool] = []
        for j, value in enumerate(int_row):
            if value == WALL:
                wall_row.append(True)
            else:
                wall_row.append(False)
                if value != 0:
                    spot = Spot(i, j)
                    camera = construct_camera(spot, value)
                    cameras.append(camera)
        walls.append(wall_row)

    return BlockMap(walls, cameras, map_size)


def rotate_view(view: View) -> View:
    # Rotate the view 90 degrees clockwise.
    north, east, south, west = view
    return View(west, north, east, south)


def construct_camera(spot: Spot, family: int) -> Camera:
    views = set[View]()

    view = INITIAL_VIEWS[family]
    views.add(view)
    for _ in range(3):
        view = rotate_view(view)
        views.add(view)

    return Camera(spot, list(views))


class Job(NamedTuple):
    is_head: int
    camera_index: int
    view_index: int


class FixedCamera(NamedTuple):
    spot: Spot
    view: View


def find_min_blind_spots(block_map: BlockMap) -> int:
    walls, cameras, _ = block_map

    camera_count = len(cameras)
    empty_spots = 0
    for wall_row in walls:
        empty_spots += wall_row.count(False)

    min_blind_spots = empty_spots - camera_count
    if not cameras:
        return min_blind_spots

    dfs_stack: list[Job] = []
    fixed_cameras: list[FixedCamera] = []
    for view_index in range(len(cameras[0].views)):
        dfs_stack.append(Job(False, 0, view_index))
        dfs_stack.append(Job(True, 0, view_index))

    while dfs_stack:
        is_head, camera_index, view_index = dfs_stack.pop()

        if is_head:
            camera = cameras[camera_index]
            spot, views = camera
            fixed_camera = FixedCamera(spot, views[view_index])
            fixed_cameras.append(fixed_camera)

            next_camera_index = camera_index + 1
            if next_camera_index == camera_count:
                # Calculate blind spots with fixed cameras.
                blind_spots = find_blind_spots(block_map, fixed_cameras, empty_spots)
                min_blind_spots = min(min_blind_spots, blind_spots)
            else:
                # Add subsequent recursion call.
                next_camera = cameras[next_camera_index]
                for view_index in range(len(next_camera[1])):
                    dfs_stack.append(Job(False, next_camera_index, view_index))
                    dfs_stack.append(Job(True, next_camera_index, view_index))

        else:
            fixed_cameras.pop()

    return min_blind_spots


class Direction(NamedTuple):
    vertical: int  # -1, 0, 1
    horizontal: int  # -1, 0, 1


DIRECTIONS = [
    Direction(-1, 0),
    Direction(0, 1),
    Direction(1, 0),
    Direction(0, -1),
]


def find_blind_spots(
    block_map: BlockMap,
    fixed_cameras: list[FixedCamera],
    empty_spots: int,
) -> int:
    walls, _, map_size = block_map

    blind_spots = empty_spots
    blind_map: list[list[bool]] = []
    for wall_row in walls:
        blind_row = [not v for v in wall_row]
        blind_map.append(blind_row)

    for fixed_camera in fixed_cameras:
        spot, view = fixed_camera
        camera_row, camera_col = spot

        if blind_map[spot[0]][spot[1]]:
            blind_map[spot[0]][spot[1]] = False
            blind_spots -= 1

        for movement_index, should_move in enumerate(view):
            if not should_move:
                continue

            direction = DIRECTIONS[movement_index]
            curr_row = camera_row + direction[0]
            curr_col = camera_col + direction[1]

            while is_spot_inside(Spot(curr_row, curr_col), map_size):
                if walls[curr_row][curr_col]:
                    break
                if blind_map[curr_row][curr_col]:
                    blind_map[curr_row][curr_col] = False
                    blind_spots -= 1
                curr_row += direction[0]
                curr_col += direction[1]

    return blind_spots


def is_spot_inside(spot: Spot, map_size: MapSize) -> bool:
    row, col = spot
    height, width = map_size

    if not 0 <= row < height:
        return False
    if not 0 <= col < width:
        return False
    return True


main()
