class Sudoku:
    size = 9
    def __init__(self, puzzle):
        self.board = puzzle

    #prints the puzzle to the terminal
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

    # checks if a row,col combination is valid
    def isValid(self, row, col):
        value = self.board[row][col]

        # makes sure value is not repeated in the row and col
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

        # makes sure values are not repeated in the 3x3 square
        for i in range(box_row*3, box_row*3 +3):
            for j in range(box_col*3, box_col*3 +3):
                if (i == row and j == col):
                    continue
                temp = self.board[i][j]
                if (temp == value):
                    return False

        # all tests have been passed
        return True

        # gets the index (row, col) for the next square that must be solved
    def nextSolve(self, row, col):
        i = 0

        # finds the next square with 0 in it
        for j in range(row, self.size):
            if j == row:
                i = col
            else:
                i = 0
            while i < self.size:
                if(self.board[j][i] == 0) and (j != row or i != col):
                    return j, i
                i += 1

        # entire board has been solved already
        return 9, col

    # helper function for solve
    # tries every possible number in a square (backtracking if necessary)
    def solveHelper(self, row, col):
        if row > 8:
            return True
        nextR, nextC = self.nextSolve(row, col)
        orig = self.board[row][col]

        for i in range(1, self.size+1):
            self.board[row][col] = i
            if self.isValid(row,col) == True:
                good = self.solveHelper(nextR, nextC)
                # if good is false unsolvable --> backtrack
                if good == True:
                    return True
        # changes board back to what it was before
        self.board[row][col] = orig
        # unsolvable due to previous move so return false
        return False

    def solve(self):
        r,c = self.nextSolve(0, 0)
        self.solveHelper(r,c)

    def is_solved(self):
        for i  in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return False
        return True
