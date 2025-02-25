#include <algorithm>
#include <iostream>
#include <vector>

auto main() -> int {
  int students = 0;
  std::cin >> students;

  std::vector<int> main_line;
  main_line.reserve(students);
  for (int i = 0; i < students; i++) {
    int number = 0;
    std::cin >> number;
    main_line.push_back(number);
  }
  std::reverse(main_line.begin(), main_line.end());

  int last_enter = 0;
  std::vector<int> side_line;
  main_line.reserve(students);
  while ((static_cast<unsigned int>(!main_line.empty()) != 0U) || (static_cast<unsigned int>(!side_line.empty()) != 0U)) {
    // Try entring from the main line
    if (static_cast<unsigned int>(!main_line.empty()) != 0U) {
      int main_back = main_line.back();
      if (main_back == last_enter + 1) {
        last_enter += 1;
        main_line.pop_back();
        continue;
      }
    }
    // Try entring from the side line
    if (static_cast<unsigned int>(!side_line.empty()) != 0U) {
      int side_back = side_line.back();
      if (side_back == last_enter + 1) {
        last_enter += 1;
        side_line.pop_back();
        continue;
      }
    }
    // Move one student from main line to side line
    if (static_cast<unsigned int>(!main_line.empty()) != 0U) {
      side_line.push_back(main_line.back());
      main_line.pop_back();
    } else {
      break;
    }
  }

  bool possible = side_line.empty() && main_line.empty();
  std::cout << (possible ? "Nice" : "Sad") << '\n';
}