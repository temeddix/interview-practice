#include <iostream>
#include <string>
#include <vector>

using namespace std;

namespace {

#pragma pack(1)
struct InnerStruct {
  bool hi;
  string hihi;
};

struct MyStruct {
  vector<int> numbers;
  InnerStruct inner;
};

void called(const MyStruct& my_struct) {
  const MyStruct& reference = my_struct;
  reference.numbers;
  cout << "CALLED" << '\n';
}

}  // namespace

int main() {
  MyStruct my_struct = {{1, 2, 3, 4, 5}, {false, "hello"}};
  int vec_size = static_cast<int>(my_struct.numbers.size());
  cout << vec_size << '\n';
  my_struct.numbers.push_back(6);
  called(my_struct);
  cout << "DONE" << '\n';
}