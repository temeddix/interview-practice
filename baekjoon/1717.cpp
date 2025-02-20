#include <algorithm>
#include <iostream>
#include <vector>

int UNION_OP = 0;

struct ItemPair {
  int item_a;
  int item_b;
};

int get_root(int item, std::vector<int>& items) {
  if (items[item] != item) {
    items[item] = get_root(items[item], items);
  }
  return items[item];
}

void union_groups(ItemPair item_pair, std::vector<int>& items) {
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

bool is_grouped(ItemPair item_pair, std::vector<int>& items) {
  return get_root(item_pair.item_a, items) == get_root(item_pair.item_b, items);
}

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(NULL);
  std::cout.tie(NULL);

  // Get the basic input.
  int item_count, operation_count;
  std::cin >> item_count >> operation_count;
  item_count += 1;

  // Initialize items.
  std::vector<int> items(item_count);
  items.resize(item_count);
  for (int i = 0; i < item_count; i++) {
    items[i] = i;
  }

  // Do operations.
  for (int i = 0; i < operation_count; i++) {
    int m, a, b;
    std::cin >> m >> a >> b;
    if (m == UNION_OP) {
      union_groups({a, b}, items);
    } else {
      bool result = is_grouped({a, b}, items);
      std::cout << (result ? "YES\n" : "NO\n");
    }
  }
}