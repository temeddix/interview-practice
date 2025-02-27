#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

const int ELEMENT_COUNT = 6;
const int CHOOSE_COUNT = 3;

// Function to generate and print all combinations.
void generate_combinations(vector<int>& elements) {
  int size = static_cast<int>(elements.size());
  vector<bool> selector(elements.size(), false);
  fill(selector.begin(), selector.begin() + CHOOSE_COUNT, true);

  while (true) {
    for (int i = 0; i < size; ++i) {
      if (selector[i]) {
        cout << elements[i] << ' ';
      }
    }
    cout << '\n';
    if (!prev_permutation(selector.begin(), selector.end())) {
      break;
    }
  }
}

auto main() -> int {
  vector<int> elements(ELEMENT_COUNT);
  for (int i = 0; i < ELEMENT_COUNT; ++i) {
    elements[i] = i;
  }

  cout << "Combinations: " << '\n';
  generate_combinations(elements);

  return 0;
}