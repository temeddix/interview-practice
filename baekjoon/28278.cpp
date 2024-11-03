#include <iostream>
#include <vector>

class IntStack {
 private:
  std::vector<int> data;

 public:
  void add(int value) { data.push_back(value); }

 public:
  int pop() {
    int data_size = data.size();
    if (data_size) {
      int last_item = data[data_size - 1];
      data.pop_back();
      return last_item;
    } else {
      return -1;
    }
  }

  int length() { return data.size(); }

  bool is_empty() { return data.size() == 0; }

  int get_last() {
    int data_size = data.size();
    if (data_size) {
      return data[data_size - 1];
    } else {
      return -1;
    }
  }
};

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(NULL);
  std::cout.tie(NULL);

  int count = 0;
  std::cin >> count;

  IntStack int_stack = IntStack();
  for (int i = 0; i < count; i++) {
    int command;
    std::cin >> command;
    if (command == 1) {
      int value;
      std::cin >> value;
      int_stack.add(value);
    } else if (command == 2) {
      std::cout << int_stack.pop() << '\n';
    } else if (command == 3) {
      std::cout << int_stack.length() << '\n';
    } else if (command == 4) {
      std::cout << (int_stack.is_empty() ? 1 : 0) << '\n';
    } else {
      std::cout << int_stack.get_last() << '\n';
    }
  }

  return 0;
}