#include <array>
#include <iostream>

int main() {
  int count;
  std::cin >> count;

  int grouped_words = 0;
  for (int i = 0; i < count; i++) {
    std::array<char, 101> word;
    std::cin >> word.data();

    std::array<bool, 26> seen_chars;
    seen_chars.fill(false);
    char last_char = '.';

    bool is_grouped = true;
    for (int j = 0; word[j] != '\0'; j++) {
      char this_char = word[j];
      if (this_char != last_char) {
        int alphabet_index = this_char - 'a';
        if (seen_chars[alphabet_index]) {
          is_grouped = false;
          break;
        }
        last_char = this_char;
        seen_chars[alphabet_index] = true;
      }
    }

    if (is_grouped) {
      grouped_words += 1;
    }
  }

  std::cout << grouped_words << std::endl;
  return 0;
}