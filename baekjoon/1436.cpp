#include <iostream>
#include <string>

auto main() -> int {
  int n = 0;
  std::cin >> n;

  int turn = 0;
  int current = 666;
  while (true) {
    std::string string_n = std::to_string(current);
    int six_count = 0;
    bool is_doom = false;
    for (char letter : string_n) {
      if (letter == '6') {
        six_count += 1;
      } else {
        six_count = 0;
      }
      if (six_count == 3) {
        is_doom = true;
        break;
      }
    }
    if (is_doom) {
      turn += 1;
    }
    if (turn == n) {
      break;
    }
    if (current < 5666) {
      current += 1000;
    } else if (current == 5666) {
      current = 6660;
    } else if (current < 6670) {
      current += 1;
    } else if (current == 6670) {
      current = 7666;
    } else {
      current += 1;
    }
  }

  std::cout << current << '\n';
}