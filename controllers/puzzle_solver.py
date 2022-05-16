from typing import Tuple
from entities.board import Board
from controllers.algorithm import board_length_to_destiny, position_length_to_destiny


class PuzzleSolver:
    def __init__(self) -> None:
        self.__path = None
        self.__border = []
        self.__visited_nodes = []
        self.__total_nodes_created = 0
        self.__border_highest_size = 0

    def create_board(self, starting_matrix: list[list], result_matrix: list[list]) -> tuple[Board, Board]:
        return Board(starting_matrix), Board(result_matrix)

    def get_best_expansion(self, result_board: Board, algorithm: callable):
        best_expansion = None

        for board in self.__border:
            if len(board.moves) == 0:
                self.__border.remove(board)
                continue

            for move in board.moves:
                if not best_expansion:
                    best_expansion = (move, board)
                else:
                    best_expansion = (move, board) if (
                        algorithm(move, board, result_board) < algorithm(
                            best_expansion[0], best_expansion[1], result_board)
                    ) else best_expansion

        if best_expansion:
            best_expansion[1].moves.remove(best_expansion[0])

        return best_expansion

    def expand_frontier(self, move_board_tuple: tuple) -> None:
        move, board = move_board_tuple
        new_board = board.apply_move_to_board(move)
        new_board.moves = new_board.get_possible_moves()

        if new_board.get_board_string() not in self.__visited_nodes:
            self.__border.append(new_board)
            self.__visited_nodes.append(new_board.get_board_string())

    def check_for_win_condition(self, result_board: Board) -> bool:
        print(self.__border[-1].get_board_string())

        if result_board.get_board_string() == self.__border[-1].get_board_string():
            return True

        return False

    def compose_result_variables(self) -> None:
        pass

    def resolve_board(self, result_board: Board, algorithm=position_length_to_destiny) -> None:
        while True:
            expansion = self.get_best_expansion(result_board, algorithm)

            if expansion:
                self.expand_frontier(expansion)

            if self.check_for_win_condition(result_board):
                break

        print("Solved")

    def run_solution(self, payload: dict) -> None:
        algorithm_dispatch = {
            1: position_length_to_destiny,
            2: board_length_to_destiny,
            3: None
        }

        starting_board, result_board = self.create_board(payload.get('starting_matrix'), payload.get('result_matrix'))

        self.__border.append(starting_board)
        self.__visited_nodes.append(starting_board)

        self.resolve_board(result_board, algorithm_dispatch[payload.get('algorithm')])
