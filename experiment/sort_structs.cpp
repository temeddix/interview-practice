#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

struct MyStruct {
  int a;
  double b;
  std::string c;

  // Define the < operator for sorting
  bool operator<(const MyStruct& other) const {
    if (a != other.a) return a < other.a;
    if (b != other.b) return b < other.b;
    return c < other.c;
  }
};

int main() {
  std::vector<MyStruct> vec = {
      {2, 3.0, "apple"},
      {3, 1.5, "cherry"},
      {1, 2.5, "banana"},
  };
  std::sort(vec.begin(), vec.end());

  // Output the sorted vector for verification
  for (const MyStruct& elem : vec) {
    std::cout << elem.a << ", " << elem.b << ", " << elem.c << std::endl;
  }

  return 0;
}
