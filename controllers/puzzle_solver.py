
class PuzzleSolver:
  def __init__(self, node):
    self.__total_nodes_visited = 0
    self.__total_nodes_created = 0
    self.__border_highest_size = 0
    self.__actual_node = node

  @property
  def total_nodes_visited(self):
    return self.__total_nodes_visited

  @property
  def total_nodes_created(self):
    return self.__total_nodes_created

  @property
  def border_highest_size(self):
    return self.__border_highest_size

  @property
  def actual_node(self):
    return self.__actual_node
