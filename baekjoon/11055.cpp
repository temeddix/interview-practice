#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

const int MAX_NUMBER = 1000;

auto find_biggest(vector<int>& numbers) -> int {
  vector<int> record(MAX_NUMBER + 1, 0);

  for (int number : numbers) {
    int max_prev = 0;
    for (int i = 0; i < number; i++) {
      max_prev = max(max_prev, record[i]);
    }
    int new_sum = max_prev + number;
    record[number] = max(record[number], new_sum);
  }

  return *max_element(record.begin(), record.end());
}

auto main() -> int {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  int number_count = 0;
  cin >> number_count;

  vector<int> numbers;
  numbers.reserve(number_count);
  for (int i = 0; i < number_count; i++) {
    int number = 0;
    cin >> number;
    numbers.push_back(number);
  }

  int biggest = find_biggest(numbers);
  cout << biggest << '\n';
}