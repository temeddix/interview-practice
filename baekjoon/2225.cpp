#include <iostream>
#include <vector>

using namespace std;

struct Input {
  int number;
  int picks;
};

constexpr int MOD = 1000000000;

auto count_sum_methods(Input input) -> int {
  vector<int> prev_record(input.number + 1, 1);
  vector<int> curr_record(input.number + 1, 1);

  for (int i = 1; i < input.picks; i++) {
    int prev_methods = 1;
    for (int sum_value = 1; sum_value <= input.number; sum_value++) {
      prev_methods = (prev_methods + prev_record[sum_value]) % MOD;
      curr_record[sum_value] = prev_methods;
    }
    swap(prev_record, curr_record);
  }

  return prev_record.back();
}

auto main() -> int {
  int number = 0;
  int picks = 0;
  cin >> number >> picks;
  cout << count_sum_methods({number, picks}) << '\n';
}