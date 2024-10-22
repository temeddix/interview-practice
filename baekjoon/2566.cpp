#include <iostream>

int main() {
  int row = 0;
  int column = 0;
  int last_biggest = -1;

  for (int i = 0; i < 9; i++) {
    for (int j = 0; j < 9; j++) {
      int value;
      std::cin >> value;
      if (last_biggest < value) {
        last_biggest = value;
        row = i;
        column = j;
      }
    }
  }

  std::cout << last_biggest;
  std::cout << '\n' << row + 1 << ' ' << column + 1 << std::endl;

  return 0;
}