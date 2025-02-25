#include <iostream>
#include <numeric>  // for `std::gcd`
#include <vector>

int get_combinations(int all, int picks) {
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

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(NULL);
  std::cout.tie(NULL);

  int count;
  std::cin >> count;

  for (int i = 0; i < count; i++) {
    int n, m;
    std::cin >> n >> m;
    int possibilities = get_combinations(m, n);
    std::cout << possibilities << '\n';
  }
}