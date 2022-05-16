from __future__ import annotations
from entities.coordenate import Coordenate
from entities.position import Position
from entities.move import Move
from settings import BOARD_SIZE
from random import randrange
import copy


class Board:
    def __init__(self, matrix=None) -> None:
        if not matrix:
            self.__matrix = self.create_board(
                self.create_random_matrix()
            )
        else:
            self.__matrix = self.create_board(matrix)
        self.__moves = self.get_possible_moves()
        self.__path = []

    @property
    def matrix(self) -> list[list[Position]]:
        return self.__matrix

    @property
    def moves(self) -> list[Move]:
        return self.__moves

    @property
    def path(self) -> list:
        return self.__path

    @matrix.setter
    def matrix(self, value: list[list[Position]]) -> None:
        self.__matrix = value

    @moves.setter
    def moves(self, value: list) -> None:
        self.__moves = value

    @path.setter
    def path(self, value: list) -> None:
        self.__path = value

    def create_board(self, matrix: list[list[int]]) -> list[list[Position]]:
        for line_index, line in enumerate(matrix):
            for position_index, value in enumerate(line):
                matrix[line_index][position_index] = Position(
                    value,
                    Coordenate(position_index, line_index)
                )

        return matrix

    def create_random_matrix(self) -> list[list[int]]:
        board = [[0, 0, 0] for i in range(BOARD_SIZE)]
        numbers = [i for i in range(BOARD_SIZE * BOARD_SIZE)]

        for line_index, _ in enumerate(board):
            for position_index, _ in enumerate(board):
                board[line_index][position_index] = numbers.pop(
                    randrange(len(numbers))
                )

        return board

    def get_board_string(self) -> str:
        board_print = [[] for i in range(BOARD_SIZE)]

        for line_index, line in enumerate(self.__matrix):
            for position in line:
                board_print[line_index].append(position.value)

        return str(board_print)

    def get_possible_moves(self) -> list:
        empty_position = self.find_position_by_value(0)
        x, y = empty_position.coordenate.get_axis()
        possible_moves = []
        possible_axis_changes = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

        for axis in possible_axis_changes:
            coordenate = Coordenate(axis[0], axis[1])
            if coordenate.valid_coordenate():
                x2, y2 = coordenate.get_axis()
                possible_moves.append(
                    Move(
                        empty_position,
                        self.__matrix[y2][x2]
                    )
                )

        return possible_moves

    def find_position_by_value(self, value: int) -> Position:
        for line_index, line in enumerate(self.__matrix):
            for position_index, position in enumerate(line):
                if position.value == value:
                    return self.__matrix[line_index][position_index]

    def apply_move_to_board(self, move: Move) -> Board:
        # TODO Refactor this method
        new_board: Board = copy.deepcopy(self)

        x, y = move.origin.coordenate.get_axis()
        x1, y1 = move.destiny.coordenate.get_axis()

        new_board.matrix[y][x] = copy.deepcopy(self.__matrix[y1][x1])
        new_board.matrix[y][x].coordenate.x, new_board.matrix[y][x].coordenate.y = copy.copy(x), copy.copy(y)
        new_board.matrix[y1][x1] = copy.deepcopy(self.__matrix[y][x])
        new_board.matrix[y1][x1].coordenate.x, new_board.matrix[y1][x1].coordenate.y = copy.copy(x1), copy.copy(y1)

        new_board.path.append(self.get_board_string())

        return new_board
