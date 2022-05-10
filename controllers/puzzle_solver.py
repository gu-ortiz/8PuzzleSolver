from entities.node import Node
from entities.border import Border
from entities.visited_nodes import VisitedNodes


class PuzzleSolver:
  def __init__(self, node: Node, ) -> None:
    self.__actual_node = node
    self.__border = Border()
    self.__visited_nodes = VisitedNodes()
    self.__total_nodes_created = 0
    self.__border_highest_size = 0

  @property
  def actual_node(self) -> Node:
    return self.__actual_node

  @property
  def border(self) -> Border:
    return self.__border

  @property
  def visited_nodes(self) -> VisitedNodes:
    return self.__visited_nodes

  @property
  def total_nodes_created(self) -> int:
    return self.__total_nodes_created

  @property
  def border_highest_size(self) -> int:
    return self.__border_highest_size
