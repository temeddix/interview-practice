#include <iostream>

void find_x_y(int& x, int& y) {
  int a = 0;
  int b = 0;
  int c = 0;
  int d = 0;
  int e = 0;
  int f = 0;
  std::cin >> a >> b >> c >> d >> e >> f;
  const int signs[2] = {-1, 1};

  // Start from 0 and increase the absolute value.
  // The probability of x and y being a simple integer looks high.
  for (int x_abs = 0; x_abs <= 999; x_abs++) {
    for (int y_abs = 0; y_abs <= 999; y_abs++) {
      for (int x_sign : signs) {
        for (int y_sign : signs) {
          int x_signed = x_abs * x_sign;
          int y_signed = y_abs * y_sign;
          bool is_first_satisfied = a * x_signed + b * y_signed == c;
          bool is_second_satisfied = d * x_signed + e * y_signed == f;
          if (is_first_satisfied && is_second_satisfied) {
            x = x_signed;
            y = y_signed;
            return;
          }
        }
      }
    }
  }
}

auto main() -> int {
  int x = 0;
  int y = 0;
  find_x_y(x, y);

  std::cout << x << ' ' << y << '\n';
}