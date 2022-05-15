

class Node:
    def __init__(self, board, prev) -> None:
        self.__board = board
        self.__prev = prev

    @property
    def board(self):
        return self.__board

    @property
    def prev(self):
        return self.__prev
