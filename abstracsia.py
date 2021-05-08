# Абстрактные классы не могут быть инстанциированы,
# от них нужно унаследовать,
#  реализовать все их абстрактные методы и только тогда можно создать экземпляр такого класса.

from abc import ABC, abstractmethod
 
class ChessPiece(ABC):
    def draw(self):
        print("Drew a chess piece")
 
class Queen(ChessPiece):
    def move(self):
        print("Moved Queen to e2e4")

q = Queen()
q.draw()
q.move()