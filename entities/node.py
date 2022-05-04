
class Node:
  def __init__(self, board):
    self.__board = board

  @property
  def board(self):
    return self.__board
