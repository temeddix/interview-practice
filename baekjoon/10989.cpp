#include <array>
#include <iostream>

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(0);

  int count;
  std::cin >> count;

  std::array<int, 10000> occurrences;
  occurrences.fill(0);
  for (int i = 0; i < count; i++) {
    int number;
    std::cin >> number;
    occurrences[number - 1] += 1;
  }

  for (int i = 0; i < 10000; i++) {
    int occurence = occurrences[i];
    for (int j = 0; j < occurence; j++) {
      std::cout << i + 1 << '\n';
    }
  }

  return 0;
}