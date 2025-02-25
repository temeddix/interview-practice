#include <algorithm>
#include <iostream>
#include <vector>

auto main() -> int {
  int students = 0;
  int rewarded = 0;
  std::cin >> students >> rewarded;

  std::vector<int> scores;
  scores.reserve(1000);

  for (int i = 0; i < students; i++) {
    int number = 0;
    std::cin >> number;
    scores.push_back(number);
  }

  // Same as using `std::greater`.
  std::sort(scores.begin(), scores.end(), [](int a, int b) { return a > b; });
  int cutline = scores[rewarded - 1];

  std::cout << cutline << '\n';
}