#include <cmath>
#include <iostream>
#include <vector>

class Stats {
 private:
  std::vector<int> occurences;
  int count = 0;

 public:
  Stats() : occurences(8001) {
    for (int i = 0; i < 8001; i++) {
      occurences.push_back(0);
    }
  }

  void write(int value) {
    occurences[value + 4000] += 1;
    count += 1;
  }

  int average() {
    int sum = 0;
    for (int i = 0; i < 8001; i++) {
      sum += occurences[i] * (i - 4000);
    }
    return std::round(double(sum) / double(count));
  }

  int median() {
    int previous = 0;
    int until = count / 2;
    int number = -4000;
    while (true) {
      previous += occurences[number + 4000];
      if (previous > until) {
        break;
      }
      number += 1;
    }
    return number;
  }

  int mode() {
    int previous_max = 0;
    std::vector<int> numbers;
    numbers.push_back(-4000);
    for (int i = 0; i < 8001; i++) {
      if (occurences[i] > previous_max) {
        numbers.clear();
        numbers.push_back(i - 4000);
        previous_max = occurences[i];
      } else if (occurences[i] == previous_max) {
        if (numbers.size() < 2) {
          numbers.push_back(i - 4000);
        }
      }
    }
    return numbers.back();
  }

  int range() {
    int min = -4000;
    int max = 4000;
    for (int i = 0; i < 8001; i++) {
      if (occurences[i] > 0) {
        min = i - 4000;
        break;
      }
    }
    for (int i = 0; i < 8001; i++) {
      if (occurences[8000 - i] > 0) {
        max = -i + 4000;
        break;
      }
    }
    return max - min;
  }
};

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(NULL);
  std::cout.tie(NULL);

  int count;
  std::cin >> count;

  Stats stats = Stats();
  for (int i = 0; i < count; i++) {
    int number;
    std::cin >> number;
    stats.write(number);
  }

  std::cout << stats.average() << '\n';
  std::cout << stats.median() << '\n';
  std::cout << stats.mode() << '\n';
  std::cout << stats.range() << '\n';
}