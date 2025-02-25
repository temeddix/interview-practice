#include <iostream>

using i64 = long long;

auto get_gcd(i64 a, i64 b) -> i64 {
  while (b != 0) {
    int temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}

auto get_lcm(i64 a, i64 b) -> i64 { return a * b / get_gcd(a, b); }

auto main() -> int {
  i64 a = 0;
  i64 b = 0;
  std::cin >> a >> b;
  std::cout << get_lcm(a, b) << '\n';
}