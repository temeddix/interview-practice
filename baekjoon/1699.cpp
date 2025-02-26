#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

const int INF = 1000000007;

auto find_min_term_count(int number) -> int {
  vector<int> record;
  record.reserve(number + 1);
  record.push_back(0);

  for (int i = 1; i <= number; i++) {
    int previous = INF;
    int behind = 1;
    while (behind * behind <= i) {
      previous = min(previous, record[i - (behind * behind)]);
      behind += 1;
    }
    record[i] = previous + 1;
  }

  return record[number];
}

auto main() -> int {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  int number = 0;
  cin >> number;

  int min_term_count = find_min_term_count(number);
  cout << min_term_count << '\n';
}