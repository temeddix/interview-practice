#include <deque>
#include <iostream>

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(NULL);
  std::cout.tie(NULL);

  int operations;
  std::cin >> operations;

  std::deque<int> numbers;
  for (int i = 0; i < operations; i++) {
    int operation;
    std::cin >> operation;
    switch (operation) {
      case 1: {
        int number;
        std::cin >> number;
        numbers.push_front(number);
        break;
      }
      case 2: {
        int number;
        std::cin >> number;
        numbers.push_back(number);
        break;
      }
      case 3: {
        int number;
        if (numbers.size()) {
          number = numbers.front();
          numbers.pop_front();
        } else {
          number = -1;
        }
        std::cout << number << '\n';
        break;
      }
      case 4: {
        int number;
        if (numbers.size()) {
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
        std::cout << (numbers.size() == 0 ? 1 : 0) << '\n';
        break;
      }
      case 7: {
        std::cout << (numbers.size() ? numbers.front() : -1) << '\n';
        break;
      }
      case 8: {
        std::cout << (numbers.size() ? numbers.back() : -1) << '\n';
        break;
      }
      default: {
        break;
      }
    }
  }

  return 0;
}