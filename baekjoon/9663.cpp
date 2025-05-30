#include <cmath>
#include <iostream>
#include <vector>

void count_possibilities(int row, int board_size, std::vector<int>& columns,
                         int& possibilities) {
  if (row == board_size) {
    possibilities++;
    return;
  }
  for (int col = 0; col < board_size; col++) {
    bool valid = true;
    for (int i = 0; i < row; i++) {
      if (columns[i] == col || std::abs(columns[i] - col) == row - i) {
        valid = false;
        break;
      }
    }
    if (valid) {
      columns[row] = col;  // Place the queen
      count_possibilities(row + 1, board_size, columns, possibilities);
    }
  }
}

auto main() -> int {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);
  std::cout.tie(nullptr);

  int board_size = 0;
  std::cin >> board_size;

  std::vector<int> columns;
  columns.reserve(board_size);
  int possibilities = 0;
  count_possibilities(0, board_size, columns, possibilities);
  std::cout << possibilities << '\n';
}