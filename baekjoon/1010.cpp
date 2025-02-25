#include <iostream>

struct Setup {
  int all;
  int picks;
};

auto get_combinations(Setup setup) -> int {
  int result = 1;
  int high_side = setup.all;
  int low_side = 1;
  for (int i = 0; i < setup.picks; i++) {
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
    int num_n = 0;
    int num_m = 0;
    std::cin >> num_n >> num_m;
    int possibilities = get_combinations({num_m, num_n});
    std::cout << possibilities << '\n';
  }
}