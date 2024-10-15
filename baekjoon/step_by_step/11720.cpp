#include <iostream>

int main() {
  int count;
  std::cin >> count;
  char numbers[1000];
  std::cin >> numbers;
  int sum = 0;
  for (int i = 0; i < count; i++) {
    int number = static_cast<int>(numbers[i]) - static_cast<int>('0');
    sum += number;
  }
  std::cout << sum << std::endl;
  return 0;
}