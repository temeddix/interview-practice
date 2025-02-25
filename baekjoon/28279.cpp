#include <deque>
#include <iostream>

auto main() -> int {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);
  std::cout.tie(nullptr);

  int operations = 0;
  std::cin >> operations;

  std::deque<int> numbers;
  for (int i = 0; i < operations; i++) {
    int operation = 0;
    std::cin >> operation;
    switch (operation) {
      case 1: {
        int number = 0;
        std::cin >> number;
        numbers.push_front(number);
        break;
      }
      case 2: {
        int number = 0;
        std::cin >> number;
        numbers.push_back(number);
        break;
      }
      case 3: {
        int number = 0;
        if (static_cast<unsigned int>(!numbers.empty()) != 0U) {
          number = numbers.front();
          numbers.pop_front();
        } else {
          number = -1;
        }
        std::cout << number << '\n';
        break;
      }
      case 4: {
        int number = 0;
        if (static_cast<unsigned int>(!numbers.empty()) != 0U) {
          number = numbers.back();
          numbers.pop_back();
        } else {
          number = -1;
        }
        std::cout << number << '\n';
        break;
      }
      case 5: {
        std::cout << numbers.size() << '\n';
        break;
      }
      case 6: {
        std::cout << (numbers.empty() ? 1 : 0) << '\n';
        break;
      }
      case 7: {
        std::cout << ((static_cast<unsigned int>(!numbers.empty()) != 0U) ? numbers.front() : -1) << '\n';
        break;
      }
      case 8: {
        std::cout << ((static_cast<unsigned int>(!numbers.empty()) != 0U) ? numbers.back() : -1) << '\n';
        break;
      }
      default: {
        break;
      }
    }
  }
}