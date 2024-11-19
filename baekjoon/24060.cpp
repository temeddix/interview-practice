#include <iostream>
#include <vector>

struct TurnInfo {
  int turn;
  int turn_goal;
  int number;
};

void merge(std::vector<int>& numbers, int from, int mid, int to,
           TurnInfo& turn_info) {
  int i = from;
  int j = mid;
  int len = to - from;
  std::vector<int> temp;
  temp.reserve(to - from);
  while (i < mid && j < to) {
    if (numbers[i] <= numbers[j]) {
      temp.push_back(numbers[i]);
      i += 1;
    } else {
      temp.push_back(numbers[j]);
      j += 1;
    }
  }
  // When the left half has leftovers
  while (i < mid) {
    temp.push_back(numbers[i]);
    i += 1;
  }
  // When the right half has leftovers
  while (j < to) {
    temp.push_back(numbers[j]);
    j += 1;
  }
  // Put the result into the original vector.
  for (int k = 0; k < len; k++) {
    numbers[from + k] = temp[k];
    turn_info.turn += 1;
    if (turn_info.turn == turn_info.turn_goal) {
      turn_info.number = temp[k];
    }
  }
}

void merge_sort(std::vector<int>& numbers, int from, int to,
                TurnInfo& turn_info) {
  if (from < to - 1) {
    int mid = (from + to + 1) / 2;
    merge_sort(numbers, from, mid, turn_info);
    merge_sort(numbers, mid, to, turn_info);
    merge(numbers, from, mid, to, turn_info);
  }
}

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(NULL);
  std::cout.tie(NULL);

  int size, turn_goal;
  std::cin >> size >> turn_goal;

  std::vector<int> numbers;
  numbers.reserve(size);
  for (int i = 0; i < size; i++) {
    int number;
    std::cin >> number;
    numbers.push_back(number);
  }
  TurnInfo turn_info = TurnInfo{0, turn_goal, -1};
  merge_sort(numbers, 0, size, turn_info);

  std::cout << turn_info.number << std::endl;
}