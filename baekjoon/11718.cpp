#include <iostream>
#include <string>

auto main() -> int {
  std::string line;  // To store each line of input

  // Continuously read lines until EOF or an error occurs
  while (std::getline(std::cin, line)) {
    if (line.empty()) {
      break;
    }
    std::cout << line << '\n';  // Output the line as it is
  }
}