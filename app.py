# Sudoku - This is a project to solve Sudoku using back-tracking
#
# Author: Indrajit Ghosh
# Created on: Apr 27, 2024
#

from flask import Flask, render_template, request
from sudoku.model import SudokuBoard
from copy import deepcopy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sudoku')
def sudoku():
    return render_template('input_sudoku.html')

@app.route('/solve', methods=['POST'])
def solve():
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
