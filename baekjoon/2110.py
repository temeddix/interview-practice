import sys


def get_max_router(houses: list[int], placing_dist: int) -> int:
    last_house = houses[0]  # Last house with router installed
    router_count = 1
    for i in range(1, len(houses)):
        house = houses[i]
        if house - last_house >= placing_dist:
            router_count += 1
            last_house = house
    return router_count


def get_max_placing_dist(houses: list[int], needed_router: int) -> int:
    # Bisect right
    left = 1
    right = houses[-1] - houses[0] + 1

    placing_dist = 1
    while left <= right:
        mid = (left + right) // 2
        max_router = get_max_router(houses, mid)
        if max_router < needed_router:
            placing_dist = mid - 1
            right = mid - 1
        else:
            left = mid + 1

    return placing_dist


def main():
    house_count, needed_router = (int(s) for s in input().split())
    houses: list[int] = []
    for _ in range(house_count):
        house = int(sys.stdin.readline())
        houses.append(house)
    houses.sort()
    max_placing_dist = get_max_placing_dist(houses, needed_router)
    print(max_placing_dist)


main()
