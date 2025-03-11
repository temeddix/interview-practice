#include <algorithm>
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

constexpr int COLUMN_COUNT = 3;

struct Records {
  vector<int> prev_min;
  vector<int> curr_min;
  vector<int> prev_max;
  vector<int> curr_max;
};

void update_min_score(vector<int>& row, Records& records) {
  vector<int>& prev_record = records.prev_min;
  vector<int>& curr_record = records.curr_min;
  curr_record[0] = min(prev_record[0], prev_record[1]) + row[0];
  curr_record[1] =
      *min_element(prev_record.begin(), prev_record.end()) + row[1];
  curr_record[2] = min(prev_record[1], prev_record[2]) + row[2];
  swap(prev_record, curr_record);
}

void update_max_score(vector<int>& row, Records& records) {
  vector<int>& prev_record = records.prev_max;
  vector<int>& curr_record = records.curr_max;
  curr_record[0] = max(prev_record[0], prev_record[1]) + row[0];
  curr_record[1] =
      *max_element(prev_record.begin(), prev_record.end()) + row[1];
  curr_record[2] = max(prev_record[1], prev_record[2]) + row[2];
  swap(prev_record, curr_record);
}

auto main() -> int {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  Records records = {
      vector<int>(COLUMN_COUNT, 0),
      vector<int>(COLUMN_COUNT, 0),
      vector<int>(COLUMN_COUNT, 0),
      vector<int>(COLUMN_COUNT, 0),
  };

  int row_count = 0;
  cin >> row_count;
  vector<int> row(COLUMN_COUNT, 0);
  for (int i = 0; i < row_count; i++) {
    for (int j = 0; j < COLUMN_COUNT; j++) {
      int number = 0;
      cin >> number;
      row[j] = number;
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