#include <iostream>
#include <unordered_map>

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(NULL);
  std::cout.tie(NULL);

  int count;
  std::cin >> count;
  std::unordered_map<int, int> occurences;
  for (int i = 0; i < count; i++) {
    int number;
    std::cin >> number;
    if (!occurences.count(number)) {
      occurences[number] = 0;
    }
    occurences[number] += 1;
  }

  int check;
  std::cin >> check;
  for (int i = 0; i < check; i++) {
    int number;
    std::cin >> number;
    std::cout << occurences[number] << ' ';
  }
}