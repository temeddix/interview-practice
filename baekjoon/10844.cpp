#include <iostream>
#include <vector>

using namespace std;

const int RANGE = 10;
const int DIVIDER = 1000000000;

auto count_stair_numbers(int length) -> int {
  vector<int> prev_count(RANGE, 1);
  prev_count[0] = 0;
  vector<int> curr_count;
  curr_count.reserve(RANGE);

  for (int i = 1; i < length; i++) {
    curr_count.push_back(prev_count[1] % DIVIDER);
    for (int j = 1; j < RANGE - 1; j++) {
      curr_count.push_back((prev_count[j - 1] + prev_count[j + 1]) % DIVIDER);
    }
    curr_count.push_back(prev_count[RANGE - 2] % DIVIDER);
    swap(prev_count, curr_count);
    curr_count.clear();
  }

  int final_sum = 0;
  for (int count : prev_count) {
    final_sum = (final_sum + count) % DIVIDER;
  }
  return final_sum;
}

auto main() -> int {
  int length = 0;
  cin >> length;
  int stair_numbers = count_stair_numbers(length);
  cout << stair_numbers;
}