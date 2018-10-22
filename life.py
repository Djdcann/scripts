import numpy as np

c = 20
board = np.zeros((c,c))
current = np.copy(board)
board[0,1] = 1
# if board[0,1]: print(board)

def neighbors(x, y):
    x1 = x-1 if x else x
    y1 = y-1 if y else y
    x2 = x+1 if x+1 < c else x
    y2 = y+1 if y+1 < c else y
    return np.sum(board[x1:x2+1, y1:y2+1])

def getNextVal(x, y):
    n = neighbors(x, y)
    if n < 2:
        return 0
    elif n < 5:
        return 1
    else:
        return 0

def step():
    global board
    for i in range(c):
        for j in range(c):
            current[i, j] = getNextVal(i, j)

    board = current
    print(current)

print(board)
for i in range(1, 21):
    print('%d.' % i)
    step()
