#include <iostream>

auto main() -> int {
  int test_count = 0;
  std::cin >> test_count;
  for (int i = 0; i < test_count; i++) {
    int repeat_count = 0;
    std::string word_s;
    std::cin >> repeat_count >> word_s;
    for (auto letter : word_s) {
      std::cout << std::string(repeat_count, letter);
    }
    std::cout << "\n";
  }
}