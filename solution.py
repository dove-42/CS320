
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
        queenQueue = deque() #creating queue to hold already placed queens
        occupiedRows = []
        occupiedCols = []
        for row in range (0,n): #iterate through rows
            if row in occupiedRows:
                break
            for col in range(0,n): #iterate through cols
                if col in occupiedCols:
                    break 
                if board[row][col] == 0:
                    #check diagonal is good
                    board[row][col] = 1
                    occupiedRows += row
                    occupiedCols += col
        return
    



