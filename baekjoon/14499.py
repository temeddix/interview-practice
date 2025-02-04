from typing import NamedTuple


def main():
    map_height, _, dice_row, dice_column, _ = (int(s) for s in input().split())
    start_spot = Spot(dice_row, dice_column)
    block_map: list[list[int]] = []
    for _ in range(map_height):
        row = [int(s) for s in input().split()]
        block_map.append(row)
    commands = [int(s) for s in input().split()]
    result = roll_dice(start_spot, block_map, commands)
    print("\n".join(str(i) for i in result))


class MapSize(NamedTuple):
    row: int
    column: int


class Spot(NamedTuple):
    row: int
    column: int


class Dice:
    __slots__ = ("top", "north", "east", "south", "west", "bottom")

    def __init__(self):
        self.top = 0
        self.north = 0
        self.east = 0
        self.south = 0
        self.west = 0
        self.bottom = 0

    def roll(self, command: int):
        if command == COMMAND_EAST:
            self.roll_east()
        elif command == COMMAND_WEST:
            self.roll_west()
        elif command == COMMAND_NORTH:
            self.roll_north()
        elif command == COMMAND_SOUTH:
            self.roll_south()
        else:
            raise ValueError

    def roll_east(self):
        prev_bottom = self.bottom
        self.bottom = self.east
        self.east = self.top
        self.top = self.west
        self.west = prev_bottom

    def roll_west(self):
        prev_bottom = self.bottom
        self.bottom = self.west
        self.west = self.top
        self.top = self.east
        self.east = prev_bottom

    def roll_north(self):
        prev_bottom = self.bottom
        self.bottom = self.north
        self.north = self.top
        self.top = self.south
        self.south = prev_bottom

    def roll_south(self):
        prev_bottom = self.bottom
        self.bottom = self.south
        self.south = self.top
        self.top = self.north
        self.north = prev_bottom


COMMAND_EAST = 1
COMMAND_WEST = 2
COMMAND_NORTH = 3
COMMAND_SOUTH = 4


def roll_dice(
    start_spot: Spot,
    block_map: list[list[int]],
    commands: list[int],
) -> list[int]:
    map_height = len(block_map)
    map_width = len(block_map[0])
    map_size = MapSize(map_height, map_width)

    top_face_record: list[int] = []
    dice_spot = start_spot

    dice = Dice()
    for command in commands:
        # Move the dice.
        if command == COMMAND_EAST:
            new_spot = Spot(dice_spot[0], dice_spot[1] + 1)
        elif command == COMMAND_WEST:
            new_spot = Spot(dice_spot[0], dice_spot[1] - 1)
        elif command == COMMAND_NORTH:
            new_spot = Spot(dice_spot[0] - 1, dice_spot[1])
        elif command == COMMAND_SOUTH:
            new_spot = Spot(dice_spot[0] + 1, dice_spot[1])
        else:
            raise ValueError
        if not is_spot_valid(map_size, new_spot):
            continue
        dice_spot = new_spot

        # Roll the dice.
        dice.roll(command)

        # Clone the number.
        block_value = block_map[dice_spot[0]][dice_spot[1]]
        if block_value == 0:
            block_map[dice_spot[0]][dice_spot[1]] = dice.bottom
        else:
            dice.bottom = block_value
            block_map[dice_spot[0]][dice_spot[1]] = 0

        # Record the top face.
        top_face_record.append(dice.top)

    return top_face_record


def is_spot_valid(map_size: MapSize, spot: Spot) -> bool:
    map_height, map_width = map_size
    if not 0 <= spot[0] < map_height:
        return False
    if not 0 <= spot[1] < map_width:
        return False
    return True


main()
