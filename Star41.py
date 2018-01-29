class Grid:
	
	def __init__(self):
		self.map = []
		self.map.append([".", "#", "."])
		self.map.append([".", ".", "#"])
		self.map.append(["#", "#", "#"])
		self.size = 3
	
	def __init__(self, gridString):
		gridString_splitted = gridString.split("/")
		self.map = []
		for gs in gridString_splitted:
			map.append(gs.split(""))
		self.size = len(self.map)
		
	def flipHorizontal(self):
		new_map = self.map.copy()
		for i in range(self.size / 2):
			for j in range(self.size):
				temp = new_map[j][i]
				new_map[j][i] = new_map[-(j+1)][i]
				new_map[-(j+1)][i] = new_map[j][i]
		return Grid(self.toString(new_map))
		
	def flipVertical(self):
		new_map = self.map.copy()
		for i in range(self.size / 2):
			temp = self.new_map[i]
			self.new_map[i] = self.new_map[-(i+1)]
			self.new_map[-(i+1)] = temp
		return Grid(self.toString(new_map))
		
	def rotateClockwise(self):
		new_map = self.map.copy()
		rows = []
		for i in range(self.size):
			temp = []
			for j in range(self.size):
				temp.append(new_map[i][j])
			rows.append(temp)
		for i in range(self.size):
			for j in range(self.size):
				new_map[j][i] = rows[self.size - i - 1][j]
		return Grid(self.toString(new_map))
		
	def toString(self):
		returning = ""
		for m in range(self.size):
			for n in range(self.size):
				returning += self.map[m][n]
			if m != self.size - 1:
				returning += "/"
		return returning
				
	def toString(self, new_map):
		returning = ""
		for m in range(self.size):
			for n in range(self.size):
				returning += new_map[m][n]
			if m != self.size - 1:
				returning += "/"
		return returning
		
	def equals(self, another_grid_string):
		return toString() == another_grid_string
		
	def divideGrid(self):
		divided_grids = []
		if self.size % 2 == 0:
			for i in self.size / 2:
				for j in self.size / 2:
					
			return self.size / 2, divided_grids
		else if self.size % 3 == 0:
			
			return self.size / 3, divided_grids
		else:
			return -1, divided_grids
		
	def getRow(self, row_num):
		return self.map[row_num]

def readFileAndGetRules(file_name):
	rules = dict([])
	for line in open(file_name, 'r'):
		line_splitted = line.split(" => ")
		rules[line_splitted[0]] = rules[line_splitted[1]]
	return rules
		
def getCombinationGrids(grid):
	combin_grids = []
	for i in range(4):
		combin_grids.append(grid)
		combin_grids.append(grid.flipHorizontal())
		combin_grids.append(grid.flipVertical())
		grid = grid.rotateClockwise()
	return combin_grids
			
def runIterations(num_iterations, rules):
	start_grid = Grid()
	for i in range(num_iterations):
		
#Assuming nxn, not mxn grid...	
def combineGrids(num_grids_per_side, grids):
	full_grid_string = ""
	for g in grids: