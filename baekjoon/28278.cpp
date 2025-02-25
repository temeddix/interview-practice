#include <iostream>
#include <vector>

class IntStack {
 private:
  std::vector<int> data;

 public:
  void add(int value) { data.push_back(value); }

  auto pop() -> int {
    int data_size = data.size();
    if (data_size != 0) {
      int last_item = data[data_size - 1];
      data.pop_back();
      return last_item;
    }
    return -1;
  }

  auto length() -> int { return data.size(); }

  auto is_empty() -> bool { return data.empty(); }

  auto get_last() -> int {
    int data_size = data.size();
    if (data_size != 0) {
      return data[data_size - 1];
    }
    return -1;
  }
};

auto main() -> int {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);
  std::cout.tie(nullptr);

  int count = 0;
  std::cin >> count;

  IntStack int_stack = IntStack();
  for (int i = 0; i < count; i++) {
    int command = 0;
    std::cin >> command;
    switch (command) {
      case 1: {
        int value = 0;
        std::cin >> value;
        int_stack.add(value);
        break;
      }
      case 2: {
        std::cout << int_stack.pop() << '\n';
        break;
      }
      case 3: {
        std::cout << int_stack.length() << '\n';
        break;
      }
      case 4: {
        std::cout << (int_stack.is_empty() ? 1 : 0) << '\n';
        break;
      }
      case 5: {
        std::cout << int_stack.get_last() << '\n';
        break;
      }
      default: {
        break;
      }
    }
  }
}