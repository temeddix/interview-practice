#include <iostream>
#include <ostream>
#include <vector>

using namespace std;

constexpr int MOD = 1'000'000'000;

auto find_combinations(int number) -> int {
  vector<int> dp_array(number + 1, 0);
  dp_array[0] = 1;

  for (int curr = 1; curr <= number; curr++) {
    int count = dp_array[curr - 1];
    if (curr % 2 == 0) {
      count += dp_array[curr / 2];
      count %= MOD;
    }
    dp_array[curr] = count;
  }

  return dp_array.back();
}

auto main() -> int {
  int number = 0;
  cin >> number;
  cout << find_combinations(number) << '\n';
}