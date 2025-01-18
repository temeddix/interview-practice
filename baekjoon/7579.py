from bisect import bisect_left

AppInfo = tuple[
    int,  # Occupying memory(m)
    int,  # Startup cost(c)
]

MemoryAct = tuple[
    int,  # Extra memory available
    int,  # Startup cost needed
]


def find_min_cost(needed_memory: int, app_infos: list[AppInfo]) -> int:
    # Index represents the startup cost spent
    max_cost = sum(a[1] for a in app_infos)
    extra_memories = [0 for _ in range(max_cost + 1)]

    for app_info in app_infos:
        for cost in range(max_cost, app_info[1] - 1, -1):
            prev_cost = cost - app_info[1]
            extra_memory = extra_memories[prev_cost] + app_info[0]
            extra_memories[cost] = max(extra_memories[cost], extra_memory)

    return bisect_left(extra_memories, needed_memory)


def main():
    _, needed_memory = (int(s) for s in input().split())
    memory_infos = (int(s) for s in input().split())
    cost_infos = (int(s) for s in input().split())
    app_infos: list[AppInfo] = []
    for app_info in zip(memory_infos, cost_infos):
        app_infos.append(app_info)
    min_cost = find_min_cost(needed_memory, app_infos)
    print(min_cost)


main()
