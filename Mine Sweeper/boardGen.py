import random


class gridSquare():
	
	def __init__(self):
		self.is_Mine = 0
		self.adjBombCount = 0
	
	#Creates a board for us to use with random mines
	def create_board(self, cols, rows, numMines):
		grid = []
		for r in range(rows):
			row = []
			for c in range(cols):
				row.append(gridSquare())
			grid.append(row)
		#set The Mines At Random Positions
		for i in range(0, numMines):
			row = random.randint(0, rows-1)
			col = random.randint(0, cols-1)
			while (grid[row][col].is_Mine):
				row = random.randint(0, rows-1)
				col = random.randint(0, cols-1)
			grid[row][col].is_Mine = 1
			
		#set the bombcount for adjacent bombs
		for j in range(0, rows):
			for k in range(0, cols):
				grid = self.set_bombCount(grid, j, k, cols, rows);
		return grid; 
	
	#sets the bomb count of a particular square
	def set_bombCount(self, grid, row, col, maxCol, maxRow):
		if (row == 0):
			if (col == 0):
				if (grid[row][col+1].is_Mine):
					grid[row][col].adjBombCount += 1
				if (grid[row+1][col].is_Mine):
					grid[row][col].adjBombCount += 1
				if (grid[row+1][col+1].is_Mine):
					grid[row][col].adjBombCount += 1
			elif (col == maxCol-1):
				if (grid[row][col-1].is_Mine):
					grid[row][col].adjBombCount += 1
				if (grid[row+1][col].is_Mine):
					grid[row][col].adjBombCount += 1
				if (grid[row+1][col-1].is_Mine):
					grid[row][col].adjBombCount += 1
			else:
				if (grid[row][col-1].is_Mine):
					grid[row][col].adjBombCount += 1
				if (grid[row][col+1].is_Mine):
					grid[row][col].adjBombCount += 1
				if (grid[row+1][col].is_Mine):
					grid[row][col].adjBombCount += 1
				if (grid[row+1][col-1].is_Mine):
					grid[row][col].adjBombCount += 1
				if (grid[row+1][col+1].is_Mine):
					grid[row][col].adjBombCount += 1
		elif (row == maxRow-1):
			if (col == 0):
				if (grid[row][col+1].is_Mine):
					grid[row][col].adjBombCount += 1
				if (grid[row-1][col].is_Mine):
					grid[row][col].adjBombCount += 1
				if (grid[row-1][col+1].is_Mine):
					grid[row][col].adjBombCount += 1
			elif (col == maxCol-1):
				if (grid[row][col-1].is_Mine):
					grid[row][col].adjBombCount += 1
				if (grid[row-1][col].is_Mine):
					grid[row][col].adjBombCount += 1
				if (grid[row-1][col-1].is_Mine):
					grid[row][col].adjBombCount += 1
			else:
				if (grid[row][col-1].is_Mine):
					grid[row][col].adjBombCount += 1
				if (grid[row][col+1].is_Mine):
					grid[row][col].adjBombCount += 1
				if (grid[row-1][col].is_Mine):
					grid[row][col].adjBombCount += 1
				if (grid[row-1][col-1].is_Mine):
					grid[row][col].adjBombCount += 1
				if (grid[row-1][col+1].is_Mine):
					grid[row][col].adjBombCount += 1
		else:
			if (col == 0):
				if (grid[row][col+1].is_Mine):
					grid[row][col].adjBombCount += 1
				if (grid[row+1][col].is_Mine):
					grid[row][col].adjBombCount += 1
				if (grid[row+1][col+1].is_Mine):
					grid[row][col].adjBombCount += 1
				if (grid[row-1][col+1].is_Mine):
					grid[row][col].adjBombCount += 1
				if (grid[row-1][col].is_Mine):
					grid[row][col].adjBombCount += 1
			elif (col == maxCol-1):
				if (grid[row][col-1].is_Mine):
					grid[row][col].adjBombCount += 1
				if (grid[row+1][col].is_Mine):
					grid[row][col].adjBombCount += 1
				if (grid[row+1][col-1].is_Mine):
					grid[row][col].adjBombCount += 1
				if (grid[row-1][col-1].is_Mine):
					grid[row][col].adjBombCount += 1
				if (grid[row-1][col].is_Mine):
					grid[row][col].adjBombCount += 1
			else:
				if (grid[row][col-1].is_Mine):
					grid[row][col].adjBombCount += 1
				if (grid[row][col+1].is_Mine):
					grid[row][col].adjBombCount += 1
				if (grid[row-1][col].is_Mine):
					grid[row][col].adjBombCount += 1
				if (grid[row+1][col].is_Mine):
					grid[row][col].adjBombCount += 1	
				if (grid[row+1][col-1].is_Mine):
					grid[row][col].adjBombCount += 1
				if (grid[row-1][col-1].is_Mine):
					grid[row][col].adjBombCount += 1
				if (grid[row+1][col+1].is_Mine):
					grid[row][col].adjBombCount += 1
				if (grid[row-1][col+1].is_Mine):
					grid[row][col].adjBombCount += 1	
		return grid;				
	#returns contents of the board square
	def reveal(self, gridSquare):
		if (gridSquare.is_Mine):
			return "X"
		else:
			return str(gridSquare.adjBombCount)
