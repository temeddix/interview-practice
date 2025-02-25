#include <algorithm>
#include <iostream>
#include <vector>

int main() {
  // Using vector here for practicing purposes
  // though array is faster.
  std::vector<int> numbers;
  numbers.reserve(1000);

  int count;
  std::cin >> count;

  for (int i = 0; i < count; i++) {
    int number;
    std::cin >> number;
    numbers.push_back(number);
  }

  std::sort(numbers.begin(), numbers.end());

  for (int number : numbers) {
    std::cout << number << '\n';
  }
}