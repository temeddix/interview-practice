from math import ceil, sqrt
from typing import NamedTuple


def main():
    box_count, goal_gap = (int(s) for s in input().split())
    map_height = max(4, ceil(sqrt(box_count)))
    boxes = [[EMPTY] * map_height for _ in range(box_count)]
    for i, fish in enumerate(int(s) for s in input().split()):
        boxes[i][0] = fish
    space = Space(box_count, map_height, boxes)
    organize_count = organize_boxes(space, goal_gap)
    print(organize_count)


class Space(NamedTuple):
    map_width: int  # Same as box count
    map_height: int  # Same as box count
    boxes: list[list[int]]  # By X and Y coordinates.


INFINITY = 1_000_000_007
EMPTY = -1


def organize_boxes(space: Space, goal_gap: int) -> int:
    organize_count = 0
    while True:
        organize_count += 1
        add_fish(space)
        rotate_stackd(space)
        spread_fish(space)
        flatten_boxes(space)
        stack_four_layers(space)
        spread_fish(space)
        flatten_boxes(space)
        fish_gap = get_fish_gap(space)
        if fish_gap <= goal_gap:
            return organize_count


def add_fish(space: Space):
    map_width, _, boxes = space

    min_fish = min(boxes[i][0] for i in range(map_width))
    indices: list[int] = []
    for x in range(map_width):
        if boxes[x][0] == min_fish:
            indices.append(x)
    for x in indices:
        boxes[x][0] = min_fish + 1


def rotate_stackd(space: Space):
    map_width, _, boxes = space

    stack_x = 1  # Size of the stack group to rotate
    stack_y = 1  # Size of the stack group to rotate
    from_x, from_y = 0, 0  # Base point of start of rotation
    to_x, to_y = 1, 1  # Base point of end of rotation

    while from_x + stack_y < map_width:
        # Rotate the stack group.
        for left in range(stack_x):
            for up in range(stack_y):
                fish = boxes[from_x - left][from_y + up]
                boxes[to_x + up][to_y + left] = fish
                boxes[from_x - left][from_y + up] = EMPTY

        # Next stack group is 1 bigger than now.
        if stack_x < stack_y:
            stack_x += 1
        else:
            stack_y += 1
        from_x += stack_x
        to_x += stack_x


def spread_fish(space: Space):
    map_width, map_height, boxes = space

    buffer = [[0] * map_height for _ in range(map_width)]

    for x_diff, y_diff in ((1, 0), (0, 1)):
        for a_x in range(map_width - 1 if x_diff else map_width):
            for a_y in range(map_height - 1 if y_diff else map_height):
                b_x, b_y = a_x + x_diff, a_y + y_diff
                fish_a, fish_b = boxes[a_x][a_y], boxes[b_x][b_y]
                if EMPTY in (fish_a, fish_b):
                    continue
                exchange = abs(boxes[a_x][a_y] - boxes[b_x][b_y]) // 5
                if fish_a < fish_b:
                    buffer[a_x][a_y] += exchange
                    buffer[b_x][b_y] -= exchange
                else:
                    buffer[a_x][a_y] -= exchange
                    buffer[b_x][b_y] += exchange

    for x in range(map_width):
        for y in range(map_height):
            boxes[x][y] += buffer[x][y]


def flatten_boxes(space: Space):
    map_width, map_height, boxes = space

    buffer: list[int] = []
    for x in range(map_width):
        for y in range(map_height):
            fish = boxes[x][y]
            if fish != EMPTY:
                buffer.append(fish)
                boxes[x][y] = EMPTY

    for x in range(map_width):
        boxes[x][0] = buffer[x]


LAYERS = [1, 2, 3]


def stack_four_layers(space: Space):
    map_width, _, boxes = space
    group_size = map_width // 4

    for i in range(3):
        for j in range(group_size):
            reverse_horizontally = i % 2 == 1

            from_x = group_size * i + j
            from_y = 0
            to_x = (
                map_width - group_size + j
                if reverse_horizontally
                else map_width - 1 - j
            )
            to_y = LAYERS[i]

            fish = boxes[from_x][from_y]
            boxes[to_x][to_y] = fish
            boxes[from_x][from_y] = EMPTY


def get_fish_gap(space: Space) -> int:
    map_width, _, boxes = space

    min_fish = INFINITY
    max_fish = 0

    for x in range(map_width):
        fish = boxes[x][0]
        min_fish = min(min_fish, fish)
        max_fish = max(max_fish, fish)

    return max_fish - min_fish


main()
