#include <array>
#include <iostream>

auto main() -> int {
  std::array<int, 26> counts{};
  counts.fill(0);

  std::string word;
  std::cin >> word;

  for (auto letter : word) {
    int letter_number = 0;
    if (letter <= 'Z') {
      letter_number = letter - 'A';
    } else {
      letter_number = letter - 'a';
    }
    counts[letter_number] += 1;
  }

  char max_letter = 0;
  int max_count = 0;
  bool is_duplicated = false;
  for (int i = 0; i < counts.size(); i++) {
    int count = counts[i];
    if (max_count < count) {
      max_letter = 'A' + i;
      max_count = count;
      is_duplicated = false;
    } else if (max_count == count) {
      is_duplicated = true;
    }
  }

  if (is_duplicated) {
    std::cout << '?' << '\n';
  } else {
    std::cout << max_letter << '\n';
  }
}