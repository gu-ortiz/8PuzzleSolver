
from multiprocessing.dummy import Array


class Node:
  def __init__(self, board, prev):
    self.__board = board
    self.__board = board

  @property
  def board(self):
    return self.__board
