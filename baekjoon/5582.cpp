#include <algorithm>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

using namespace std;

auto find_longest_common(const string& str_a, const string& str_b) -> int {
  int a_len = static_cast<int>(str_a.size());
  int b_len = static_cast<int>(str_b.size());

  int longest = 0;
  vector<int> prev(b_len + 1, 0);
  vector<int> curr(b_len + 1, 0);

  for (int i = 0; i < a_len; i++) {
    for (int j = 0; j < b_len; j++) {
      if (str_a[i] == str_b[j]) {
        curr[j + 1] = prev[j] + 1;
        longest = max(longest, curr[j + 1]);
      } else {
        curr[j + 1] = 0;
      }
    }
    swap(prev, curr);
  }

  return longest;
}

auto main() -> int {
  string str_a;
  string str_b;
  cin >> str_a >> str_b;
  cout << find_longest_common(str_a, str_b) << '\n';
}