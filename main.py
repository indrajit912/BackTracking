# BackTrack - This is a project to solve Few problems using back-tracking
#
# Author: Indrajit Ghosh
# Created on: Apr 27, 2024
#

from chess import *
from pprint import pprint

def main():
    chess_board = ChessBoard(
        data={
            'a5': ChessPiece('black_queen'),
            'b3': ChessPiece('black_queen'),
            'c1': ChessPiece('black_queen'),
            'd7': ChessPiece('black_queen'),
            'e2': ChessPiece('black_queen'),
            'f8': ChessPiece('black_queen'),
            'g6': ChessPiece('black_queen'),
            'h4': ChessPiece('black_queen')
        }
    )

    pprint(chess_board.get_integer_board())
    print()


if __name__ == '__main__':
    main()
    