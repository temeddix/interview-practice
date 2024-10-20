#include <iostream>

void print_chars(const char letter, short repeat) {
  for (short i = 0; i < repeat; i++) {
    std::cout << letter;
  }
}

int main() {
  short number;
  std::cin >> number;

  short rows = number * 2 - 1;
  for (short i = 0; i < rows; i++) {
    short level;
    if (i < number) {
      level = i;
    } else {
      level = number * 2 - 2 - i;
    }
    short stars = level * 2 + 1;
    short spacing = number - level - 1;
    print_chars(' ', spacing);
    print_chars('*', stars);
    std::cout << '\n';
  }

  return 0;
}