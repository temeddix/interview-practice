#include <iostream>
#include <numeric>
#include <utility>
#include <vector>

using namespace std;

const int DIVIDER = 10007;
const int BASE = 10;

auto count_ascending_numbers(int digits) -> int {
  vector<int> prev_record(BASE, 1);
  vector<int> curr_record(BASE, 0);

  for (int i = 1; i < digits; i++) {
    for (int tail = 0; tail < BASE; tail++) {
      int count_sum = 0;
      for (int last = 0; last <= tail; last++) {
        count_sum += prev_record[last];
      }
      curr_record[tail] = count_sum % DIVIDER;
    }
    swap(prev_record, curr_record);
  }

  return accumulate(prev_record.begin(), prev_record.end(), 0) % DIVIDER;
}

auto main() -> int {
  int digits = 0;
  cin >> digits;
  int ascending_numbers = count_ascending_numbers(digits);
  cout << ascending_numbers << '\n';
}