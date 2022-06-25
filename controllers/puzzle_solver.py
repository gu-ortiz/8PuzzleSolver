from controllers.algorithm import best_possible_heuristic, simple_heuristic, uniform_cost
from entities.position import Position
from entities.board import Board
import time


class PuzzleSolver:
    def __init__(self) -> None:
        self.__frontier: list[Board] = []
        self.__visited: list[Board] = []
        self.__total_boards_created = 0
        self.__frontier_highest_size = 0

    def create_board(self, starting_matrix: list[list[Position]], result_matrix: list[list[Position]]) -> tuple[Board, Board]:
        return Board(starting_matrix, []), Board(result_matrix, [])

    def check_board_in_list(self, board: Board, list: list[Board]) -> bool:
        for item in list:
            if item.get_board_string() == board.get_board_string():
                return True

        return False

    def check_for_win_condition(self, board: Board, result_board: Board) -> bool:
        if board.get_board_string() == result_board.get_board_string():
            return True

        return False

    def get_best_expansion(self, result_board: Board, algorithm: callable) -> (Board | None):
        best_expansion: (Board | None) = None

        for board in self.__frontier:
            if not best_expansion:
                best_expansion = board
            else:
                best_expansion = board if (
                    algorithm(board, result_board) < algorithm(best_expansion, result_board)
                ) else best_expansion

        return best_expansion

    def visit_board(self, board: Board, result_board: Board) -> bool:
        self.__frontier = [item for item in self.__frontier if item.get_board_string() != board.get_board_string()]
        self.__visited.append(board)

        if self.check_for_win_condition(board, result_board):
            return True

        for move in board.moves:
            new_board = board.apply_move_to_board(move)
            if not self.check_board_in_list(new_board, self.__frontier) and not self.check_board_in_list(new_board, self.__visited):
                self.__frontier.append(new_board)
                self.__total_boards_created += 1

        return False

    def resolve_board(self, result_board: Board, algorithm: callable) -> Board:
        while True:
            self.__frontier_highest_size = len(self.__frontier) if (
                self.__frontier_highest_size < len(self.__frontier)
            ) else self.__frontier_highest_size

            board = self.get_best_expansion(result_board, algorithm)

            if self.visit_board(board, result_board):
                break

        return board

    def print_solution(self, board: Board) -> None:
        print('\nCaminho:\n')

        for value in board.path:
            print(value.replace('],', ']\n').replace('[[', '[').replace(
                ']]', ']').replace(' ', '').replace('0', ' ') + '\n')
        
        print(board.get_board_string().replace('],', ']\n').replace('[[', '[').replace(
            ']]', ']').replace(' ', '').replace('0', ' ') + '\n')

        print('Tamanho...........', len(board.path))
        print('Nodos visitados...', len(self.__visited))
        print('Nodos criados.....', self.__total_boards_created)
        print('Maior fronteira...', self.__frontier_highest_size)

    def run_solution(self, payload: dict) -> None:
        algorithm_dispatch = {
            1: uniform_cost,
            2: simple_heuristic,
            3: best_possible_heuristic
        }

        starting_board, result_board = self.create_board(payload.get('starting_matrix'), payload.get('result_matrix'))

        self.__frontier.append(starting_board)

        inicio = time.time()

        solution = self.resolve_board(result_board, algorithm_dispatch[payload.get('algorithm')])

        fim = time.time()

        self.print_solution(solution)
        print('Tempo (ms)........', (fim - inicio))
