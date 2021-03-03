"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


class Error(Exception):
    def __init__(self, msg="Error"):
        self.msg = msg
        super().__init__(self.msg)
    def __str__(self):
        return self.msg

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
    for i in board:
        for j in i:
            if j == X:
                x += 1
            if j == O:
                o += 1

    if x + o < 9:

        if x == 0 and o == 0 or x == o:
            return X
        elif x > 0:
            return O

    return None

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = []

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                moves.append((i, j))

    #return moves if len(moves) else None
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = deepcopy(board)
    i, j = action

    if new_board[i][j] != EMPTY:
        raise Error("Invalid Action")

    new_board[i][j] = player(new_board)
    return new_board 


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(len(board)):
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
    
    if board[0][0] == board[1][1] == board[2][2] or board[2][0] == board[1][1] == board[0][2]:
        return board[1][1]

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    for i in board:
        for j in i:
            if j == EMPTY and not winner(board):
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if X == winner(board):
        return 1
    elif O == winner(board):
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    current_player = player(board)
    print(current_player)
    if current_player == X:
        return max_value(board)[1]
    elif current_player == O:
        return min_value(board)[1]
    return None


def max_value(board):
    v = (float("-inf"), ())

    if terminal(board):
        return (utility(board), ())

    for action in actions(board):
        m = min_value(result(board, action))[0]
        print("Max", v, m, type(m))
        v = max(v, (m, action), \
                key = lambda x: x[0])
    return v

 
def min_value(board):
    v = (float("inf"), ())

    if terminal(board):
        return (utility(board), ())

    for action in actions(board):
        m = max_value(result(board, action))[0]
        print("Min", v, m, type(m))
        v = min(v, (m, action), \
                key = lambda x: x[0])
    return v

