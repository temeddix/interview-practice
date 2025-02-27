#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

auto get_min_operations(int number) -> int {
  vector<int> record(2, 0);
  record.reserve(number + 1);

  for (int i = 2; i <= number; i++) {
    int operations = record[i - 1] + 1;
    if (i % 3 == 0) {
      operations = min(operations, record[i / 3] + 1);
    }
    if (i % 2 == 0) {
      operations = min(operations, record[i / 2] + 1);
    }
    record.push_back(operations);
  }

  return record.back();
}

auto main() -> int {
  int number = 0;
  cin >> number;
  cout << get_min_operations(number) << '\n';
}