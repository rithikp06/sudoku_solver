import random
import sudoku
from copy import deepcopy

# generates a puzzle
def generate_puzzle():
    puzzle = []
    # 9x9 2d array of 0s
    for i in range(9):
        puzzle.append([])
        for j in range(9):
            puzzle[i].append(0)

    # generates a completely solved puzzle
    for i in range(9):
        for j in range(9):
            vals = get_vals(puzzle, i,j)
            puzzle = set_val(puzzle, vals, i, j)
            s = sudoku.Sudoku(puzzle)

    # randomly removes numbers from puzzle (by replaceing them with 0)
    for i in range(9):
        for j in range(9):
            n = random.randint(0,10)
            if n <= 5:
                puzzle[i][j] = 0
    return puzzle



# gets a list of all possible values (based on rows/columns/boxes)
def get_vals(puzzle, row, col):
    all_vals = [1,2,3,4,5,6,7,8,9]
    for i in range(row):
        try:
            all_vals.remove(puzzle[i][col])
        except:
            continue
    for i in range(col):
        try:
            all_vals.remove(puzzle[row][i])
        except:
            continue

    box_row = int(row / 3)
    box_col = int(col / 3)
    for i in range(box_row*3, box_row*3 +3):
        for j in range(box_col*3, box_col*3 +3):
            if (i == row and j == col):
                continue
            try:
                all_vals.remove(puzzle[i][j])
            except:
                continue

    return all_vals

# uses backtracking algorithm to find solvable board with one more number on it
def set_val(puzzle, all_vals, row, col):
    n = random.randint(0, len(all_vals))
    orig = deepcopy(puzzle)
    # randomly chooses a number and checks if it can be used
    # if not checks next number in all_vals
    k = len(all_vals)
    for i in range(n, n+k):
        puzzle = deepcopy(orig)
        j = i % k
        try:
            puzzle[row][col] = all_vals[j]
        except:
            print("exception")
            continue
        s = sudoku.Sudoku(puzzle)
        s.solve()
        if s.is_solved():
            puzzle = deepcopy(orig)
            puzzle[row][col] = all_vals[j]
            s = sudoku.Sudoku(puzzle)
            return puzzle
    puzzle = deepcopy(orig)
    puzzle[row][col] = 0
    return puzzle
