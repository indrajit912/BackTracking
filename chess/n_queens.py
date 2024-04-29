# N-Queens Puzzle!
# 
# The N-Queens problem is a classic puzzle that involves placing N queens on 
# an N×N chessboard in such a way that no two queens threaten each other. 
# In other words, no two queens should share the same row, column, or diagonal. 
# The goal is to find all possible arrangements of N queens that satisfy these constraints.
# 
# Statement: Construct an n x n matrix with entries of either 0 or 1, ensuring that 
# each row and column contains exactly one 1, and no two 1s are on the same diagonal.
# 
# Author: Indrajit Ghosh
# Created On: Apr 28, 2024
# 
import numpy as np

def check_row_col_sum(array:np.ndarray):
    """
    Check whether the row sum and column sum of each row and column is not bigger than 1.

    Parameters:
    array (numpy.ndarray): Input 2D NumPy array.

    Returns:
    bool: True if all row and column sums are not greater than 1, False otherwise.
    """
    row_sum = np.sum(array, axis=1)
    col_sum = np.sum(array, axis=0)

    for i in range(len(array)):
        if row_sum[i] > 1 or col_sum[i] > 1:
            return False
    return True


def check_diagonals_sum(array:np.ndarray):
    """
    Check whether the sum of each diagonal (parallel to principal) 
    is not bigger than 1.

    This determines whether there is atmost one queen on each diagonal.

    Parameters:
    array (numpy.ndarray): Input square 2D NumPy array.

    Returns:
    bool: True if the sum of each diagonal is not greater than 1, False otherwise.
    """
    n = len(array)
    for i in range(n):
        if np.trace(array, offset=i) > 1:
            return False
        if i != 0:
            if np.trace(array, offset=-i) > 1:
                return False

    return True


def is_valid(board):
    """
    This function make sure that none of the queens are attacking each other!
    """
    return check_row_col_sum(board) and check_diagonals_sum(board) and check_diagonals_sum(board[:, ::-1])


def solve_n_queens(board: np.ndarray, col: int):
    """
    Solves the N-Queens problem using backtracking algorithm.

    Places N queens on an N x N chessboard in such a way that no two queens
    attack each other. This function attempts to find a solution by recursively
    placing queens on the board, backtracking when a conflict arises.

    Parameters:
        board (numpy.ndarray): An N x N numpy array representing the chessboard.
        col (int): The current column being considered for queen placement.

    Returns:
        bool: True if a solution is found, False otherwise.
    """
    n = len(board)

    # Base case: If all queens are placed and no conflicts, return True
    if board.sum() == n and is_valid(board):
        return True

    # Try placing a queen in each row of the current column
    for row in range(n):
        board[row][col] = 1

        # Check if the current placement is valid
        if is_valid(board):
            # Recursively try placing queens in the next column
            if solve_n_queens(board, col + 1):
                return True

            # If placing a queen in the next column doesn't lead to a solution,
            # backtrack by removing the current queen placement
            board[row][col] = 0
        else:
            # If the current placement is invalid, backtrack by removing the queen
            board[row][col] = 0

    # If no solution is found in this branch, return False
    return False



def main():
    N = 12
    bo = np.zeros((N, N))
    
    solve_n_queens(bo, 0)
    print(bo)


if __name__ == '__main__':
    main()
    