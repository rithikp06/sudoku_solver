import random

class Sudoku:
    size = 9
    def __init__(self, puzzle):
        self.board = puzzle

    def print(self):
        for row in range(self.size):
            if row % 3 == 0:
                print("-------------------------------")
            s = ""
            for col in range(self.size):
                if col % 3 == 0:
                    s += "|"
                if(self.board[row][col] != 0):
                    s += " " + str(self.board[row][col]) + " "
                else:
                    s += " . "
            s += "|"
            print(s)
        print("-------------------------------")

    def isValid(self, row, col):
        value = self.board[row][col]
        for i in range(self.size):
            if (i == row):
                continue
            temp = self.board[i][col]
            if (temp == value):
                return False

        for i in range(self.size):
            if (i == col):
                continue
            temp = self.board[row][i]
            if (temp == value):
                return False

        box_row = int(row / 3)
        box_col = int(col / 3)

        for i in range(box_row*3, box_row*3 +3):
            for j in range(box_col*3, box_col*3 +3):
                if (i == row and j == col):
                    continue
                temp = self.board[i][j]
                if (temp == value):
                    return False
        return True

    def nextSolve(self, row, col):
        i = 0
        for j in range(row, self.size):
            if j == row:
                i = col
            else:
                i = 0
            while i < self.size:
                if(self.board[j][i] == 0) and (j != row or i != col):
                    return j, i
                i += 1
        return 9, col

    def solveHelper(self, row, col):
        if row > 8:
            return True
        nextR, nextC = self.nextSolve(row, col)
        orig = self.board[row][col]
        for i in range(1, self.size+1):
            self.board[row][col] = i
            if self.isValid(row,col) == True:
                good = self.solveHelper(nextR, nextC)
                if good == True:
                    return True
        self.board[row][col] = orig
        return False

    def solve(self):
        self.solveHelper(0,0)

    def verify(self):
        pass

def puzzle_generator():
    puzzle = []
    for i in range(9):
        puzzle.append([])
        for j in range(9):
            puzzle[i].append(0)

    for i in range(9):
        poss = all_vals
        for j in range(9):


def get_vals(puzzle, row, col):
    all_vals = [1,2,3,4,5,6,7,8,9]
    for i in range(row):
        all_vals.remove(puzzle[i][col])
    for i in range(col):
        all_vals.remove(puzzle[row][i])
    return all_vals
