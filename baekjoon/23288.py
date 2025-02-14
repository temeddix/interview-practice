from sys import stdin
from typing import NamedTuple


def main():
    r_count, c_count, moves = (int(s) for s in stdin.readline().split())
    numbers: list[list[int]] = []
    for _ in range(r_count):
        number_row = [int(s) for s in stdin.readline().split()]
        numbers.append(number_row)
    scores = calculate_scores(numbers)
    block_map = BlockMap(r_count, c_count, numbers, scores)
    total_score = roll_dice(block_map, moves)
    print(total_score)


class Dice:
    def __init__(self):
        self.spot = Spot(0, 0)
        self.direction = 1

        self.up = 1
        self.back = 2
        self.right = 3
        self.front = 5
        self.left = 4
        self.down = 6

    def roll(self):
        direction = self.direction

        if direction == NORTH:
            self.roll_north()
        elif direction == EAST:
            self.roll_east()
        elif direction == SOUTH:
            self.roll_south()
        elif direction == WEST:
            self.roll_west()
        else:
            raise ValueError

    def roll_north(self):
        prev_down = self.down
        self.down = self.back
        self.back = self.up
        self.up = self.front
        self.front = prev_down

    def roll_south(self):
        prev_down = self.down
        self.down = self.front
        self.front = self.up
        self.up = self.back
        self.back = prev_down

    def roll_east(self):
        prev_down = self.down
        self.down = self.right
        self.right = self.up
        self.up = self.left
        self.left = prev_down

    def roll_west(self):
        prev_down = self.down
        self.down = self.left
        self.left = self.up
        self.up = self.right
        self.right = prev_down


NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DIRECTION_COUNT = len(DIRECTIONS)


class BlockMap(NamedTuple):
    r_count: int
    c_count: int
    numbers: list[list[int]]
    scores: list[list[int]]


class Spot(NamedTuple):
    row: int
    column: int


def roll_dice(block_map: BlockMap, moves: int) -> int:
    r_count, c_count, numbers, scores = block_map
    dice = Dice()

    total_score = 0
    for _ in range(moves):
        # Go to the next spot.
        r_prev, c_prev = dice.spot
        r_diff, c_diff = DIRECTIONS[dice.direction]
        r, c = r_prev + r_diff, c_prev + c_diff
        if not (0 <= r < r_count and 0 <= c < c_count):
            dice.direction = (dice.direction + 2) % DIRECTION_COUNT
            r_diff, c_diff = DIRECTIONS[dice.direction]
            r, c = r_prev + r_diff, c_prev + c_diff
        dice.roll()
        dice.spot = Spot(r, c)

        # Get the score.
        total_score += scores[r][c]

        # Determine the direction.
        dice_number = dice.down
        map_number = numbers[r][c]
        if dice_number > map_number:
            dice.direction = (dice.direction + 1) % DIRECTION_COUNT
        elif dice_number < map_number:
            dice.direction = (dice.direction - 1) % DIRECTION_COUNT

    return total_score


ADJACENTS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def calculate_scores(numbers: list[list[int]]) -> list[list[int]]:
    r_count = len(numbers)
    c_count = len(numbers[0])

    visited = [[False] * c_count for _ in range(r_count)]
    scores = [[0] * c_count for _ in range(r_count)]

    for r_start in range(r_count):
        for c_start in range(c_count):
            if visited[r_start][c_start]:
                continue

            group_number = numbers[r_start][c_start]
            group_spots: list[Spot] = []

            dfs_stack: list[Spot] = [Spot(r_start, c_start)]
            while dfs_stack:
                spot = dfs_stack.pop()
                r, c = spot
                if visited[r][c]:
                    continue
                if numbers[r][c] != group_number:
                    continue
                visited[r][c] = True
                group_spots.append(Spot(r, c))
                for r_diff, c_diff in ADJACENTS:
                    r_next, c_next = r + r_diff, c + c_diff
                    if 0 <= r_next < r_count and 0 <= c_next < c_count:
                        dfs_stack.append(Spot(r_next, c_next))

            group_size = len(group_spots)
            score = group_number * group_size
            for r, c in group_spots:
                scores[r][c] = score

    return scores


main()
