#include <iostream>
#include <vector>

using namespace std;

struct Spot {
  int row;
  int column;
};

auto create_sum_table(vector<vector<int>>& numbers) -> vector<vector<int>> {
  int table_size = static_cast<int>(numbers.size());
  vector<vector<int>> sum_table(table_size + 1, vector<int>(table_size + 1, 0));

  for (int i = 0; i < table_size; i++) {
    for (int j = 0; j < table_size; j++) {
      int previous_sum =
          sum_table[i + 1][j] + sum_table[i][j + 1] - sum_table[i][j];
      int sum_value = previous_sum + numbers[i][j];
      sum_table[i + 1][j + 1] = sum_value;
    }
  }

  return sum_table;
}

auto get_sum(vector<vector<int>>& sum_table, Spot a_spot, Spot b_spot) -> int {
  return sum_table[b_spot.row][b_spot.column] +
         sum_table[a_spot.row - 1][a_spot.column - 1] -
         sum_table[a_spot.row - 1][b_spot.column] -
         sum_table[b_spot.row][a_spot.column - 1];
}

auto main() -> int {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  int table_size = 0;
  int command_count = 0;
  cin >> table_size >> command_count;

  vector<vector<int>> numbers;
  for (int i = 0; i < table_size; i++) {
    vector<int> row;
    row.reserve(table_size);
    for (int j = 0; j < table_size; j++) {
      int number = 0;
      cin >> number;
      row.push_back(number);
    }
    numbers.push_back(row);
  }

  vector<vector<int>> sum_table = create_sum_table(numbers);
  for (int i = 0; i < command_count; i++) {
    int a_row = 0;
    int a_column = 0;
    int b_row = 0;
    int b_column = 0;
    cin >> a_row >> a_column >> b_row >> b_column;
    cout << get_sum(sum_table, {a_row, a_column}, {b_row, b_column}) << '\n';
  }
}