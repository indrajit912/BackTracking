# Sudoku/model.py
#
# Author: Indrajit Ghosh
# Created on: Apr 27, 2024
#

import random

__all__ = ["SudokuBoard"]

class SudokuBoard:
    """
    A class to represent a Sudoku board and provide methods for solving it.

    Author: Indrajit Ghosh
    Created On: Apr 27, 2024

    Attributes:
        _board (list): A 9x9 list representing the Sudoku board.
    """

    def __init__(self, board):
        """
        Initializes the SudokuBoard with a given board configuration.

        Parameters:
            board (list): A 9x9 list representing the initial Sudoku board.
        """
        self._board = board
        self._rows = len(board)
        self._cols = len(board[0]) 

    @property
    def board(self):
        """
        Gets the Sudoku board.

        Returns:
            list: A 9x9 list representing the Sudoku board.
        """
        return self._board

    @board.setter
    def board(self, new_board):
        """
        Sets the Sudoku board with a new configuration.

        Parameters:
            new_board (list): A 9x9 list representing the new Sudoku board configuration.
        """
        self._board = new_board

    def __str__(self):
        """
        Returns a string representation of the Sudoku board.
        """
        board_str = ""
        for i in range(len(self._board)):
            if i % 3 == 0 and i != 0:
                board_str += "- - - - - - - - - - - - - \n"

            for j in range(len(self._board[0])):
                if j % 3 == 0 and j != 0:
                    board_str += " | "

                if j == 8:
                    board_str += str(self._board[i][j]) + "\n"
                else:
                    board_str += str(self._board[i][j]) + " "

        return board_str

    def get_empty_cell(self):
        """
        Get an empty cell (denoted by 0) in the Sudoku board.

        Returns:
            tuple: A tuple containing the row and column indices of an empty cell.
                   Returns None if no empty cell is found.
        """
        for i in range(len(self._board)):
            for j in range(len(self._board[0])):
                if self._board[i][j] == 0:
                    return i, j  # row, col

        return None

    def is_valid(self, num, pos):
        """
        Check whether placing the given `num` at the position `pos` of the Sudoku board is valid.

        Parameters:
            num (int): The number to be checked for validity at the position `pos`.
            pos (tuple): A tuple containing the row and column indices of the position to check.

        Returns:
            bool: True if placing `num` at `pos` is valid, False otherwise.
        """
        row, col = pos

        # Check whether `num` appears once in the row `pos[0]`
        for j in range(len(self._board[0])):
            if self._board[row][j] == num and j != col:  # If the number appears again in the same row
                return False

        # Check whether `num` appears once in the column `pos[1]`
        for i in range(len(self._board)):
            if self._board[i][col] == num and i != row:  # If the number appears again in the same column
                return False

        # Check whether `num` appears once in the 3x3 square
        # Determine the starting position of the square
        a, b = pos[0] - (pos[0] % 3), pos[1] - (pos[1] % 3)
        for i in range(3):  # Loop through the rows of the square
            for j in range(3):  # Loop through the columns of the square
                if self._board[a + i][b + j] == num and (a + i, b + j) != pos:  # If the number appears again in the square
                    return False             
        return True

    def solve(self):
        """
        Solves the Sudoku board using backtracking.

        Returns:
            bool: True if the Sudoku board is solvable and solved successfully, False otherwise.
        """
        empty_cell = self.get_empty_cell()

        # No empty cell found! This means the board is solved already (due to backtracking).
        if not empty_cell:
            return True
        else:
            row, col = empty_cell

        # Place all the numbers through 1 to 9 on this empty cell and backtrack.
        for num in range(1, 10):
            if self.is_valid(num, (row, col)):
                self._board[row][col] = num

                if self.solve():
                    return True

                self._board[row][col] = 0

        return False

    def is_solved(self):
        """
        Check if the Sudoku board is solved.

        Returns:
            bool: True if the board is solved, False otherwise.
        """
        # Check rows
        for row in self._board:
            if len(set(row)) != 9 or 0 in row:
                return False

        # Check columns
        for col in range(9):
            column_values = [self._board[row][col] for row in range(9)]
            if len(set(column_values)) != 9 or 0 in column_values:
                return False

        # Check 3x3 subgrids
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                subgrid = [self._board[row][col] for row in range(i, i + 3) for col in range(j, j + 3)]
                if len(set(subgrid)) != 9 or 0 in subgrid:
                    return False

        return True

    @classmethod
    def get_empty_board(cls):
        """
        Returns an empty SudokuBoard
        """
        return cls([[0 for _ in range(9)] for _ in range(9)])
    
    @classmethod
    def get_random_solved_board(cls):
        """
        Generates a random Sudoku board.

        Returns:
            SudokuBoard: A SudokuBoard object representing the random Sudoku board.
        """
        # Start with an empty board
        board = [[0 for _ in range(9)] for _ in range(9)]

        # Fill the diagonal 3x3 squares with random numbers
        for i in range(0, 9, 3):
            nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            random.shuffle(nums)
            for j in range(3):
                for k in range(3):
                    board[i + j][i + k] = nums.pop()

        # Solve the board to get a valid Sudoku puzzle
        sudoku = cls(board)
        sudoku.solve()
        return sudoku
    
    @classmethod
    def get_random_puzzle(cls):
        """
        Generates a random Sudoku puzzle.

        Returns:
            SudokuBoard: A SudokuBoard object representing the random Sudoku puzzle.
        """
        # Generate a random solved Sudoku board
        solved_board = cls.get_random_solved_board().board

        # Create a copy of the solved board
        puzzle_board = [row[:] for row in solved_board]

        # Randomly remove numbers to create the puzzle
        for i in range(81 // 2):  # Remove half of the numbers
            row, col = random.randint(0, 8), random.randint(0, 8)
            while puzzle_board[row][col] == 0:
                row, col = random.randint(0, 8), random.randint(0, 8)
            puzzle_board[row][col] = 0

        return cls(puzzle_board)