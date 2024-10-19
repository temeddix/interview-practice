#include <array>
#include <iostream>

int main() {
  int count;
  std::cin >> count;
  std::array<char, 1000> numbers;
  std::cin >> numbers.data();
  int sum = 0;
  for (auto ascii_number : numbers) {
    int number = ascii_number - '0';
    sum += number;
  }
  std::cout << sum << std::endl;
  return 0;
}