"""
A grid is a perfect starting point for many games (Chess, battleships, Candy Crush!).

Making a digital chessboard I think is an interesting way of visualising how loops can work together.

Your task is to write a function that takes two integers rows and columns and returns a chessboard pattern as a two dimensional array.

So chessBoard(6,4) should return an array like this:

[
    ["O","X","O","X"],
    ["X","O","X","O"],
    ["O","X","O","X"],
    ["X","O","X","O"],
    ["O","X","O","X"],
    ["X","O","X","O"]
]
And chessBoard(3,7) should return this:

[
    ["O","X","O","X","O","X","O"],
    ["X","O","X","O","X","O","X"],
    ["O","X","O","X","O","X","O"]
]
The white spaces should be represented by an: 'O'

and the black an: 'X'

The first row should always start with a white space 'O'

"""

def chess_board(rows, columns):
    board = []
    row1 = []
    row2 = []
    
    for _ in range(columns):
        if _ % 2 == 0:
            row1.append('O')
            row2.append('X')
        if _ % 2 != 0:
            row1.append('X')
            row2.append('O')
    
    for _ in range(rows):
        if _ % 2 == 0:
            board.append(row1)
        if _ % 2 != 0:
            board.append(row2)
            
    return board


# easier way of writing it

def chess_board(rows, columns):
    board = []
    for row in range(rows):
        if row % 2:
            board.append(["X" if not column % 2 else "O" for column in range(columns)])
        else:
            board.append(["O" if not column % 2 else "X" for column in range(columns)])
    return board