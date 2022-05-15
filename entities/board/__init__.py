from entities.board.coordenate import Coordenate
from entities.board.position import Position
from entities.board.move import Move
from settings import BOARD_SIZE
from random import randrange
import copy


class Board:
    def __init__(self, board_matrix=None):
        if not board_matrix:
            self.__board_matrix = self.create_board(
                self.create_random_matrix()
            )
        else:
            self.__board_matrix = self.create_board(board_matrix)

    def get_board_string(self):
        board_print = [[] for i in range(BOARD_SIZE)]

        for line_index, line in enumerate(self.__board_matrix):
            for position in line:
                board_print[line_index].append(position.value)

        return str(board_print)

    def create_board(self, board_matrix: list[list]):
        for line_index, line in enumerate(board_matrix):
            for position_index, _ in enumerate(line):
                board_matrix[line_index][position_index] = Position(
                    board_matrix[line_index][position_index],
                    Coordenate(position_index, line_index)
                )

        return board_matrix

    def create_random_matrix(self):
        board = [[0, 0, 0] for i in range(BOARD_SIZE)]
        numbers = [i for i in range(BOARD_SIZE * BOARD_SIZE)]

        for line_index, _ in enumerate(board):
            for position_index, _ in enumerate(board):
                board[line_index][position_index] = numbers.pop(
                    randrange(len(numbers))
                )

        return board

    def get_possible_moves(self):
        empty_position_coordenate = self.find_position_by_value(0).coordenate
        x, y = empty_position_coordenate.get_axis()
        possible_axis_changes = [
            (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)
        ]
        possible_moves = []

        for axis in possible_axis_changes:
            coordenate = Coordenate(axis[0], axis[1])
            if coordenate.valid_coordenate():
                possible_moves.append(
                    Move(
                        empty_position_coordenate,
                        coordenate
                    )
                )

        return possible_moves

    def find_position_by_value(self, value: int):
        for line_index, line in enumerate(self.__board_matrix):
            for position_index, position in enumerate(line):
                if position.value == value:
                    return self.__board_matrix[line_index][position_index]

    def apply_move_to_board(self, move: Move):
        new_board = copy.deepcopy(self.__board_matrix)
        x, y = move.origin.get_axis()
        x1, y1 = move.destiny.get_axis()
        new_board[y][x] = self.__board_matrix[y1][x1]
        new_board[y1][x1] = self.__board_matrix[y][x]

        return new_board
