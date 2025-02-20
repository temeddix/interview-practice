#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

struct MyStruct {
  int a;
  double b;
  std::string c;
};

// Define the < operator outside the struct.
// Putting the function inside the struct is also possible.
bool operator<(const MyStruct& lhs, const MyStruct& rhs) {
  if (lhs.a != rhs.a) return lhs.a < rhs.a;
  if (lhs.b != rhs.b) return lhs.b < rhs.b;
  return lhs.c < rhs.c;
}

int main() {
  std::vector<MyStruct> vec = {
      {2, 3.0, "apple"},
      {3, 1.5, "cherry"},
      {1, 2.5, "banana"},
  };
  std::sort(vec.begin(), vec.end());

  // Output the sorted vector for verification.
  for (const MyStruct& elem : vec) {
    std::cout << elem.a << ", " << elem.b << ", " << elem.c << std::endl;
  }

  return 0;
}
