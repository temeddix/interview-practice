#include <algorithm>
#include <iostream>

int main() {
  int numbers[5];

  int sum = 0;
  for (int i = 0; i < 5; i++) {
    int number;
    std::cin >> number;
    sum += number;
    numbers[i] = number;
  }

  std::sort(numbers, numbers + 5);
  int middle = numbers[2];
  int average = sum / 5;

  std::cout << average << '\n' << middle << std::endl;
  return 0;
}