#include <iostream>

class Base {};
class Derived : public Base {};
class Unrelated {};  // An unrelated class

int main() {
  Derived derived;

  // Convert char to int
  char my_char = '5';
  int char_to_int = int(my_char);
  std::cout << "char to int: " << char_to_int << std::endl;
  // Outputs: 5

  //   // Static cast (will cause a compile-time error)
  //   Unrelated* ptr =
  //       static_cast<Unrelated*>(&derived);  // Error: invalid static_cast

  // C-style cast (will compile, but is unsafe)
  Unrelated* ptr2 =
      (Unrelated*)&derived;  // Compiles, but leads to undefined behavior

  //   // C-style cast (will cause a compile-time error)
  //   Unrelated ptr3 = Unrelated(derived);  // Error: no matching function

  return 0;
}
