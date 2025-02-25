#include <algorithm>
#include <array>
#include <iostream>

int main() {
  int n, m;
  std::cin >> n >> m;

  std::array<std::array<bool, 50>, 50> board = {};
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      char letter = std::cin.get();
      while (letter == '\n') {
        letter = std::cin.get();
      }
      if (letter == 'W') {
        board[i][j] = true;
      } else {
        board[i][j] = false;
      }
    }
  }

  int min_mismatches = 32;
  for (int i = 0; i < n - 7; i++) {
    for (int j = 0; j < m - 7; j++) {
      int mismatches = 0;
      for (int k = 0; k < 8; k++) {
        for (int l = 0; l < 8; l++) {
          int cell_x = i + k;
          int cell_y = j + l;
          bool is_odd_cell = (cell_x + cell_y) % 2 == 1;
          if (board[cell_x][cell_y] != is_odd_cell) {
            mismatches += 1;
          }
        }
      }
      mismatches = std::min(mismatches, 64 - mismatches);
      if (mismatches < min_mismatches) {
        min_mismatches = mismatches;
      }
    }
  }

  std::cout << min_mismatches << std::endl;
}