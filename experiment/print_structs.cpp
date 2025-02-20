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

ostream& operator<<(ostream& os, const InnerStruct& obj) {
  os << "InnerStruct(x: " << obj.x << ", y: " << obj.y << ")";
  return os;
}

ostream& operator<<(ostream& os, const OuterStruct obj) {
  os << "OuterStruct(a: " << obj.a << ", b: " << obj.b << ")";
  return os;
}

int main() {
  OuterStruct obj = {true, {3, 5.5}};
  cout << obj << endl;
}