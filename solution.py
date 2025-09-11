
import numpy as np
from collections import deque


#Got code for this from the instructions
def onSameDiagonal(row1, row2, col1, col2):
    if abs(row1 - row2) == abs(col1 - col2):
        return True
    return False

 


def nQueensAll(n):
    if n < 4:
        raise ValueError
    else:
        board = np.zeros((n,n)) # making the matrix representation of the board
        placedQueens = deque()
        occupiedRows = []
        occupiedCols = []
        for row in range (0,n): #iterate through rows
            if row in occupiedRows:
                break
            for col in range(0,n): #iterate through cols
                if col in occupiedCols:
                    break 
                if board[row][col] == 0:
                    if placedQueens.isEmpty():
                        continue
                    else:
                        if abs(row - placedQueens[-1][0]) == abs(col - placedQueens[-1][1]):
                            break
                        else:
                            board[row][col] = 1
                            occupiedRows += [row]
                            occupiedCols += [col]
                            placedQueens.append((row,col))
        #go back to the last queen in the queue and save her old position (mark as unavailible) and find a new one
        #   implement this using a helper function?
        return
    



