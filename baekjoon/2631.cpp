#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

auto find_longest_increasing_sequence(vector<int>& children) -> int {
  int children_count = static_cast<int>(children.size());
  vector<int> lis_record;
  lis_record.reserve(children_count);
  lis_record.push_back(children[0]);

  for (int i = 1; i < children_count; i++) {
    int child = children[i];
    int last_number = lis_record.back();
    if (last_number < child) {
      lis_record.push_back(child);
    } else {
      int new_index = static_cast<int>(
          lower_bound(lis_record.begin(), lis_record.end(), child) -
          lis_record.begin());
      lis_record[new_index] = min(lis_record[new_index], child);
    }
  }

  return static_cast<int>(lis_record.size());
}

auto main() -> int {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  int children_count = 0;
  cin >> children_count;

  vector<int> children(children_count);
  for (int i = 0; i < children_count; i++) {
    cin >> children[i];
  }

  int movements = children_count - find_longest_increasing_sequence(children);
  cout << movements << '\n';
}