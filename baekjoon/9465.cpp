
#include <algorithm>
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

const int ROW_COUNT = 2;
const int SITUATIONS = 3;

const int NONE_CHOSEN = 0;
const int UP_CHOSEN = 1;
const int DOWN_CHOSEN = 2;

auto find_max_score(vector<vector<int>>& rows) -> int {
  int column_count = static_cast<int>(rows[0].size());
  vector<int> prev_record(SITUATIONS, 0);
  vector<int> curr_record(SITUATIONS, 0);

  for (int column = 0; column < column_count; column++) {
    curr_record[NONE_CHOSEN] =
        *max_element(prev_record.begin(), prev_record.end());
    curr_record[UP_CHOSEN] =
        max(prev_record[NONE_CHOSEN], prev_record[DOWN_CHOSEN]) +
        rows[0][column];
    curr_record[DOWN_CHOSEN] =
        max(prev_record[NONE_CHOSEN], prev_record[UP_CHOSEN]) + rows[1][column];
    swap(prev_record, curr_record);
  }

  return *max_element(prev_record.begin(), prev_record.end());
}

auto main() -> int {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  int test_cases = 0;
  cin >> test_cases;

  for (int test = 0; test < test_cases; test++) {
    int column_count = 0;
    cin >> column_count;

    vector<vector<int>> rows;
    rows.reserve(column_count);
    for (int i = 0; i < ROW_COUNT; i++) {
      vector<int> row;
      row.reserve(column_count);
      for (int j = 0; j < column_count; j++) {
        int number = 0;
        cin >> number;
        row.push_back(number);
      }
      rows.push_back(row);
    }

    int max_score = find_max_score(rows);
    cout << max_score << '\n';
  }
}