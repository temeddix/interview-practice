#include <iostream>
#include <queue>
#include <string>

auto main() -> int {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);
  std::cout.tie(nullptr);

  int operations = 0;
  std::cin >> operations;

  std::queue<int> numbers;
  for (int i = 0; i < operations; i++) {
    std::string command;
    std::cin >> command;
    if (command == "push") {
      int number = 0;
      std::cin >> number;
      numbers.push(number);
    } else if (command == "pop") {
      int number = 0;
      if (static_cast<unsigned int>(!numbers.empty()) != 0U) {
        number = numbers.front();
        numbers.pop();
      } else {
        number = -1;
      }
      std::cout << number << '\n';
    } else if (command == "size") {
      std::cout << numbers.size() << '\n';
    } else if (command == "empty") {
      std::cout << (numbers.empty() ? 1 : 0) << '\n';
    } else if (command == "front") {
      int number = 0;
      if (static_cast<unsigned int>(!numbers.empty()) != 0U) {
        number = numbers.front();
      } else {
        number = -1;
      }
      std::cout << number << '\n';
    } else if (command == "back") {
      int number = 0;
      if (static_cast<unsigned int>(!numbers.empty()) != 0U) {
        number = numbers.back();
      } else {
        number = -1;
      }
      std::cout << number << '\n';
    }
  }
}