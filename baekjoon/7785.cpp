#include <iostream>
#include <set>
#include <string>

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(NULL);
  std::cout.tie(NULL);

  int log_count;
  std::cin >> log_count;
  std::set<std::string, std::greater<>> people_working;
  for (int i = 0; i < log_count; i++) {
    std::string name, action;
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