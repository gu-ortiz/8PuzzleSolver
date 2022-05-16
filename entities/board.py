from __future__ import annotations
from entities.coordenate import Coordenate
from entities.position import Position
from entities.move import Move
from settings import BOARD_SIZE
from random import randrange
import copy


class Board:
    def __init__(self, board_matrix=None) -> None:
        if not board_matrix:
            self.__board_matrix = self.create_board(
                self.create_random_matrix()
            )
        else:
            self.__board_matrix = self.create_board(board_matrix)

        self.__moves = self.get_possible_moves()
        self.__path = []

    @property
    def board_matrix(self) -> list[list]:
        return self.__board_matrix

    @property
    def moves(self) -> list:
        return self.__moves

    @property
    def path(self) -> list:
        return self.__path

    @board_matrix.setter
    def board_matrix(self, value: list[list]) -> None:
        if isinstance(value, list[list]):
            self.__board_matrix = value

    @moves.setter
    def moves(self, value: list) -> None:
        if isinstance(value, list):
            self.__moves = value

    @path.setter
    def path(self, value: list) -> None:
        if isinstance(value, list):
            self.__path = value

    def get_board_string(self) -> str:
        board_print = [[] for i in range(BOARD_SIZE)]

        for line_index, line in enumerate(self.__board_matrix):
            for position in line:
                board_print[line_index].append(position.value)

        return str(board_print).replace('],', ']\n').replace('[[', '[').replace(']]', ']').replace(' ', '').replace('0', ' ') + '\n'

    def create_board(self, board_matrix: list[list]) -> list[list]:
        for line_index, line in enumerate(board_matrix):
            for position_index, _ in enumerate(line):
                board_matrix[line_index][position_index] = Position(
                    board_matrix[line_index][position_index],
                    Coordenate(position_index, line_index)
                )

        return board_matrix

    def create_random_matrix(self) -> list[list[int]]:
        board = [[0, 0, 0] for i in range(BOARD_SIZE)]
        numbers = [i for i in range(BOARD_SIZE * BOARD_SIZE)]

        for line_index, _ in enumerate(board):
            for position_index, _ in enumerate(board):
                board[line_index][position_index] = numbers.pop(
                    randrange(len(numbers))
                )

        return board

    def get_possible_moves(self) -> list:
        empty_position = self.find_position_by_value(0)
        x, y = empty_position.coordenate.get_axis()
        possible_moves = []
        possible_axis_changes = [
            (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)
        ]

        for axis in possible_axis_changes:
            coordenate = Coordenate(axis[0], axis[1])
            if coordenate.valid_coordenate():
                x2, y2 = coordenate.get_axis()
                possible_moves.append(
                    Move(
                        empty_position,
                        self.__board_matrix[y2][x2]
                    )
                )

        return possible_moves

    def find_position_by_value(self, value: int) -> Position:
        for line_index, line in enumerate(self.__board_matrix):
            for position_index, position in enumerate(line):
                if position.value == value:
                    return self.__board_matrix[line_index][position_index]

    def apply_move_to_board(self, move: Move) -> Board:
        # TODO Refactor this method
        new_board = copy.deepcopy(self)

        x, y = move.origin.coordenate.get_axis()
        x1, y1 = move.destiny.coordenate.get_axis()

        new_board.board_matrix[y][x] = copy.deepcopy(
            self.__board_matrix[y1][x1])
        new_board.board_matrix[y][x].coordenate.x, new_board.board_matrix[y][x].coordenate.y = copy.copy(
            x), copy.copy(y)
        new_board.board_matrix[y1][x1] = copy.deepcopy(
            self.__board_matrix[y][x])
        new_board.board_matrix[y1][x1].coordenate.x, new_board.board_matrix[y1][x1].coordenate.y = copy.copy(
            x1), copy.copy(y1)

        return new_board
