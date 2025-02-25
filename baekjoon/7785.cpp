#include <iostream>
#include <set>
#include <string>

auto main() -> int {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);
  std::cout.tie(nullptr);

  int log_count = 0;
  std::cin >> log_count;
  std::set<std::string, std::greater<>> people_working;
  for (int i = 0; i < log_count; i++) {
    std::string name;
    std::string action;
    std::cin >> name >> action;
    if (action == "enter") {
      people_working.insert(name);
    } else {
      people_working.erase(name);
    }
  }

  for (const std::string& name : people_working) {
    std::cout << name << '\n';
  }
}