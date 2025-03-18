#include <iostream>
#include <vector>

using namespace std;

constexpr int POWER_LIMIT = 20;  // 2^20 > 1,000,000
constexpr int MOD = 1'000'000'000;

auto find_combinations(int number) -> int {
  // First index means the number,
  // and the second index means the power of smallest element in combination.
  vector<vector<int>> dp_array(number + 1, vector(POWER_LIMIT, 0));

  for (int curr = 1; curr <= number; curr++) {
    int back_power = 0;
    while (1 << back_power < curr) {
      int dist = 1 << back_power;
      for (int ref_power = back_power; ref_power < POWER_LIMIT; ref_power++) {
        dp_array[curr][back_power] += dp_array[curr - dist][ref_power];
        dp_array[curr][back_power] %= MOD;
      }
      back_power += 1;
    }
    if (1 << back_power == curr) {
      dp_array[curr][back_power] += 1;
      dp_array[curr][back_power] %= MOD;
    }
  }

  int final_sum = 0;
  for (int count : dp_array.back()) {
    final_sum += count;
    final_sum %= MOD;
  }
  return final_sum;
}

auto main() -> int {
  int number = 0;
  cin >> number;
  cout << find_combinations(number) << '\n';
}