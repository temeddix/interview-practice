#include <cmath>
#include <iostream>

auto main() -> int {
  int count = 0;
  std::cin >> count;

  int open = std::sqrt(count);
  std::cout << open << '\n';
}