
import numpy as np


def nQueensAll(n):
    #define internal recursive helper function
    def findSolution(n, row, board, solution):
        if row == n: #we have gone through all of the rows
            return solution
    
        if len(solution) == 0:
            board[row][0] = 1  #col is not defined yet, start at col 0
            solution += [(row, col)]
            findSolution(n, row + 1, board, solution)
    
        for col in range(0,n): #we check every column in each row
            #got logic for the diagonal check from the lab instructions
            if board[row][col] == 0 and (abs(row - solution[-1][0]) != abs(col - solution[-1][1])):
                board[row][col] = 1
                solution += [(row, col)]
                findSolution(n, row + 1, board, solution)

                #backtracking has to be here as the previous recursive call will return here after failure (when we need to backtrack)
                board[row][col] = 0
                solution.pop()
    if n < 4:
        raise ValueError
    else:
        board = np.zeros((n,n)) # making the matrix representation of the board
        solutions = []
        for row in range(0,n): 
            currSolution = findSolution(n,row,board,currSolution)
            solutions += [currSolution]
        return solutions
        


