#include <iostream>
#include <string>
#include <vector>

using namespace std;

struct InnerStruct {
  bool hi;
  string hihi;
};

struct MyStruct {
  vector<int> numbers;
  InnerStruct inner;
};

void called(MyStruct& my_struct) {
  MyStruct& reference = my_struct;
  cout << "CALLED" << '\n';
}

int main() {
  MyStruct my_struct = {{1, 2, 3, 4, 5}, {false, "hello"}};
  my_struct.numbers.push_back(6);
  called(my_struct);
  cout << "DONE" << '\n';
}