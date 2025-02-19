def main():
    _ = int(input())
    visible_text = input()
    longest_prefix_suffix = get_longest_prefix_suffix(visible_text)
    text_len = len(visible_text)
    print(text_len - longest_prefix_suffix)


def get_longest_prefix_suffix(text: str) -> int:
    # LPS stands for "Longest Prefix which is also Suffix"

    text_len = len(text)
    lps_table = [0] * text_len  # Array to store LPS values
    lps_length = 0  # Length of the previous longest prefix-suffix

    # The LPS value for the first character (index 0) is always 0.
    # Start iterating from index 1.
    index = 1
    while index < text_len:
        if text[index] == text[lps_length]:
            # Characters match:
            # Extend the current prefix-suffix length.
            lps_length += 1
            lps_table[index] = lps_length
            index += 1  # Move to the next character
        elif lps_length != 0:
            # Characters do not match, but there was a previous prefix-suffix:
            # Fall back to the previous LPS value (without incrementing `index`).
            lps_length = lps_table[lps_length - 1]
        else:
            # Characters do not match and no prefix-suffix exists:
            # Set LPS value to 0 and move to the next character.
            lps_table[index] = 0
            index += 1

    return lps_table[-1]


main()
