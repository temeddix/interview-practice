#include <iostream>

auto main() -> int {
  char letter = 0;
  std::cin >> letter;
  std::cout << static_cast<int>(letter);
}