#include <algorithm>
#include <iostream>
#include <vector>

int main() {
  int students;
  std::cin >> students;

  std::vector<int> main_line;
  main_line.reserve(students);
  for (int i = 0; i < students; i++) {
    int number;
    std::cin >> number;
    main_line.push_back(number);
  }
  std::reverse(main_line.begin(), main_line.end());

  int last_enter = 0;
  std::vector<int> side_line;
  main_line.reserve(students);
  while (main_line.size() || side_line.size()) {
    // Try entring from the main line
    if (main_line.size()) {
      int main_back = main_line.back();
      if (main_back == last_enter + 1) {
        last_enter += 1;
        main_line.pop_back();
        continue;
      }
    }
    // Try entring from the side line
    if (side_line.size()) {
      int side_back = side_line.back();
      if (side_back == last_enter + 1) {
        last_enter += 1;
        side_line.pop_back();
        continue;
      }
    }
    // Move one student from main line to side line
    if (main_line.size()) {
      side_line.push_back(main_line.back());
      main_line.pop_back();
    } else {
      break;
    }
  }

  bool possible = !side_line.size() && !main_line.size();
  std::cout << (possible ? "Nice" : "Sad") << std::endl;
}