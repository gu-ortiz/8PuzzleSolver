from controllers.puzzle_solver import PuzzleSolver
from settings import EXAMPLE_BOARD, EXPECTED_RESULT, ALGORITHM


def run_eights_game():
    payload = {
        'starting_matrix': EXAMPLE_BOARD,
        'result_matrix': EXPECTED_RESULT,
        'algorithm': ALGORITHM
    }
    PuzzleSolver().run_solution(payload)


if __name__ == '__main__':
    run_eights_game()
