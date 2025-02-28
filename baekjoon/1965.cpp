#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

constexpr int MAX_BOX = 1000;

auto contain_max(vector<int>& boxes) -> int {
  // Index means the last box size, value means the streak length.
  vector<int> record(MAX_BOX + 1, 0);

  for (int box : boxes) {
    int prev_streak = *max_element(record.begin(), record.begin() + box);
    record[box] = max(record[box], prev_streak + 1);
  }

  return *max_element(record.begin(), record.end());
}

auto main() -> int {
  int box_count = 0;
  cin >> box_count;
  vector<int> boxes;
  boxes.reserve(box_count);
  for (int i = 0; i < box_count; i++) {
    int box = 0;
    cin >> box;
    boxes.push_back(box);
  }
  cout << contain_max(boxes) << '\n';
}