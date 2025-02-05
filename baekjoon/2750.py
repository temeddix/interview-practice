from sys import stdin, stdout


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
    return do_bubble_sort(numbers)


def do_insertion_sort(numbers: list[int]):
    # Time complexty O(n^2), stable.

    number_count = len(numbers)

    for i in range(1, number_count):
        key = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key


def do_bubble_sort(numbers: list[int]):
    # Time complexity O(n^2), stable.

    number_count = len(numbers)

    for i in range(number_count - 1, 0, -1):
        for j in range(0, i):
            next = numbers[j + 1]
            curr = numbers[j]
            if curr > next:
                numbers[j + 1] = curr
                numbers[j] = next


main()
