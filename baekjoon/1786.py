def main():
    text = input()
    pattern = input()
    occurences = find_occurences(text, pattern)
    print(len(occurences))
    print(" ".join(str(i + 1) for i in occurences))


def find_occurences(text: str, pattern: str) -> list[int]:
    text_len = len(text)
    pattern_len = len(pattern)
    lps_table = get_lps_table(pattern)

    occurences: list[int] = []

    # Keep sliding the pattern block from left to right.
    # Base index of the pattern is represented as "`index_t` - `index_p`".
    index_t = 0  # Index of the current character in the text
    index_p = 0  # Index of the current character in the pattern
    while index_t < text_len:
        if text[index_t] == pattern[index_p]:
            # If the letter matches,
            # increase the index on both sides,
            # keeping the base index the same.
            index_t += 1
            index_p += 1
        elif index_p == 0:
            # If we are at the first letter of the pattern,
            # there's obviously no matching part.
            # Therefore shift the base index by 1.
            index_t += 1
        else:
            # Shift the base index with the precomputed LPS distance.
            index_p = lps_table[index_p - 1]

        # When the whole pattern has matched,
        # remember the base index inside the text.
        if index_p == pattern_len:
            occurences.append(index_t - index_p)
            index_p = lps_table[-1]

    return occurences


def get_lps_table(pattern: str) -> list[int]:
    # LPS stands for "Longest prefix and suffix"

    pattern_len = len(pattern)
    lps_table = [0] * pattern_len  # LPS table
    last_lps = 0  # Length of previous longest prefix suffix

    # Index 0 in LPS table is always 0.
    # Therefore start iterating from index 1.
    index_p = 1
    while index_p < pattern_len:
        if pattern[index_p] == pattern[last_lps]:
            # If the letter matches,
            # lengthen the prefix-suffix pair.
            last_lps += 1
            lps_table[index_p] = last_lps
            index_p += 1
        elif last_lps != 0:
            # If the letter doesn't match and
            # there was a prefix-suffix pair,
            # shorten the prefix-suffix pair length to retry matching.
            # Stay on the current index.
            last_lps = lps_table[last_lps - 1]
        else:
            # The letter doesn't match
            # and there's no existing prefix-suffix pair.
            lps_table[index_p] = 0
            index_p += 1

    return lps_table


main()
