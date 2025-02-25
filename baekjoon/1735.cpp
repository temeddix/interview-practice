#include <iostream>

int get_gcd(int a, int b) {
  while (b != 0) {
    int temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}

int get_lcm(int a, int b) { return a * b / get_gcd(a, b); }

class Fraction {
 public:
  int numerator;
  int denominator;

  static Fraction from_input() {
    int numerator, denominator;
    std::cin >> numerator >> denominator;
    return Fraction{
        numerator,
        denominator,
    };
  }

  Fraction scale_up(int by) const {
    const Fraction& self = *this;
    return Fraction{
        self.numerator * by,
        self.denominator * by,
    };
  }

  Fraction scale_down() const {
    const Fraction& self = *this;
    int gcd = get_gcd(self.numerator, self.denominator);
    return Fraction{
        self.numerator / gcd,
        self.denominator / gcd,
    };
  }

  Fraction operator+(const Fraction& other) const {
    const Fraction& self = *this;
    Fraction higher_self, higher_other;
    if (self.denominator != other.denominator) {
      int denominator_lcm = get_lcm(self.denominator, other.denominator);
      higher_self = self.scale_up(denominator_lcm / self.denominator);
      higher_other = other.scale_up(denominator_lcm / other.denominator);
    } else {
      higher_self = self;
      higher_other = other;
    }
    int higher_numerator = higher_self.numerator + higher_other.numerator;
    int higher_denominator = higher_self.denominator;
    Fraction higher_sum = Fraction{
        higher_numerator,
        higher_denominator,
    };
    return higher_sum.scale_down();
  }
};

int main() {
  Fraction fraction_a = Fraction::from_input();
  Fraction fraction_b = Fraction::from_input();
  Fraction sum = fraction_a + fraction_b;
  std::cout << sum.numerator << ' ' << sum.denominator << std::endl;
}