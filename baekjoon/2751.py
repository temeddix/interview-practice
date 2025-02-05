from statistics import median
from sys import stdin, stdout
from typing import NamedTuple


def main():
    number_count = int(input())
    numbers: list[int] = []
    for _ in range(number_count):
        number = int(stdin.readline().strip())
        numbers.append(number)
    sort_numbers(numbers)
    for number in numbers:
        stdout.write(f"{number}\n")


def sort_numbers(numbers: list[int]):
    # Change this part to use other sorting algorithm.
    return do_quick_sort(numbers)


def do_insertion_sort(numbers: list[int]):
    # Time complexity O(n^2), Omega(n).
    # This method is stable.

    number_count = len(numbers)

    for i in range(1, number_count):
        key = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key


def do_bubble_sort(numbers: list[int]):
    # Time complexity O(n^2), Omega(n).
    # This method is stable.

    number_count = len(numbers)

    for i in range(number_count - 1, 0, -1):
        swapped = False
        for j in range(0, i):
            next = numbers[j + 1]
            curr = numbers[j]
            if curr > next:
                numbers[j + 1] = curr
                numbers[j] = next
                swapped = True
        if not swapped:
            break


def do_merge_sort(numbers: list[int]):
    # Time complexity O(n log n), Omega(n log n).
    # This method is stable.

    # Extra space is needed when using merge sort.
    temp: list[int] = [0 for _ in numbers]

    class IndexRange(NamedTuple):
        start: int  # Inclusive
        end: int  # Exclusive

    class Job(NamedTuple):
        is_head: bool
        index_range: IndexRange

    # Use iterative DFS.
    # Writing this way is harder but worth learning.
    dfs_stack: list[Job] = []
    full_range = IndexRange(0, len(numbers))
    dfs_stack.append(Job(False, full_range))
    dfs_stack.append(Job(True, full_range))

    while dfs_stack:
        is_head, index_range = dfs_stack.pop()

        start, end = index_range
        mid = (start + end) // 2

        # Divide and conquer.
        if is_head:
            # Do nothing when there's nothing to sort.
            if end - start <= 1:
                continue

            # Divide the range.
            left_range = IndexRange(start, mid)
            right_range = IndexRange(mid, end)

            # Add recursive jobs.
            for next_range in (left_range, right_range):
                dfs_stack.append(Job(False, next_range))
                dfs_stack.append(Job(True, next_range))

        # Next recursion logically runs here.

        # Merge left and right.
        else:
            # Prepare cursors.
            cur = start
            left_cur = start
            right_cur = mid

            # Merge left and right ranges.
            while left_cur < mid and right_cur < end:
                left_number = numbers[left_cur]
                right_number = numbers[right_cur]
                if left_number <= right_number:
                    temp[cur] = left_number
                    left_cur += 1
                else:
                    temp[cur] = right_number
                    right_cur += 1
                cur += 1

            # Copy remaining left values.
            while left_cur < mid:
                temp[cur] = numbers[left_cur]
                left_cur += 1
                cur += 1

            # Copy remaining right values.
            while right_cur < end:
                temp[cur] = numbers[right_cur]
                right_cur += 1
                cur += 1

            # Copy temporary values back to the original list.
            for index in range(start, end):
                numbers[index] = temp[index]


def do_quick_sort(numbers: list[int]):
    # Time complexity O(n^2), Omega(n log n).
    # This method is unstable.

    class IndexRange(NamedTuple):
        start: int  # Inclusive
        end: int  # Exclusive

    # Use iterative DFS.
    dfs_stack: list[IndexRange] = []
    full_range = IndexRange(0, len(numbers))
    dfs_stack.append(full_range)

    while dfs_stack:
        index_range = dfs_stack.pop()
        start, end = index_range

        # Do nothing when there's nothing to sort.
        if end - start <= 1:
            continue

        # Choose the pivot.
        pivot = numbers[start]

        # Put cursor at the left and the right end.
        left_cur = start + 1
        right_cur = end - 1

        # Move cursors closer, switching values if needed.
        while left_cur <= right_cur:
            # Move left pointer to the right.
            while left_cur <= right_cur and numbers[left_cur] <= pivot:
                left_cur += 1

            # Move right pointer to the left.
            while left_cur <= right_cur and numbers[right_cur] >= pivot:
                right_cur -= 1

            if left_cur < right_cur:
                # Swap the values at left and right cursors.
                previous_pair = (numbers[right_cur], numbers[left_cur])
                numbers[left_cur], numbers[right_cur] = previous_pair

        # Place pivot in the correct position.
        numbers[start], numbers[right_cur] = numbers[right_cur], numbers[start]

        # Add next recursion job.
        dfs_stack.append(IndexRange(start, right_cur))
        dfs_stack.append(IndexRange(right_cur + 1, end))


main()
