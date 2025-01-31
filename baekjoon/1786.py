from typing import NamedTuple


def main():
    text = input()
    pattern = input()
    occurences = find_occurences(text, pattern)
    print(len(occurences))
    print(" ".join(str(i + 1) for i in occurences))


def find_occurences(text: str, pattern: str) -> list[int]:
    cursor = 0
    pattern_len = len(pattern)
    max_cursor = len(text) - pattern_len
    kmp_list = get_kmp_list(pattern)

    occurences: list[int] = []
    start_letter = 0
    while cursor <= max_cursor:
        did_match = True
        for i in range(start_letter, pattern_len):
            if text[cursor + i] != pattern[i]:
                did_match = False
                base_shift, start_letter = kmp_list[i]
                cursor += base_shift
                break
        if did_match:
            occurences.append(cursor)
            base_shift, start_letter = kmp_list[-1]
            cursor += base_shift

    return occurences


class Shift(NamedTuple):
    base: int  # Movement of the base cursor
    letter: int  # Index of the pattern letter to start from


def get_kmp_list(pattern: str) -> list[Shift]:
    pattern_len = len(pattern)
    lps = [0] * pattern_len  # LPS table
    j = 0  # Length of previous longest prefix suffix

    # Build the LPS table
    for i in range(1, pattern_len):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]  # Fallback to previous LPS

        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j

    # Convert LPS table to Shift table
    kmp_list = [Shift(1, 0)]  # First entry always shifts 1
    for i in range(1, pattern_len + 1):
        base_shift = i - lps[i - 1]
        start_letter = lps[i - 1]
        kmp_list.append(Shift(base_shift, start_letter))

    return kmp_list


main()
