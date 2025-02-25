#include <iostream>
#include <queue>
#include <string>

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(NULL);
  std::cout.tie(NULL);

  int operations;
  std::cin >> operations;

  std::queue<int> numbers;
  for (int i = 0; i < operations; i++) {
    std::string command;
    std::cin >> command;
    if (command == "push") {
      int number;
      std::cin >> number;
      numbers.push(number);
    } else if (command == "pop") {
      int number;
      if (numbers.size()) {
        number = numbers.front();
        numbers.pop();
      } else {
        number = -1;
      }
      std::cout << number << '\n';
    } else if (command == "size") {
      std::cout << numbers.size() << '\n';
    } else if (command == "empty") {
      std::cout << (numbers.size() == 0 ? 1 : 0) << '\n';
    } else if (command == "front") {
      int number;
      if (numbers.size()) {
        number = numbers.front();
      } else {
        number = -1;
      }
      std::cout << number << '\n';
    } else if (command == "back") {
      int number;
      if (numbers.size()) {
        number = numbers.back();
      } else {
        number = -1;
      }
      std::cout << number << '\n';
    }
  }
}