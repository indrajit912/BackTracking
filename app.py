# BackTrack - This is a project to solve Few problems using back-tracking
#
# Author: Indrajit Ghosh
# Created on: Apr 27, 2024
#

from flask import Flask, render_template, request
from sudoku.model import SudokuBoard
from copy import deepcopy
from chess import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sudoku')
def sudoku():
    return render_template('input_sudoku.html')

@app.route('/solve_sudoku', methods=['POST'])
def solve_sudoku():
    given_board = [[0 for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            cell_value = request.form.get(f'cell{i}{j}')
            if cell_value.isdigit():
                given_board[i][j] = int(cell_value)

    # Check if all elements in the given_board are 0
    all_zero = all(all(cell == 0 for cell in row) for row in given_board)

    # Generate a Sudoku board
    sudoku_board = (
        SudokuBoard.get_random_puzzle()
        if all_zero
        else SudokuBoard(given_board)
    )
    puzzle_board = deepcopy(sudoku_board.board)

    # TODO: Check whether it is solvable or not

    # Solve the puzzle board
    sudoku_board.solve()

    solved_board = sudoku_board.board  # This is solved

    # Pass both the puzzle board and the solved board to the template
    return render_template(
        'sudoku.html', 
        puzzle_board=puzzle_board,
        solved_board=solved_board
    )

@app.route('/chessboard')
def chessboard():
    chess_board_obj = ChessBoard.from_list(eight_queens_board)

    board = [
        [57, 12, 20, 23, 49, 11, 31, 36],
        [45, 6, 4, 24, 52, 2, 22, 54],
        [17, 26, 59, 16, 10, 29, 64, 47],
        [38, 63, 41, 61, 14, 53, 18, 44],
        [9, 35, 62, 34, 55, 1, 7, 19],
        [40, 5, 32, 43, 56, 28, 60, 46],
        [50, 15, 27, 58, 51, 30, 3, 37],
        [39, 13, 33, 21, 42, 8, 48, 25]
    ]


    return render_template(
        'chessboard.html',
        chess_board = chess_board_obj.get_board_string_representation()
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
