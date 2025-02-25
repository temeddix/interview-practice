#include <algorithm>
#include <iostream>

auto main() -> int {
  int numbers[5];

  int sum = 0;
  for (int& i : numbers) {
    int number = 0;
    std::cin >> number;
    sum += number;
    i = number;
  }

  std::sort(numbers, numbers + 5);
  int middle = numbers[2];
  int average = sum / 5;

  std::cout << average << '\n' << middle << '\n';
}