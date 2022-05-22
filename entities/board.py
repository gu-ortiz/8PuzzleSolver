from __future__ import annotations
from settings import BOARD_SIZE
from entities.coordinate import Coordinate
from entities.position import Position
from entities.move import Move
from random import randrange
import copy


class Board:
    def __init__(self, matrix: (list[list[Position]] | None), path: list[str]) -> None:
        if not matrix:
            self.__matrix = self.create_board(
                self.create_random_matrix()
            )
        else:
            self.__matrix = self.create_board(matrix)
        self.__moves = self.get_possible_moves()
        self.__path = path

    @property
    def matrix(self) -> list[list[Position]]:
        return self.__matrix

    @property
    def moves(self) -> list[Move]:
        return self.__moves

    @property
    def path(self) -> list[str]:
        return self.__path

    @matrix.setter
    def matrix(self, value: list[list[Position]]) -> None:
        self.__matrix = value

    @moves.setter
    def moves(self, value: list[Move]) -> None:
        self.__moves = value

    @path.setter
    def path(self, value: list[str]) -> None:
        self.__path = value

    def create_board(self, matrix: list[list[int]]) -> list[list[Position]]:
        for line_index, line in enumerate(matrix):
            for position_index, value in enumerate(line):
                matrix[line_index][position_index] = Position(
                    value,
                    Coordinate(position_index, line_index)
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
        board = [[] for i in range(BOARD_SIZE)]

        for line_index, line in enumerate(self.__matrix):
            for position in line:
                board[line_index].append(position.value)

        return str(board)

    def get_board_int(self) -> list[list[int]]:
        board = [[] for i in range(BOARD_SIZE)]

        for line_index, line in enumerate(self.__matrix):
            for position in line:
                board[line_index].append(position.value)

        return board

    def get_possible_moves(self) -> list[Move]:
        empty_position = self.find_position_by_value(0)
        x, y = empty_position.coordinate.get_axis()
        possible_moves = []
        possible_axis_changes = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

        for axis in possible_axis_changes:
            coordinate = Coordinate(axis[0], axis[1])
            if coordinate.valid_coordinate():
                x2, y2 = coordinate.get_axis()
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
        new_matrix: list[list[int]] = self.get_board_int()
        new_path: list[str] = copy.deepcopy(self.__path)

        x, y = move.origin.coordinate.get_axis()
        x1, y1 = move.destiny.coordinate.get_axis()

        new_matrix[y][x] = copy.copy(self.__matrix[y1][x1].value)
        new_matrix[y1][x1] = copy.copy(self.__matrix[y][x].value)

        new_board: Board = Board(
            new_matrix,
            new_path
        )
        new_board.path.append(self.get_board_string())

        return new_board
