#include <algorithm>
#include <iostream>
#include <numeric>
#include <vector>

using namespace std;

const int HOR_ALL = 0;
const int VER_UP_END = 1;
const int VER_DN_END = 2;
const int VER_UP_GO = 3;
const int VER_DN_GO = 4;

const int SITUATIONS = 5;

auto count_possibilities(int columns) -> int {
  if (columns % 2 == 1) {
    return 0;
  }

  vector<int> prev_record(SITUATIONS, 1);
  vector<int> curr_record(SITUATIONS, 0);

  int blocks = columns / 2;
  for (int i = 1; i < blocks; i++) {
    vector<int> to_sum;
    to_sum = {
        prev_record[HOR_ALL],
        prev_record[VER_UP_END],
        prev_record[VER_DN_END],
    };
    curr_record[HOR_ALL] = accumulate(to_sum.begin(), to_sum.end(), 0);
    to_sum = {
        prev_record[HOR_ALL],
        prev_record[VER_UP_END],
        prev_record[VER_DN_END],
        prev_record[VER_UP_GO],
    };
    curr_record[VER_UP_END] = accumulate(to_sum.begin(), to_sum.end(), 0);
    to_sum = {
        prev_record[HOR_ALL],
        prev_record[VER_UP_END],
        prev_record[VER_DN_END],
        prev_record[VER_DN_GO],
    };
    curr_record[VER_DN_END] = accumulate(to_sum.begin(), to_sum.end(), 0);
    to_sum = {
        prev_record[HOR_ALL],
        prev_record[VER_UP_END],
        prev_record[VER_DN_END],
        prev_record[VER_UP_GO],
    };
    curr_record[VER_UP_GO] = accumulate(to_sum.begin(), to_sum.end(), 0);
    to_sum = {
        prev_record[HOR_ALL],
        prev_record[VER_UP_END],
        prev_record[VER_DN_END],
        prev_record[VER_DN_GO],
    };
    curr_record[VER_DN_GO] = accumulate(to_sum.begin(), to_sum.end(), 0);
    swap(prev_record, curr_record);
  }

  vector<int> to_sum = {
      prev_record[HOR_ALL],
      prev_record[VER_UP_END],
      prev_record[VER_DN_END],
  };
  return accumulate(to_sum.begin(), to_sum.end(), 0);
}

auto main() -> int {
  int columns = 0;
  cin >> columns;
  int possibilities = count_possibilities(columns);
  cout << possibilities << '\n';
}