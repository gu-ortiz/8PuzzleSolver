from entities.board import Board


def uniform_cost(board: Board, result_board: Board) -> int:
    return len(board.path)

def simple_heuristic(board: Board, result_board: Board) -> int:
    heuristic_value = 0

    for line in board.matrix:
        for position in line:
            if position.value != 0:
                coordinate_x, coordinate_y = position.coordinate.get_axis()
                expected_x, expected_y = result_board.find_position_by_value(position.value).coordinate.get_axis()
                heuristic_value += (
                    abs(coordinate_x - expected_x) +
                    abs(coordinate_y - expected_y)
                )

    return (
        heuristic_value +
        uniform_cost(board, result_board)
    )

def best_possible_heuristic(board: Board, result_board: Board) -> int:
    heuristic_value = 0

    for i in range(2):
        for j in range(3):
            if (
                board.matrix[i][j].value == result_board.matrix[i+1][j].value
            ) and (
                board.matrix[i+1][j].value == result_board.matrix[i][j].value
            ) and (
                board.matrix[i][j].value != 0 and board.matrix[i+1][j].value != 0
            ):
                heuristic_value += 2
            if (
                board.matrix[j][i].value == result_board.matrix[j][i+1].value
            ) and (
                board.matrix[j][i+1].value == result_board.matrix[j][i].value
            ) and (
                board.matrix[j][i].value != 0 and board.matrix[j][i+1].value != 0
            ):
                heuristic_value += 2

    return (
        heuristic_value +
        simple_heuristic(board, result_board)
    )
