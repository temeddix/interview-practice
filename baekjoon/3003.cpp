#include <iostream>

int main() {
  short king, queen, rook, bishop, knight, pawn;
  std::cin >> king >> queen >> rook >> bishop >> knight >> pawn;

  std::cout << 1 - king << ' ' << 1 - queen;
  std::cout << ' ' << 2 - rook << ' ' << 2 - bishop << ' ' << 2 - knight;
  std::cout << ' ' << 8 - pawn;
}