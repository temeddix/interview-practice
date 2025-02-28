#include <iostream>
#include <string>

using namespace std;

struct Status {
  int finished;
  int unfinished;
};

constexpr int MOD = 1000000;
constexpr int TWENTY_LIMIT = 6;

auto count_possibilities(string& encrypted) -> int {
  Status prev_status = {1, 0};
  int prev_number = 0;
  for (char letter : encrypted) {
    int curr_number = letter - '0';
    bool can_continue = (curr_number == 1) || (curr_number == 2);
    Status curr_status = {
        (prev_status.finished + prev_status.unfinished) % MOD,
        can_continue ? prev_status.finished : 0,
    };
    if (curr_number == 0) {
      if (prev_status.unfinished == 0) {
        return 0;
      }
      curr_status = {prev_status.unfinished, 0};
    } else if (curr_number > TWENTY_LIMIT && prev_number == 2) {
      curr_status = {prev_status.finished, 0};
    }
    prev_status = curr_status;
    prev_number = curr_number;
  }
  return prev_status.finished % MOD;
}

auto main() -> int {
  string encrypted;
  cin >> encrypted;
  cout << count_possibilities(encrypted);
}