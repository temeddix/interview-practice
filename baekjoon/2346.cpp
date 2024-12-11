#include <iostream>
#include <vector>

class Ring : public std::vector<int> {
 private:
  int cursor = 0;

 public:
  int current_index() { return cursor; }

  int pop_written() {
    int written = (*this)[cursor];
    (*this)[cursor] = 0;
    return written;
  }

  void next() {
    do {
      cursor += 1;
      if (cursor == (*this).size()) {
        cursor = 0;
      }
    } while ((*this)[cursor] == 0);
  }

  void previous() {
    do {
      cursor -= 1;
      if (cursor == -1) {
        cursor = (*this).size() - 1;
      }
    } while ((*this)[cursor] == 0);
  }
};

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(NULL);
  std::cout.tie(NULL);

  int count;
  std::cin >> count;
  Ring ring;
  ring.reserve(count);
  for (int i = 0; i < count; i++) {
    int written;
    std::cin >> written;
    ring.push_back(written);
  }

  for (int i = 0; i < count; i++) {
    std::cout << ring.current_index() + 1 << ' ';
    int next_move = ring.pop_written();
    if (i == count - 1) {
      break;
    }
    if (next_move < 0) {
      for (int i = 0; i < -next_move; i++) {
        ring.previous();
      }
    } else {
      for (int i = 0; i < next_move; i++) {
        ring.next();
      }
    }
  }

  return 0;
}