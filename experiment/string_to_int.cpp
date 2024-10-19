#include <iostream>
#include <string>

int main() {
  // Convert char array to int
  char my_char_array[] = "1000";
  int char_array_to_int = std::stoi(my_char_array);
  std::cout << "char array to int: " << char_array_to_int << std::endl;
  // Outputs: 1000

  // Convert string to int
  std::string my_string = "2000";
  int string_to_int = std::stoi(my_string);
  std::cout << "string to int: " << string_to_int << std::endl;
  // Outputs: 2000

  return 0;
}
