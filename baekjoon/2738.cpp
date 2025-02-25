#include <array>
#include <iostream>

using Array2d = std::array<std::array<int, 100>, 100>;

Array2d create_array(int rows, int columns) {
  Array2d array;
  for (int i = 0; i < rows; i++) {
    for (int j = 0; j < columns; j++) {
      std::cin >> array[i][j];
    }
  }
  return array;
}

int main() {
  int rows, columns;
  std::cin >> rows >> columns;

  Array2d array_a = create_array(rows, columns);
  Array2d array_b = create_array(rows, columns);

  for (int i = 0; i < rows; i++) {
    for (int j = 0; j < columns; j++) {
      std::cout << array_a[i][j] + array_b[i][j];
      if (j < columns - 1) {
        std::cout << ' ';
      }
    }
    std::cout << '\n';
  }
}