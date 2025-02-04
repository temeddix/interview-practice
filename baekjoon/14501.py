from typing import NamedTuple


def main():
    day_count = int(input())
    tasks: list[Task] = []
    for day in range(day_count):
        duration, reward = (int(s) for s in input().split())
        task = Task(day, duration, reward)
        tasks.append(task)
    max_reward = calculate_max_reward(tasks)
    print(max_reward)


class Task(NamedTuple):
    day: int
    duration: int
    reward: int


def calculate_max_reward(tasks: list[Task]) -> int:
    day_count = len(tasks)
    dp_list = [0 for _ in tasks]

    for day, duaration, reward in reversed(tasks):
        next_available_day = day + duaration
        if next_available_day == day_count:
            reward_accepting = reward
        elif next_available_day < day_count:
            reward_accepting = dp_list[next_available_day] + reward
        else:
            reward_accepting = 0

        next_day = day + 1
        if next_day < day_count:
            reward_rejecting = dp_list[next_day]
        else:
            reward_rejecting = 0

        max_reward_from_day = max(reward_accepting, reward_rejecting)
        dp_list[day] = max_reward_from_day

    return dp_list[0]


main()
