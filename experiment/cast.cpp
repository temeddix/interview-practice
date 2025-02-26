#include <iostream>

using namespace std;

class Base {};
class Derived : public Base {};
class Unrelated {};  // An unrelated class

auto main() -> int {
  // Convert char to int
  unsigned char my_char = '5';
  int char_to_int = static_cast<int>(my_char);
  cout << "char to int: " << char_to_int << '\n';
  // Outputs: 5

  // // Static cast (will cause a compile-time error)
  // Derived derived;
  // Unrelated* ptr =
  //     static_cast<Unrelated*>(&derived);  // Error: invalid static_cast

  // // C-style cast (will compile, but is unsafe)
  // Derived derived;
  // auto* ptr2 =
  //     (Unrelated*)&derived;  // Compiles, but leads to undefined behavior

  // // C-style cast (will cause a compile-time error)
  // Derived derived;
  // Unrelated ptr3 = Unrelated(derived);  // Error: no matching function
}
