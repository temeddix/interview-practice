#include <iostream>

class Base {};
class Derived : public Base {};
class Unrelated {};  // An unrelated class

int main() {
  Derived derived;

  //   // Static cast (will cause a compile-time error)
  //   Unrelated* ptr =
  //       static_cast<Unrelated*>(&derived);  // Error: invalid static_cast

  // C-style cast (will compile, but is unsafe)
  Unrelated* ptr2 =
      (Unrelated*)&derived;  // Compiles, but leads to undefined behavior

  //   // C-style cast (will cause a compile-time error)
  //   Unrelated ptr3 =
  //       Unrelated(derived);  // Compiles, but leads to undefined behavior

  return 0;
}
