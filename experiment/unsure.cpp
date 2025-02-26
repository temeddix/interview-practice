#include <iostream>
#include <optional>
#include <string>
#include <variant>

using namespace std;

// Function returning optional
auto get_number(bool give_value) -> optional<int> {
  const int number = 42;
  if (give_value) {
    return number;
  }
  return nullopt;  // No value
}

// Function returning variant
auto process_data(bool use_string) -> variant<int, string> {
  const int number = 123;
  if (use_string) {
    return string("Hello, Variant!");
  }
  return number;
}

auto main() -> int {
  // Using optional
  optional<int> opt = get_number(true);
  if (opt) {
    cout << "Optional has value: " << *opt << '\n';
  } else {
    cout << "Optional is empty\n";
  }

  // Using variant
  variant<int, string> var = process_data(false);
  if (holds_alternative<int>(var)) {
    cout << "Variant holds an int: " << get<int>(var) << '\n';
  } else {
    cout << "Variant holds a string: " << get<string>(var) << '\n';
  }
}
