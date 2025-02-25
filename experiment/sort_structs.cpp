#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

struct MyStruct {
  int a;
  double b;
  string c;
};

// Define the < operator outside the struct.
// Putting the function inside the struct is also possible.
auto operator<(const MyStruct& lhs, const MyStruct& rhs) -> bool {
  if (lhs.a != rhs.a) {
    return lhs.a < rhs.a;
  }
  if (lhs.b != rhs.b) {
    return lhs.b < rhs.b;
  }
  return lhs.c < rhs.c;
}

auto operator<<(ostream& out, const MyStruct& obj) -> ostream& {
  out << obj.a << ", " << obj.b << ", " << obj.c;
  return out;
}

const vector<MyStruct> given = {
    {2, 3.0, "apple"},
    {3, 1.5, "cherry"},
    {1, 2.5, "banana"},
};

auto main() -> int {
  vector<MyStruct> vec = given;
  sort(vec.begin(), vec.end());

  // Output the sorted vector for verification.
  for (const MyStruct& elem : vec) {
    cout << elem << '\n';
  }
}
