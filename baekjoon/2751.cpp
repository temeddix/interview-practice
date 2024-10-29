#include <algorithm>
#include <iostream>
#include <vector>

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(0);

  int count;
  std::cin >> count;

  std::vector<int> numbers;
  numbers.reserve(count);
  for (int i = 0; i < count; i++) {
    int number;
    std::cin >> number;
    numbers.push_back(number);
  }

  std::sort(numbers.begin(), numbers.end());
  for (int number : numbers) {
    std::cout << number << '\n';
  }

  return 0;
}