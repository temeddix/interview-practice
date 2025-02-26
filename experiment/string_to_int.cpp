#include <iostream>
#include <string>

using namespace std;

const string my_char_array = "1000";

auto main() -> int {
  // Convert char array to int
  int char_array_to_int = stoi(my_char_array);
  cout << "char array to int: " << char_array_to_int << '\n';
  // Outputs: 1000

  // Convert string to int
  string my_string = "2000";
  int string_to_int = stoi(my_string);
  cout << "string to int: " << string_to_int << '\n';
  // Outputs: 2000
}
