#include <iostream>

typedef long long int i64;

i64 get_gcd(i64 a, i64 b) {
  while (b != 0) {
    int temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}

i64 get_lcm(i64 a, i64 b) { return a * b / get_gcd(a, b); }

int main() {
  i64 a, b;
  std::cin >> a >> b;
  std::cout << get_lcm(a, b) << std::endl;
}