def main():
    _ = int(input())
    takers_list: list[int] = [int(s) for s in input().split()]
    main_covergae, sub_coverage = (int(s) for s in input().split())
    supervisors = 0
    for takers in takers_list:
        leftover = takers
        leftover -= main_covergae
        supervisors += 1
        sub_supervisors = max(0, ((leftover - 1) // sub_coverage) + 1)
        supervisors += sub_supervisors
    print(supervisors)


main()
