#include <iostream>
#include <vector>

int main() {
  std::vector<std::vector<bool>> paper;
  for (int i = 0; i < 100; i++) {
    std::vector<bool> row = std::vector(100, false);
    paper.push_back(row);
  }

  int repeat;
  std::cin >> repeat;
  for (int i = 0; i < repeat; i++) {
    int left, bottom;
    std::cin >> left >> bottom;
    for (int j = 0; j < 10; j++) {
      for (int k = 0; k < 10; k++) {
        paper[j + bottom][k + left] = true;
      }
    }
  }

  int area = 0;
  for (int i = 0; i < 100; i++) {
    for (int j = 0; j < 100; j++) {
      bool is_filled = paper[i][j];
      if (is_filled) {
        area += 1;
      }
    }
  }

  std::cout << area << std::endl;
}