#include <iostream>

void find_x_y(int& x, int& y) {
  int a, b, c, d, e, f;
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

int main() {
  int x, y;
  find_x_y(x, y);

  std::cout << x << ' ' << y << std::endl;
  return 0;
}