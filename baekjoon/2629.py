def get_measurables(weights: list[int]) -> set[int]:
    measurables = set[int]([0])

    for weight in weights:
        new_measurables = set[int]()
        for measurable in measurables:
            new_measurables.add(measurable + weight)
            new_measurables.add(measurable - weight)
        measurables.update(new_measurables)

    return measurables


def main():
    _ = input()
    weights = [int(s) for s in input().split()]
    _ = input()
    marbles = [int(s) for s in input().split()]
    measurables = get_measurables(weights)
    results = (m in measurables for m in marbles)
    print(" ".join("Y" if r else "N" for r in results))


main()
