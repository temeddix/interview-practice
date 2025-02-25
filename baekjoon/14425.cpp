#include <iostream>
#include <string>
#include <unordered_set>

auto main() -> int {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);
  std::cout.tie(nullptr);

  int data_count = 0;
  int check_count = 0;
  std::cin >> data_count >> check_count;

  std::unordered_set<std::string> data;
  data.reserve(10000);
  for (int i = 0; i < data_count; i++) {
    std::string each_string;
    std::cin >> each_string;
    data.insert(each_string);
  }

  int checked = 0;
  for (int i = 0; i < check_count; i++) {
    std::string check_string;
    std::cin >> check_string;
    if (data.find(check_string) != data.end()) {
      checked += 1;
    }
  }

  std::cout << checked << '\n';
}