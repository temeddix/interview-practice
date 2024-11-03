#include <iostream>
#include <numeric>  // for `std::gcd`
#include <vector>

typedef long long int i64;

i64 get_c_combination(int all, int picks) {
  std::vector<int> numerators, denominators;

  // Fill numerators (all! / (all - picks)!)
  for (int i = all - picks + 1; i <= all; ++i) {
    numerators.push_back(i);
  }

  // Fill denominators (picks!)
  for (int i = 1; i <= picks; ++i) {
    denominators.push_back(i);
  }

  for (int& denom : denominators) {
    for (int& num : numerators) {
      int gcd = std::gcd(num, denom);
      if (gcd > 1) {
        num /= gcd;
        denom /= gcd;
      }
      if (denom == 1) break;
    }
  }

  i64 result = 1;
  for (i64 num : numerators) {
    result *= num;
  }

  return result;
}

int main() {
  int count;
  std::cin >> count;

  for (int i = 0; i < count; i++) {
    int n, m;
    std::cin >> n >> m;
    i64 possibilities = get_c_combination(m, n);
    std::cout << possibilities << '\n';
  }

  return 0;
}