#include <array>
#include <iostream>
#include <vector>

using namespace std;

struct Board {
  int size;
  vector<vector<int>> numbers;
};

struct Diff {
  int row;
  int col;
};

const array<Diff, 2> DIFFS = {{{1, 0}, {0, 1}}};

auto count_paths(Board& board) -> int64_t {
  vector<vector<int64_t>> paths(board.size, vector<int64_t>(board.size, 0));
  paths[0][0] = 1;

  for (int row = 0; row < board.size; row++) {
    for (int col = 0; col < board.size; col++) {
      int64_t path_found = paths[row][col];
      int jump = board.numbers[row][col];
      for (Diff diff : DIFFS) {
        int r_next = row + (diff.row * jump);
        int c_next = col + (diff.col * jump);
        if (r_next < 0 || r_next >= board.size) {
          continue;
        }
        if (c_next < 0 || c_next >= board.size) {
          continue;
        }
        paths[r_next][c_next] += path_found;
      }
    }
  }

  return paths.back().back();
}

auto main() -> int {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  int board_size = 0;
  cin >> board_size;

  vector<vector<int>> numbers(board_size, vector<int>(board_size, 0));
  for (int row = 0; row < board_size; row++) {
    for (int col = 0; col < board_size; col++) {
      int number = 0;
      cin >> number;
      numbers[row][col] = number;
    }
  }
  numbers[board_size - 1][board_size - 1] = 1;

  Board board = {board_size, numbers};
  cout << count_paths(board) << '\n';
}