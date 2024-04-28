# Models for chessboard
# Author: Indrajit Ghosh
# Created On: Apr 28, 2024
#

class ChessPiece:
    """
    A class to represent a chess piece.
    """

    chess_pieces = {
        'black_pawn': {'symbol': '♟', 'color': 'black', 'value': -1},
        'black_rook': {'symbol': '♜', 'color': 'black', 'value': -2},
        'black_knight': {'symbol': '♞', 'color': 'black', 'value': -3},
        'black_bishop': {'symbol': '♝', 'color': 'black', 'value': -4},
        'black_queen': {'symbol': '♛', 'color': 'black', 'value': -5},
        'black_king': {'symbol': '♚', 'color': 'black', 'value': -6},
        'white_pawn': {'symbol': '♙', 'color': 'white', 'value': 1},
        'white_rook': {'symbol': '♖', 'color': 'white', 'value': 2},
        'white_knight': {'symbol': '♘', 'color': 'white', 'value': 3},
        'white_bishop': {'symbol': '♗', 'color': 'white', 'value': 4},
        'white_queen': {'symbol': '♕', 'color': 'white', 'value': 5},
        'white_king': {'symbol': '♔', 'color': 'white', 'value': 6},
    }

    def __init__(self, name: str = 'white_king'):
        """
        Initialize a chess piece object.
        
        Args:
            name (str): The name of the piece, defaults to 'white_king'.
        """
        name = name.lower()
        if name not in self.chess_pieces:
            raise ValueError("Invalid piece name")

        self._name = name

    @property
    def name(self):
        """Get the name of the piece."""
        return self._name

    @property
    def value(self):
        """Get the value of the piece."""
        return self.chess_pieces[self._name]['value']

    @property
    def symbol(self):
        """Get the symbol representing the piece."""
        return self.chess_pieces[self._name]['symbol']
    
    def __str__(self):
        """Return a string representation of the piece."""
        return f"{self.symbol} ({self.name})"


class ChessBoard:
    """
    A class to represent a chessboard.

    Attributes:
        board (list): A 2D list representing the state of the chessboard.
    """

    def __init__(self, data=None):
        """
        Initialize the chessboard with an 8x8 grid.

        Args:
            board (list, optional): A 2D list representing the initial state of the chessboard. Defaults to None.
        """
        # `data` could be a `dict` or a `2D-list`
        # If the `data` is a `dict` then it should be of the form
        # {'a2': ChessPiece('white_pawn'), 'b4': ChessPiece('black_king')}
        self.board = [[None for _ in range(8)] for _ in range(8)]

        if isinstance(data, dict):
            # Add pieces to the self.board
            for square_name, piece in data.items():
                row, col = self.square_name_to_indices(square_name)
                self.board[row][col] = piece

        elif isinstance(data, list):
            self.board = data


    def __str__(self):
        """Return a string representation of the chessboard."""
        board_str = ""
        for row in range(8):
            rank = 8 - row
            board_str += f"{rank}|"
            for col in range(8):
                piece = self.board[row][col]
                if piece is None:
                    board_str += " - "
                else:
                    board_str += f" {piece.symbol} "
            board_str += "\n"

        # Add bottom border and column labels
        board_str += "  -------------------------\n"
        board_str += "   a  b  c  d  e  f  g  h\n"
        return board_str
   

    def set_square(self, file:str, rank:int, piece:ChessPiece):
        """
        Set the piece on the specified square.

        Args:
            file (str): The file of the chessboard (a-h).
            rank (int): The rank of the chessboard (1-8).
            piece (ChessPiece): The chess piece object to be placed on the specified cell.
        """
        files = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        row = 8 - rank
        col = files[file.lower()]

        self.board[row][col] = piece


    def get_piece_at_square(self, square_name: str):
        """
        Get the chess piece at the specified square.

        Args:
            square_name (str): The name of the square (e.g., 'a5').

        Returns:
            ChessPiece or None: The chess piece at the specified square, or None if the square is empty.
        """
        files = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        
        file_index = files.get(square_name[0].lower())
        rank_index = 8 - int(square_name[1])
        
        if file_index is not None and 0 <= rank_index < 8:
            return self.board[rank_index][file_index]
        else:
            return None

    @staticmethod
    def integer_to_square_name(row:int, col:int):
        """
        Convert a pair of integers between 0 and 7 to a valid chess square name.

        Args:
            row (int): The row index (0-7).
            col (int): The column index (0-7).

        Returns:
            str: The square name in algebraic notation (e.g., 'a4', 'h5').
        """
        files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        if row < 0 or row > 7 or col < 0 or col > 7:
            raise ValueError("Row and column indices must be between 0 and 7")

        file = files[col]
        rank = 8 - row

        return file + str(rank)
    
    @staticmethod
    def square_name_to_indices(square_name: str):
        """
        Convert a square name in algebraic notation to row and column indices.

        Args:
            square_name (str): The name of the square (e.g., 'a5').

        Returns:
            tuple: A tuple containing the row index and column index, both ranging from 0 to 7.
        """
        files = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}

        file_index = files.get(square_name[0].lower())
        rank_index = 8 - int(square_name[1])

        if file_index is not None and 0 <= rank_index < 8:
            return rank_index, file_index
        else:
            raise ValueError("Invalid square name")
        

    def get_board_string_representation(self):
        """
        Get the string representation of the current board state.

        Returns:
            list: A 2D list representing the current board state, with each element being the symbol
            of the piece or None if the square is empty.
        """
        board_data = [[None for _ in range(8)] for _ in range(8)]

        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]

                if piece:
                    board_data[row][col] = piece.symbol

        return board_data

    
    def get_integer_board(self):
        """
        Get the integer representation of the current board state.

        Returns:
            list: A 2D list representing the current board state, with each element being 
            the value of the piece or 0 if the square is empty.
        """
        board_data = [[0 for _ in range(8)] for _ in range(8)]

        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]

                if piece:
                    board_data[row][col] = piece.value

        return board_data
    

    @classmethod
    def from_list(cls, board_data):
        """
        Create a ChessBoard instance from a given 2D list representing the board state.

        Args:
            board_data (list): A 2D list representing the board state.

        Returns:
            ChessBoard: A ChessBoard instance initialized with the provided board state.
        """
        # Validate input dimensions
        if len(board_data) != 8 or any(len(row) != 8 for row in board_data):
            raise ValueError("Invalid board dimensions. Board must be 8x8.")

        board = cls()  # Initialize an empty board
        for row_index, row in enumerate(board_data):
            for col_index, piece_value in enumerate(row):
                if piece_value != 0:  # Skip empty squares
                    # Map piece values to ChessPiece names
                    piece_name = next(name for name, data in ChessPiece.chess_pieces.items() if data['value'] == piece_value)
                    piece = ChessPiece(name=piece_name)
                    board.set_square(chr(ord('a') + col_index), 8 - row_index, piece)

        return board


