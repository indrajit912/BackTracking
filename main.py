# BackTrack - This is a project to solve Few problems using back-tracking
#
# Author: Indrajit Ghosh
# Created on: Apr 27, 2024
#

from chess import *
from pprint import pprint

def main():
    chess_board = ChessBoard.from_list(eight_queens_board)

    print(chess_board)
    print()


if __name__ == '__main__':
    main()
    