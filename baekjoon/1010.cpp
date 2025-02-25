#include <iostream>
#include <numeric>  // for `std::gcd`
#include <vector>

auto get_combinations(int all, int picks) -> int {
  int result = 1;
  int high_side = all;
  int low_side = 1;
  for (int i = 0; i < picks; i++) {
    result *= high_side;
    high_side -= 1;
    result /= low_side;
    low_side += 1;
  }
  return result;
}

auto main() -> int {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);
  std::cout.tie(nullptr);

  int count = 0;
  std::cin >> count;

  for (int i = 0; i < count; i++) {
    int n = 0;
    int m = 0;
    std::cin >> n >> m;
    int possibilities = get_combinations(m, n);
    std::cout << possibilities << '\n';
  }
}