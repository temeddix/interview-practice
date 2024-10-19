class NonCopyable {
 public:
  NonCopyable() {}
  NonCopyable(const NonCopyable&) = delete;  // Deleted copy constructor
};

class MyClass {
 private:
  NonCopyable nc;  // Member with deleted copy constructor

 public:
  MyClass() {}
  // The default copy constructor is deleted here because of `nc`
};

int main() {
  MyClass obj1;
  // MyClass obj2 = obj1;  // Error: use of deleted function
}
