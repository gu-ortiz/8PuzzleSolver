from entities.tree.node import Node


class VisitedNodes:
    def __init__(self) -> None:
        self.__list = []

    @property
    def list(self) -> list:
        return self.__list

    def push(self, node: Node):
        if isinstance(node, Node):
            self.__list.append(node)
