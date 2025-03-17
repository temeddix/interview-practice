#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

auto find_longest_common(string& str_a, string& str_b) -> int {
  int a_len = static_cast<int>(str_a.size());
  int b_len = static_cast<int>(str_b.size());

  int longest = 0;
  vector<vector<int>> dp_array(a_len + 1, vector(b_len + 1, 0));
  for (int i = 0; i < a_len; i++) {
    for (int j = 0; j < b_len; j++) {
      if (str_a[i] == str_b[j]) {
        int current = dp_array[i][j] + 1;
        dp_array[i + 1][j + 1] = current;
        longest = max(longest, current);
      }
    }
  }

  return longest;
}

auto main() -> int {
  string str_a;
  string str_b;
  cin >> str_a >> str_b;
  cout << find_longest_common(str_a, str_b) << '\n';
}