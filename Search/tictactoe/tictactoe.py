"""
T ic Tac Toe Player
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
        return "O"
    else:
        return None


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
    
    # row checking
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2] != None:
            return board[i][0]
    # col checking
    for i in range(len(board)):
        if board[0][i] == board[1][i] == board[2][i] != None:
            return board[0][i]

    # diagnol checking
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] != None:
            return board[0][0]

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] != None:
            return board[0][2]

    return None

    #
    # optimize the whole winner function
    #


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == None:
        for i in board:
            for j in i:
                if j == None:
                    return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)
    if winner_player == "X":
        return 1
    elif winner_player == "O":
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    if terminal(board):
        return None


    Max = -math.inf
    Min = math.inf


    if player(board) == "X":
        value, action = max_value(board, Max, Min)
    else:
        value, action = min_value(board, Max, Min)

    return action


def min_value(board, Max, Min):
    if terminal(board):
        return [utility(board), None]
    value = math.inf
    for action in actions(board):
        m_value, _ = max_value(result(board, action), Max, Min)
        Min = min(Min, m_value)
        if m_value < value:
            value = m_value
            optimal_action = action
        if Max >= Min:
            break
    print("min_value: ", value, optimal_action, "Max:", Max, "Min:", Min)
    return [value, optimal_action]

def max_value(board, Max, Min):
    if terminal(board):
        return [utility(board), None]
    value = -math.inf
    for action in actions(board):
        m_value, _ = min_value(result(board, action), Max, Min)
        Max = max(Max, m_value)
        if m_value > value:
            value = m_value
            optimal_action = action
        if Max >= Min:
            break
    print("max_value: ", value, optimal_action, "Max:", Max, "Min:", Min)
    return [value, optimal_action]
