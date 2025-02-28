#include <iostream>

using namespace std;

struct RowStatus {
  int empty;
  int placed_left;
  int placed_right;
};

constexpr int MOD = 9901;

auto count_possibilities(int rows) -> int {
  RowStatus last_row = {1, 0, 0};
  for (int i = 0; i < rows; i++) {
    RowStatus curr_row = {
        (last_row.empty + last_row.placed_left + last_row.placed_right) % MOD,
        (last_row.empty + last_row.placed_right) % MOD,
        (last_row.empty + last_row.placed_left) % MOD};
    last_row = curr_row;
  }

  return (last_row.empty + last_row.placed_left + last_row.placed_right) % MOD;
}

auto main() -> int {
  int rows = 0;
  cin >> rows;
  cout << count_possibilities(rows) << '\n';
}