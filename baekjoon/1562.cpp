#include <algorithm>
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

constexpr int BASE = 10;
constexpr int COMBINATIONS = 1 << BASE;
constexpr int MOD = 1'000'000'000;

auto count_stair_numbers(int digits) -> int {
  vector<vector<int>> dp_prev(BASE, vector(COMBINATIONS, 0));
  vector<vector<int>> dp_curr(BASE, vector(COMBINATIONS, 0));

  for (int end = 1; end < BASE; end++) {
    dp_prev[end][1 << end] = 1;
  }

  for (int i = 1; i < digits; i++) {
    for (int end = 0; end < BASE; end++) {
      for (int curr_comb = 0; curr_comb < COMBINATIONS; curr_comb++) {
        dp_curr[end][curr_comb] = 0;
      }
      for (int prev_comb = 0; prev_comb < COMBINATIONS; prev_comb++) {
        int curr_comb = prev_comb | (1 << end);
        if (end == 0) {
          dp_curr[end][curr_comb] += dp_prev[end + 1][prev_comb];
          dp_curr[end][curr_comb] %= MOD;
        } else if (end == BASE - 1) {
          dp_curr[end][curr_comb] += dp_prev[end - 1][prev_comb];
          dp_curr[end][curr_comb] %= MOD;
        } else {
          dp_curr[end][curr_comb] += dp_prev[end - 1][prev_comb];
          dp_curr[end][curr_comb] %= MOD;
          dp_curr[end][curr_comb] += dp_prev[end + 1][prev_comb];
          dp_curr[end][curr_comb] %= MOD;
        }
      }
    }
    swap(dp_prev, dp_curr);
  }

  int stair_numbers = 0;
  for (vector<int>& end_records : dp_prev) {
    stair_numbers += end_records.back();
    stair_numbers %= MOD;
  }

  return stair_numbers;
}

auto main() -> int {
  int digits = 0;
  cin >> digits;
  cout << count_stair_numbers(digits) << '\n';
}