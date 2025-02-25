#include <iostream>
#include <string>

auto main() -> int {
  int count = 0;
  std::cin >> count;

  for (int i = 0; i < count; i++) {
    std::string p_string;
    std::cin >> p_string;
    int stack_level = 0;
    for (char letter : p_string) {
      if (letter == '(') {
        stack_level += 1;
      } else {
        stack_level -= 1;
      }
      if (stack_level < 0) {
        break;
      }
    }
    if (stack_level == 0) {
      std::cout << "YES" << '\n';
    } else {
      std::cout << "NO" << '\n';
    }
  }
}