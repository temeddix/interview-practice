#include <iostream>
#include <vector>

using namespace std;

int range = 10;
int divider = 1000000000;

int count_stair_numbers(int length) {
  vector<int> prev_count(range, 1);
  prev_count[0] = 0;
  vector<int> curr_count;
  curr_count.reserve(range);

  for (int i = 1; i < length; i++) {
    curr_count.push_back(prev_count[1] % divider);
    for (int j = 1; j < range - 1; j++) {
      curr_count.push_back((prev_count[j - 1] + prev_count[j + 1]) % divider);
    }
    curr_count.push_back(prev_count[range - 2] % divider);
    swap(prev_count, curr_count);
    curr_count.clear();
  }

  int final_sum = 0;
  for (int count : prev_count) {
    final_sum = (final_sum + count) % divider;
  }
  return final_sum;
}

int main() {
  int length;
  cin >> length;
  int stair_numbers = count_stair_numbers(length);
  cout << stair_numbers;
}