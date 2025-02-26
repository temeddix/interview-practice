#include <algorithm>
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

struct Streak {
  int zero;
  int one;
  int two;
};

const int INVALID = -1;

auto drink(vector<int>& glasses) -> int {
  Streak previous = {0, INVALID, INVALID};
  Streak current = {INVALID, INVALID, INVALID};

  for (int glass : glasses) {
    if (previous.one != INVALID) {
      current.two = previous.one + glass;
    }
    current.one = previous.zero + glass;
    current.zero = max({previous.zero, previous.one, previous.two});
    swap(previous, current);
    current = {INVALID, INVALID, INVALID};
  }

  return max({previous.zero, previous.one, previous.two});
}

auto main() -> int {
  int glass_count = 0;
  cin >> glass_count;
  vector<int> glasses;
  glasses.reserve(glass_count);
  for (int i = 0; i < glass_count; i++) {
    int glass = 0;
    cin >> glass;
    glasses.push_back(glass);
  }
  int drunk = drink(glasses);
  cout << drunk << '\n';
}