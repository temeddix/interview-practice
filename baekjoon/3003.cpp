#include <iostream>

auto main() -> int {
  short king = 0;
  short queen = 0;
  short rook = 0;
  short bishop = 0;
  short knight = 0;
  short pawn = 0;
  std::cin >> king >> queen >> rook >> bishop >> knight >> pawn;

  std::cout << 1 - king << ' ' << 1 - queen;
  std::cout << ' ' << 2 - rook << ' ' << 2 - bishop << ' ' << 2 - knight;
  std::cout << ' ' << 8 - pawn;
}