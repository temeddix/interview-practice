from sys import stdin
from typing import NamedTuple


def main():
    people_count = int(stdin.readline().strip())

    pair_count = 0
    front_people: list[Group] = []
    for _ in range(people_count):
        height = int(stdin.readline().strip())
        max_between = 0

        while front_people and front_people[-1][0] < height:
            between, size = front_people.pop()
            if between >= max_between:
                pair_count += size
            max_between = max(max_between, between)

        if front_people:
            previous_height, previous_size = front_people[-1]
            if previous_height == height:
                if len(front_people) == 1:
                    pair_count += previous_size
                else:
                    pair_count += previous_size + 1
                front_people[-1] = Group(height, previous_size + 1)
            else:
                pair_count += 1
                front_people.append(Group(height, 1))
        else:
            front_people.append(Group(height, 1))

    print(pair_count)


class Group(NamedTuple):
    height: int
    size: int


main()
