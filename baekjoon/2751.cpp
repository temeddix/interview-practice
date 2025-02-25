#include <algorithm>
#include <iostream>
#include <vector>

auto main() -> int {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int count = 0;
  std::cin >> count;

  std::vector<int> numbers;
  numbers.reserve(count);
  for (int i = 0; i < count; i++) {
    int number = 0;
    std::cin >> number;
    numbers.push_back(number);
  }

  std::sort(numbers.begin(), numbers.end());
  for (int number : numbers) {
    std::cout << number << '\n';
  }
}