
import numpy as np
from collections import deque

def findSolution(n, row, board, solution):
    if row == n: #we have gone through all of the rows
        return solution
    
    if len(solution) == 0:
        board[row][col] = 1
        solution += [(row, col)]
        findSolution(n, row + 1, board, solution)
    
    for col in range(0,n): #we check every column in each row
        #got logic for the diagonal check from the lab instructions
        if board[row][col] == 0 and (abs(row - solution[-1][0]) != abs(col - solution[-1][1])):
            board[row][col] = 1
            solution += [(row, col)]
            findSolution(n, row + 1, board, solution)

            board[row][col] = 0
            solution.pop()

def nQueensAll(n):
    if n < 4:
        raise ValueError
    else:
        board = np.zeros((n,n)) # making the matrix representation of the board
        solutions = []
        for row in range(0,n): 
            currSolution = []
            currSolution = findSolution(n,row,board,currSolution)
            solutions += [currSolution]
        return solutions
        #placedQueens = deque()
        #occupiedRows = []
        #occupiedCols = []
        #while len(placedQueens) != n - 1: #go through and fix logic, you are infintely looping some places
        #    for row in range (1,n): #iterate through rows starting at 1 as position 0,0 will never allow for any subsequent valid queen placement
        #        if row in occupiedRows:
        #            break
        #        for col in range(0,n): #iterate through cols
        #            if col in occupiedCols:
        #                break 
        #            if board[row][col] == 0:
        #                if placedQueens.isEmpty():
        #                   board[row][col] = 1
        #                   occupiedRows += [row]
        #                   occupiedCols += [col]
        #                   placedQueens.append((row,col)) 
        #                   break
        #                else:
                            #pulled the code logic from the lab instructions
        #                    if abs(row - placedQueens[-1][0]) == abs(col - placedQueens[-1][1]):
        #                        break
        #                    else:
        #                        board[row][col] = 1
        #                        occupiedRows += [row]
        #                        occupiedCols += [col]
        #                        placedQueens.append((row,col))
            #need to save the current position of the queen and disallow it from being chosen again
        #    oldQueen = placedQueens.pop()
        #    occupiedRows.remove(oldQueen[0])
        #    occupiedCols.remove(oldQueen[1])
        #    board[oldQueen[0]][oldQueen[1]] = 0
            #go back to the last queen in the queue and save her old position (mark as unavailible) and find a new one
            #   implement this using a helper function? (extract lines 14-30?)
        #add the placedQueens values in a list, then add that list to the solutions list, move on to creating a new solution
        #may need to extract the placement logic code and make it a helper function and then call it recursively
        #return solutions



