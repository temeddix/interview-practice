#include <iostream>
#include <vector>

using namespace std;

struct SeatPair {
  int smaller;
  int bigger;
};

struct SwapRecord {
  SeatPair pair;
  int fixed_cases;
  int swapped_cases;
};

void count_cases(vector<SwapRecord>& records, vector<bool> vip_seats) {
  int record_count = static_cast<int>(records.size());

  for (int i = 1; i < record_count; i++) {
    SwapRecord& prev_record = records[i - 1];
    SwapRecord& curr_record = records[i];
    SeatPair pair = curr_record.pair;
    curr_record.fixed_cases =
        prev_record.fixed_cases + prev_record.swapped_cases;
    if (!vip_seats[pair.smaller] && !vip_seats[pair.bigger]) {
      curr_record.swapped_cases = prev_record.fixed_cases;
    }
  }
}

auto main() -> int {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  int seat_count = 0;
  cin >> seat_count;

  if (seat_count == 1) {
    cout << 1 << '\n';
    return 0;
  }

  vector<SwapRecord> swap_records;
  for (int i = 1; i < seat_count; i++) {
    swap_records.push_back({{i - 1, i}, 0, 0});
  }

  int vip_count = 0;
  cin >> vip_count;
  vector<bool> vip_seats(seat_count, false);
  for (int i = 0; i < vip_count; i++) {
    int vip_seat = 0;
    cin >> vip_seat;
    vip_seats[vip_seat - 1] = true;
  }

  swap_records.front().fixed_cases = 1;
  if (!vip_seats[0] && !vip_seats[1]) {
    swap_records.front().swapped_cases = 1;
  }

  count_cases(swap_records, vip_seats);
  SwapRecord& last_record = swap_records.back();
  cout << last_record.fixed_cases + last_record.swapped_cases << '\n';
}