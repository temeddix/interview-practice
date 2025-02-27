#include <iostream>
#include <optional>
#include <stdexcept>
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
auto process_data(bool use_string) -> variant<int, invalid_argument> {
  const int number = 123;
  if (use_string) {
    return invalid_argument("Something went wrong!");
  }
  return number;
}

auto main() -> int {
  // Using optional
  optional<int> option = get_number(true);
  if (option) {
    cout << "Optional has value: " << *option << '\n';
  } else {
    cout << "Optional is empty\n";
  }

  // Using variant
  variant<int, invalid_argument> result = process_data(true);
  if (holds_alternative<int>(result)) {
    cout << "Variant holds an int: " << get<int>(result) << '\n';
  } else {
    cout << "Exception: " << get<invalid_argument>(result).what() << '\n';
  }
}
