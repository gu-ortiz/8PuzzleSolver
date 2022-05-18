from entities.move import Move
from entities.board import Board


def uniform_cost(board: Board, result_board: Board) -> int:
    return len(board.path)

def position_length_to_destiny(board: Board, result_board: Board) -> int:
    heuristic_value = 1

    for line in board.matrix:
        for position in line:
            if position.value != 0:
                coordenate_x, coordenate_y = position.coordenate.get_axis()
                expected_x, expected_y = result_board.find_position_by_value(position.value).coordenate.get_axis()
                heuristic_value += (
                    abs(coordenate_x - expected_x) +
                    abs(coordenate_y - expected_y)
                )

    return (
        heuristic_value +
        uniform_cost(board, result_board)
    )

def board_length_to_destiny(board: Board, result_board: Board) -> int:
    return
