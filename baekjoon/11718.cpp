#include <iostream>
#include <string>

int main() {
  std::string line;  // To store each line of input

  // Continuously read lines until EOF or an error occurs
  while (std::getline(std::cin, line)) {
    if (line.size() == 0) {
      break;
    }
    std::cout << line << std::endl;  // Output the line as it is
  }
}