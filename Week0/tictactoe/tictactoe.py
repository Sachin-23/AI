"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x = 0
    o = 0
    empty = 0 
    for i in board:
        for j in i:
            if j == "X":
                x += 1
            elif j == "O":
                o += 1
    if x == o or (x == 0 and o == 0):
        return "X"
    elif x > o:
        return "Y"
    else:
        return None

"""
total : 9
empty|empty|empty
empty|empty|empty
empty|empty|empty
x = 0
y = 0

  x  |empty|  x
empty|  y  |empty
empty|empty|empty

y = 1
x = 1
"""


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set() 
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == None:
                actions_set.add((i, j)) 
    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    current_player = player(board)
    current_board = deepcopy(board)
    if len(action) == 2:
        current_board[action[0]][action[1]] = current_player
        return current_board
    else:
        raise Exception("Invalid Action")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    current_player = player(board)
    if current_player == "X":
        prev_player = Y
    elif current_player == "Y":
        prev_player = X
    else:
        raise Exception("Invalid Board from winner function")
    
    # row checking
    for i in range(len(Board)):
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
    # col checking
    for i in range(len(Board)):
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]

    # diagnol checking
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]

    if board[2][2] == board[1][1] == board[0][0]:
        return board[0][0]


    #
    # optimize the whole winner function and check the player thing
    #


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
