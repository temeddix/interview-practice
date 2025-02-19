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
    # LPS stands for "Longest Prefix which is also Suffix"

    pattern_len = len(pattern)
    lps_table = [0] * pattern_len  # Array to store LPS values
    lps_length = 0  # Length of the previous longest prefix-suffix

    # The LPS value for the first character (index 0) is always 0.
    # Start iterating from index 1.
    index_p = 1
    while index_p < pattern_len:
        if pattern[index_p] == pattern[lps_length]:
            # Characters match:
            # Extend the current prefix-suffix length.
            lps_length += 1
            lps_table[index_p] = lps_length
            index_p += 1  # Move to the next character
        elif lps_length != 0:
            # Characters do not match, but there was a previous prefix-suffix:
            # Fall back to the previous LPS value (without incrementing `index_p`).
            lps_length = lps_table[lps_length - 1]
        else:
            # Characters do not match and no prefix-suffix exists:
            # Set LPS value to 0 and move to the next character.
            lps_table[index_p] = 0
            index_p += 1

    return lps_table


main()
