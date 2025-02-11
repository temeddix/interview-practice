from typing import NamedTuple


def main():
    wheel_count, step_count, operation_count = (int(s) for s in input().split())
    wheels: list[list[int]] = []
    for _ in range(wheel_count):
        wheel = [int(s) for s in input().split()]
        wheels.append(wheel)
    structure = Structure(wheel_count, step_count, wheels)
    operations: list[Operation] = []
    for _ in range(operation_count):
        x, d, k = (int(s) for s in input().split())
        operation = Operation(x, True if d == 0 else False, k)
        operations.append(operation)
    number_sum = operate(structure, operations)
    print(number_sum)


class Operation(NamedTuple):
    base_radius: int
    clockwise: bool
    steps: int


class Structure(NamedTuple):
    wheel_count: int
    step_count: int
    wheels: list[list[int]]


class Spot(NamedTuple):
    wheel: int
    step: int


ADJACENTS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
EMPTY = 0


def operate(structure: Structure, operations: list[Operation]) -> int:
    wheel_count, step_count, wheels = structure

    for operation in operations:
        # Rotate wheels.
        rotate_wheels(structure, operation)

        # Collect adjacent numbers.
        number_groups = group_adjacent_numbers(structure)

        # Manipulate values.
        if number_groups:
            for spot_group in number_groups:
                for w, s in spot_group:
                    wheels[w][s] = EMPTY
        else:
            all_numbers: list[int] = []
            for wheel in wheels:
                all_numbers.extend(i for i in wheel if i != EMPTY)
            if all_numbers:
                sum_value = sum(all_numbers)
                mean_value = sum_value / len(all_numbers)
                for w in range(wheel_count):
                    for s in range(step_count):
                        number = wheels[w][s]
                        if number == EMPTY:
                            continue
                        if number < mean_value:
                            wheels[w][s] = number + 1
                        elif number > mean_value:
                            wheels[w][s] = number - 1

    sum_value = sum(sum(w) for w in wheels)
    return sum_value


def rotate_wheels(structure: Structure, operation: Operation):
    _, step_count, wheels = structure
    base_radius, clockwise, steps = operation
    steps = steps % step_count

    for w, wheel in enumerate(wheels):
        if (w + 1) % base_radius != 0:
            continue
        if clockwise:
            wheels[w] = wheel[-steps:] + wheel[:-steps]
        else:
            wheels[w] = wheel[steps:] + wheel[:steps]


def group_adjacent_numbers(structure: Structure) -> list[list[Spot]]:
    wheel_count, step_count, wheels = structure

    spot_groups: list[list[Spot]] = []
    visited: list[list[bool]] = [[False for _ in w] for w in wheels]
    for start_w in range(wheel_count):
        for start_s in range(step_count):
            if visited[start_w][start_s]:
                continue
            number = wheels[start_w][start_s]
            if number == EMPTY:
                continue
            spot_group: list[Spot] = []
            dfs_stack: list[Spot] = [Spot(start_w, start_s)]
            while dfs_stack:
                spot = dfs_stack.pop()
                w, s = spot
                visited[w][s] = True
                spot_group.append(spot)
                for w_diff, s_diff in ADJACENTS:
                    w_new = w + w_diff
                    if not 0 <= w_new < wheel_count:
                        continue
                    s_new = (s + s_diff + step_count) % step_count
                    if visited[w_new][s_new]:
                        continue
                    if wheels[w_new][s_new] == number:
                        dfs_stack.append(Spot(w_new, s_new))
            if len(spot_group) > 1:
                spot_groups.append(spot_group)

    return spot_groups


main()
