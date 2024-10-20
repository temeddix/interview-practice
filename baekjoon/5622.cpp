#include <array>
#include <iostream>
#include <string>

int main() {
  // Get the input
  std::string alphabets;
  std::cin >> alphabets;
  int length = alphabets.size();

  // Collect numbers
  // Each number would be one of 2~9
  std::array<char, 15> numbers;
  for (int i = 0; i < length; i++) {
    char alphabet = alphabets[i];
    char number = 2;
    char criterion = 'A';
    for (int j = 0; j < 7; j++) {
      if (number < 7) {
        criterion += 3;
      } else if (number == 7) {
        criterion += 4;
      } else if (number == 8) {
        criterion += 3;
      }
      if (alphabet < criterion) {
        break;
      }
      number += 1;
    }
    numbers[i] = number;
  }

  // Calculate dialing time
  int min_time = 0;
  for (int i = 0; i < length; i++) {
    int number = numbers[i];
    min_time += number + 1;
  }

  // Print the output
  std::cout << min_time << std::endl;

  return 0;
}