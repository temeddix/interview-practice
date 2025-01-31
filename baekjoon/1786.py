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

    # Base index is represented as "`index_t` - `index_p`".
    index_t = 0  # Index for the text
    index_p = 0  # Index for the pattern
    while index_t < text_len:
        if text[index_t] == pattern[index_p]:
            # If the letter matches,
            # increase the index on both sides,
            # keeping the base index the same.
            index_t += 1
            index_p += 1
        elif index_p == 0:
            # If the pattern index is 0,
            # there's obviously no matching part.
            # Therefore shift the base index by 1.
            index_t += 1
        else:
            # Analyze again from the short LPS.
            # This shifts the base index with a big step.
            index_p = lps_table[index_p - 1]

        # When the whole pattern has matched,
        # remember the base index inside the text.
        if index_p == pattern_len:
            occurences.append(index_t - index_p)
            index_p = lps_table[index_p - 1]

    return occurences


def get_lps_table(pattern: str) -> list[int]:
    pattern_len = len(pattern)
    lps_table = [0] * pattern_len  # LPS table
    last_lps = 0  # Length of previous longest prefix suffix

    # Build the LPS table.
    for index_p in range(1, pattern_len):
        while last_lps > 0 and pattern[index_p] != pattern[last_lps]:
            # Fallback to previous LPS.
            last_lps = lps_table[last_lps - 1]

        if pattern[index_p] == pattern[last_lps]:
            last_lps += 1
            lps_table[index_p] = last_lps

    return lps_table


main()
