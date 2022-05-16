from entities.move import Move
from entities.board import Board


def position_length_to_destiny(move: Move, board: Board, result_board: Board) -> int:
    new_board = board.apply_move_to_board(move)
    coordenate_x, coordenate_y = move.origin.coordenate.get_axis()
    expected_x, expected_y = result_board.find_position_by_value(
        move.destiny.value
    ).coordenate.get_axis()

    return (
        abs(coordenate_x - expected_x) + abs(coordenate_y - expected_y)
    )


def board_length_to_destiny(move: Move, board: Board, result_board: Board) -> int:
    heuristic_value = 1
    new_board = board.apply_move_to_board(move)
    for line in new_board.board_matrix:
        for position in line:
            if position.value != 0:
                coordenate_x, coordenate_y = position.coordenate.get_axis()
                expected_x, expected_y = result_board.find_position_by_value(
                    position.value
                ).coordenate.get_axis()
                heuristic_value += (
                    abs(coordenate_x - expected_x) +
                    abs(coordenate_y - expected_y)
                )

    return heuristic_value + position_length_to_destiny(move, board, result_board)
