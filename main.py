import sudoku

size = 9

puzzle = [[1,0,0,0,0,7,0,9,0],
		 [0,3,0,0,2,0,0,0,8],
		 [0,0,9,6,0,0,5,0,0],
		 [0,0,5,3,0,0,9,0,0],
		 [0,1,0,0,8,0,0,0,2],
		 [6,0,0,0,0,4,0,0,0],
		 [3,0,0,0,0,0,0,1,0],
		 [0,4,0,0,0,0,0,0,7],
         [0,0,7,0,0,0,3,0,0]]
s = sudoku.Sudoku(puzzle)
s.solve()
s.print()

puzzle = [[0,9,0,3,0,0,0,0,1],
         [0,0,0,0,8,0,0,4,6],
         [0,0,0,0,0,0,8,0,0],
         [4,0,5,0,6,0,0,3,0],
         [0,0,3,2,7,5,6,0,0],
         [0,6,0,0,1,0,9,0,4],
         [0,0,1,0,0,0,0,0,0],
         [5,8,0,0,2,0,0,0,0],
         [2,0,0,0,0,7,0,6,0]]
s = sudoku.Sudoku(puzzle)
s.solve()
s.print()

puzzle = [[0,0,0,0,0,3,2,9,0],
         [0,8,6,5,0,0,0,0,0],
         [0,2,0,0,0,1,0,0,0],
         [0,0,3,7,0,5,1,0,0],
         [9,0,0,0,0,0,0,0,8],
         [0,0,2,9,0,8,3,0,0],
         [0,0,0,4,0,0,0,8,0],
         [0,0,0,0,0,6,4,7,0],
         [0,4,7,1,0,0,0,0,0]]
s = sudoku.Sudoku(puzzle)
s.solve()
s.print()
