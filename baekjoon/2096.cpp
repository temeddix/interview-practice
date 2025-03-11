#include <algorithm>
#include <array>
#include <iostream>

using namespace std;

constexpr int COLUMN_COUNT = 3;

struct Records {
  array<int, COLUMN_COUNT> prev_min;
  array<int, COLUMN_COUNT> curr_min;
  array<int, COLUMN_COUNT> prev_max;
  array<int, COLUMN_COUNT> curr_max;
};

void update_min_score(array<int, COLUMN_COUNT>& row, Records& records) {
  array<int, COLUMN_COUNT>& prev_record = records.prev_min;
  array<int, COLUMN_COUNT>& curr_record = records.curr_min;
  curr_record[0] = min(prev_record[0], prev_record[1]) + row[0];
  curr_record[1] =
      min({prev_record[0], prev_record[1], prev_record[2]}) + row[1];
  curr_record[2] = min(prev_record[1], prev_record[2]) + row[2];
  prev_record = curr_record;
}

void update_max_score(array<int, COLUMN_COUNT>& row, Records& records) {
  array<int, COLUMN_COUNT>& prev_record = records.prev_max;
  array<int, COLUMN_COUNT>& curr_record = records.curr_max;
  curr_record[0] = max(prev_record[0], prev_record[1]) + row[0];
  curr_record[1] =
      max({prev_record[0], prev_record[1], prev_record[2]}) + row[1];
  curr_record[2] = max(prev_record[1], prev_record[2]) + row[2];
  prev_record = curr_record;
}

auto main() -> int {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  Records records{};

  int row_count = 0;
  cin >> row_count;
  array<int, COLUMN_COUNT> row{};
  for (int i = 0; i < row_count; i++) {
    for (int& number : row) {
      cin >> number;
    }
    update_min_score(row, records);
    update_max_score(row, records);
  }

  int min_score =
      *min_element(records.prev_min.begin(), records.prev_min.end());
  int max_score =
      *max_element(records.prev_max.begin(), records.prev_max.end());
  cout << max_score << ' ' << min_score << '\n';
}