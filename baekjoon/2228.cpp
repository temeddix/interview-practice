#include <algorithm>
#include <iostream>
#include <ostream>
#include <utility>
#include <vector>

using namespace std;

constexpr int INVALID = -1'000'000'007;

struct Record {
  vector<int> used;
  vector<int> unused;
};

auto get_max_sum(vector<int>& sequence, int group_count) -> int {
  Record dp_prev = {vector(group_count + 1, INVALID),
                    vector(group_count + 1, INVALID)};
  dp_prev.unused[0] = 0;
  Record dp_curr = {vector(group_count + 1, INVALID),
                    vector(group_count + 1, INVALID)};
  dp_curr.unused[0] = 0;

  for (int number : sequence) {
    for (int groups = 1; groups <= group_count; groups++) {
      int curr_used = INVALID;
      int curr_unused = INVALID;
      if (dp_prev.used[groups] != INVALID) {
        curr_used = max(curr_used, dp_prev.used[groups] + number);
      }
      if (dp_prev.unused[groups - 1] != INVALID) {
        curr_used = max(curr_used, dp_prev.unused[groups - 1] + number);
      }
      curr_unused = max(curr_unused, dp_prev.used[groups]);
      curr_unused = max(curr_unused, dp_prev.unused[groups]);
      dp_curr.used[groups] = curr_used;
      dp_curr.unused[groups] = curr_unused;
    }
    swap(dp_prev, dp_curr);
  }

  return max(dp_prev.used.back(), dp_prev.unused.back());
}

auto main() -> int {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  int sequence_size = 0;
  int group_count = 0;
  cin >> sequence_size >> group_count;

  vector<int> sequence(sequence_size);
  for (int i = 0; i < sequence_size; i++) {
    cin >> sequence[i];
  }

  cout << get_max_sum(sequence, group_count) << '\n';
}