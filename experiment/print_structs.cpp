#include <iostream>

using namespace std;

struct InnerStruct {
  int x;
  double y;
};

struct OuterStruct {
  bool a;
  InnerStruct b;
};

auto operator<<(ostream& out, const InnerStruct& obj) -> ostream& {
  out << "InnerStruct(x: " << obj.x << ", y: " << obj.y << ")";
  return out;
}

auto operator<<(ostream& out, const OuterStruct& obj) -> ostream& {
  out << "OuterStruct(a: " << obj.a << ", b: " << obj.b << ")";
  return out;
}

const OuterStruct obj = {true, {3, 5.5}};

auto main() -> int { cout << obj << '\n'; }