#include <iostream>

auto main() -> int {
  int n = 0;
  std::cin >> n;

  int least_bags = -1;
  for (int i = n / 5; i >= 0; i--) {
    // `i` is the 5kg bag count
    int leftover_bags = (n - (i * 5));
    if (leftover_bags % 3 == 0) {
      least_bags = i + leftover_bags / 3;
      break;
    }
  }

  std::cout << least_bags << '\n';
}