#include <iostream>
#include <utility>  // for `move`

using namespace std;

class MyClass {
 private:
  int* data;        // Pointer to dynamically allocated resource
  bool is_owned{};  // Indicates if the instance is valid (not moved-from)

 public:
  // Constructor
  MyClass(int value) : data(new int(value)) {
    cout << "Constructor: " << *data << '\n';
  }

  // Disable copying
  MyClass(const MyClass&) = delete;         // Copy constructor
  auto operator=(const MyClass&) = delete;  // Copy assignment operator

  // Enable moving
  MyClass(MyClass&& other) noexcept
      : data(other.data), is_owned(other.is_owned) {
    other.data = nullptr;    // Leave other in a valid but unspecified state
    other.is_owned = false;  // Mark other as moved-from
    cout << "Move Constructor called." << '\n';
  }
  auto operator=(MyClass&& other) noexcept -> MyClass& {
    if (this != &other) {
      delete data;        // Free existing resource
      data = other.data;  // Transfer ownership
      is_owned = other.is_owned;

      other.data = nullptr;    // Leave other in a valid but unspecified state
      other.is_owned = false;  // Mark other as moved-from
      cout << "Move Assignment Operator called." << '\n';
    }
    return *this;
  }

  // Destructor
  ~MyClass() {
    if (is_owned) {
      delete data;  // Only delete if valid
      cout << "Destructor called." << '\n';
    }
  }

  // Function to access data safely
  void print() const {
    if (!is_owned) {
      cout << "Error: Attempt to use moved-from object." << '\n';
      return;
    }
    cout << "Data: " << *data << '\n';
  }
};

const int INITIAL_VALUE = 42;

auto main() -> int {
  MyClass obj1(INITIAL_VALUE);
  obj1.print();  // Output: Data: 42

  // Trying to copy an object produces an error
  // because the copy constructor is deleted.
  // We can move the value instead.
  MyClass obj2 = std::move(obj1);
  // MyClass obj2 = obj1;

  obj2.print();  // Output: Data: 42
  obj1.print();  // Output: Error: Attempt to use moved-from object.
}
