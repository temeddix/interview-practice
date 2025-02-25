#include <array>
#include <iostream>

auto main() -> int {
  std::array<std::array<char, 15>, 5> arrays{};
  for (auto& array : arrays) {
    array.fill('.');
  }

  for (int i = 0; i < 5; i++) {
    for (int j = 0; j < 16; j++) {
      char value = std::cin.get();
      if (value == '\n') {
        break;
      }
      arrays[i][j] = value;
    }
  }

  for (int i = 0; i < 15; i++) {
    for (int j = 0; j < 5; j++) {
      char value = arrays[j][i];
      if (value != '.') {
        std::cout << value;
      }
    }
  }
}