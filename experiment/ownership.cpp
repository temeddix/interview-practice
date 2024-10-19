#include <iostream>
#include <utility>  // for std::move

class MyClass {
 private:
  int* data;      // Pointer to dynamically allocated resource
  bool is_valid;  // Indicates if the instance is valid (not moved-from)

 public:
  // Constructor
  MyClass(int value) : data(new int(value)), is_valid(true) {
    std::cout << "Constructor: " << *data << std::endl;
  }

  // Disable copying
  MyClass(const MyClass&) = delete;             // Copy constructor
  MyClass& operator=(const MyClass&) = delete;  // Copy assignment operator

  // Enable moving
  MyClass(MyClass&& other) noexcept
      : data(other.data), is_valid(other.is_valid) {
    other.data = nullptr;    // Leave other in a valid but unspecified state
    other.is_valid = false;  // Mark other as moved-from
    std::cout << "Move Constructor called." << std::endl;
  }
  MyClass& operator=(MyClass&& other) noexcept {
    if (this != &other) {
      delete data;        // Free existing resource
      data = other.data;  // Transfer ownership
      is_valid = other.is_valid;

      other.data = nullptr;    // Leave other in a valid but unspecified state
      other.is_valid = false;  // Mark other as moved-from
      std::cout << "Move Assignment Operator called." << std::endl;
    }
    return *this;
  }

  // Destructor
  ~MyClass() {
    if (is_valid) {
      delete data;  // Only delete if valid
      std::cout << "Destructor called." << std::endl;
    }
  }

  // Function to access data safely
  void print() const {
    if (!is_valid) {
      std::cout << "Error: Attempt to use moved-from object." << std::endl;
      return;
    }
    std::cout << "Data: " << *data << std::endl;
  }
};

int main() {
  MyClass obj1(42);
  obj1.print();  // Output: Data: 42

  MyClass obj2 = std::move(obj1);  // Move obj1 into obj2

  obj2.print();  // Output: Data: 42
  obj1.print();  // Output: Error: Attempt to use moved-from object.

  return 0;
}
