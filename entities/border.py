from entities.node import Node


class Border:
  def __init__(self) -> None:
    self.__list = []

  @property
  def list(self) -> list:
    return self.__list

  def push(self, node: Node):
    self.__list.append(node)
