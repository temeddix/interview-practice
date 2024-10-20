#include <array>
#include <iostream>

int main() {
  double weighted_grade_sum = 0.0;
  double weight_sum = 0.0;

  for (int i = 0; i < 20; i++) {
    std::array<char, 51> lecture;
    double weight;
    std::array<char, 3> human_grade;
    std::cin >> lecture.data() >> weight >> human_grade.data();

    double grade;
    if (human_grade[0] == 'A') {
      grade = 4.0;
    } else if (human_grade[0] == 'B') {
      grade = 3.0;
    } else if (human_grade[0] == 'C') {
      grade = 2.0;
    } else if (human_grade[0] == 'D') {
      grade = 1.0;
    } else if (human_grade[0] == 'F') {
      grade = 0.0;
    } else {
      continue;
    }
    if (grade != 0.0 && human_grade[1] == '+') {
      grade += 0.5;
    }

    weighted_grade_sum += weight * grade;
    weight_sum += weight;
  }

  double average_grade = weighted_grade_sum / weight_sum;
  std::cout << average_grade << std::endl;

  return 0;
}