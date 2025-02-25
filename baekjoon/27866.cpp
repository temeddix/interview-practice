#include <array>
#include <iostream>

auto main() -> int {
  std::array<char, 1000> word{};
  std::cin >> word.data();
  int index = 0;
  std::cin >> index;
  std::cout << word[index - 1] << '\n';
}