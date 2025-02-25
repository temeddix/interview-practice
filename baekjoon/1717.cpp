#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

const int UNION_OP = 0;

struct ItemPair {
  int item_a;
  int item_b;
};

auto get_root(int item, vector<int>& items) -> int {
  if (items[item] != item) {
    items[item] = get_root(items[item], items);
  }
  return items[item];
}

void union_groups(ItemPair item_pair, vector<int>& items) {
  if (item_pair.item_a == item_pair.item_b) {
    return;
  }
  int root_a = get_root(item_pair.item_a, items);
  int root_b = get_root(item_pair.item_b, items);
  if (root_a < root_b) {
    items[root_b] = root_a;
  } else {
    items[root_a] = root_b;
  }
}

auto is_grouped(ItemPair item_pair, vector<int>& items) -> bool {
  return get_root(item_pair.item_a, items) == get_root(item_pair.item_b, items);
}

auto main() -> int {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  // Get the basic input.
  int item_count = 0;
  int operation_count = 0;
  cin >> item_count >> operation_count;
  item_count += 1;

  // Initialize items.
  vector<int> items(item_count);
  items.resize(item_count);
  for (int i = 0; i < item_count; i++) {
    items[i] = i;
  }

  // Do operations.
  for (int i = 0; i < operation_count; i++) {
    int m_in = 0;
    int a_in = 0;
    int b_in = 0;
    cin >> m_in >> a_in >> b_in;
    if (m_in == UNION_OP) {
      union_groups({a_in, b_in}, items);
    } else {
      bool result = is_grouped({a_in, b_in}, items);
      cout << (result ? "YES\n" : "NO\n");
    }
  }
}