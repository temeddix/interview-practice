import sys
from dataclasses import dataclass


@dataclass
class Meeting:
    start_time: int
    end_time: int


def count_meetings(meetings: list[Meeting]) -> int:
    meetings = sorted(meetings, key=lambda m: (m.end_time, m.start_time))
    meetings_count = 0
    last_end_time = 0
    for meeting in meetings:
        if meeting.start_time < last_end_time:
            continue
        meetings_count += 1
        last_end_time = meeting.end_time
    return meetings_count


def main():
    meeting_count = int(input())
    meetings: list[Meeting] = []
    for _ in range(meeting_count):
        about_meeting = str(sys.stdin.readline()).strip().split()
        meeting = Meeting(
            start_time=int(about_meeting[0]),
            end_time=int(about_meeting[1]),
        )
        meetings.append(meeting)
    meetings_count = count_meetings(meetings)
    print(meetings_count)


main()
