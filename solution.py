
import numpy as np

def nQueensAll(n):
    if n < 4:
        raise ValueError
    else:
        #Got logic for this function from the lab instructions
        def isSafe(row, col, solution):
            for position in range(len(solution)):
                if col == solution[position][1] or abs(row - solution[position][0]) == abs(col - solution[position][1]):
                    return False
            return True
        def findAllSolutions(n, row, board, solution, allSolutions):
            if row ==  n:
                allSolutions += [list(solution)]
                return
            for col in range (0,n):
                if isSafe(row, col, solution) and board[row][col] == 0:
                    board[row][col] = 1
                    solution += [(row, col)]

                    findAllSolutions(n, row + 1, board, solution, allSolutions)

                    board[row][col] = 0
                    solution.pop()
            return None
        
        board = np.zeros((n,n))
        allSolutions = []
        findAllSolutions(n, 0, board, [], allSolutions)
        return allSolutions

