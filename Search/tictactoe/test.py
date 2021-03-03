from tictactoe import *
 
board  = initial_state()
'''
for i in range(len(a) + 1):
    for j in range(len(a) + 1):
        if i > 2 or j > 2:
            i =- 1
            j =- 1
        print(player(a))
        if player(a):
            a[i][j] = player(a)  
        print(a)

print(actions(a))
a[1][2] = player(a)  
print(actions(a))
print(a)
print(actions(a))
for action in actions(a):
    print(result(a, action))
    print(winner(a))
'''
board[0][0] = board[1][1] = board[2][2] = 'X'
print(winner(board))
