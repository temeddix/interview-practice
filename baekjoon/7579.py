from bisect import bisect_left

MAX_COST = 100 * 100

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
    extra_memories = [-1 for _ in range(MAX_COST + 1)]
    extra_memories[0] = 0

    for app_info in app_infos:
        for i in range(MAX_COST + 1):
            prev_cost = MAX_COST - i
            prev_extra_memory = extra_memories[prev_cost]
            real_cost = prev_cost
            while prev_extra_memory == -1:
                real_cost -= 1
                prev_extra_memory = extra_memories[real_cost]
            cost = prev_cost + app_info[1]
            extra_memory = prev_extra_memory + app_info[0]
            if cost > MAX_COST:
                continue
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
