"""
Tic Tac Toe Player
"""
import tictactoe as ttt
import math

X = "X"
O = "O"
EMPTY = None


board = ttt.initial_state()

player = ttt.player(board)

move = []

for i in range(3):
    for j in range(3):
        if board[i][j] is None:
            avail = (i, j)
            move.append(avail)

# print(move)

action = (1,1)

if action not in move:
    raise IndexError('Invalid move attempted!!')
else:
    print(action)
