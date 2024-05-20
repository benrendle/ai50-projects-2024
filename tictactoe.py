"""
Tic Tac Toe Player
"""

import math

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
    # Initialise counters for players
    nX = 0 # X counter
    nO = 0 # O counter
    nN = 0 # None Counter

    # Scan the grid for number of turns taken
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                nX += 1
            if board[i][j] == 'O':
                nO += 1
            if board[i][j] is None:
                nN += 1
    # If a count of 9 is achieved for nN, game is in initial state and X goes first
    if nN == 9:
        return 'X'
    if nX == nO:
        return 'X'
    if nO < nX:
        return 'O'


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    move = []

    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                 empty = (i, j)
                 move.append(empty)

    return move

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    Raise exception is move is not valid!
    Take input board, apply move, return new game state board
    Make a deep copy of the board first! Need to preserve the original implementation for minmax searching algorithm to work
    Make a new board parameter to store the modified output board
    """
    # raise NotImplementedError
    valid = actions(board)
    if action in valid:
        raise IndexError('Invalid move attempted!!')
    else:
        print('Game on')
#         implement code


def winner(board):
    """
    Returns the winner of the game, if there is one.
    Return X, O or None
    Need to check for winning state and confirm the winner
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    Should check the board after iteration
    Default state is to continue, otherwise call winner function
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    Takes terminal board as input
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    Algorithm for the AI to pick the best move available to it
    """
    raise NotImplementedError
