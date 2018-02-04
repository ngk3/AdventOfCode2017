
# class to represent a Grid of lights
class Grid:
	
    # Initializes a grid based on a gridstring (look at input file to see gridstring format)
    def __init__(self, gridString = ".#./..#/###"):
        gridString_splitted = gridString.split("/")
        self.map = []
        for gs in gridString_splitted:
            temp = []
            for g in gs:
                temp.append(g)
            self.map.append(temp)
        self.size = len(self.map)
	
    # Function that returns a copy of the Grid's map
    def copyMap(self):
        new_map = []
        for i in range(self.size):
            temp = []
            for j in range(self.size):
                temp.append(self.map[i][j])
            new_map.append(temp)
        return new_map
    
    # Function used to flip the Grid horizontally and return a new flipped Grid
    def flipHorizontal(self):
        new_map = self.copyMap()
        for i in range(self.size):
            for j in range(self.size / 2):
                temp = new_map[i][j]
                new_map[i][j] = new_map[i][-(j+1)]
                new_map[i][-(j+1)] = temp
        return Grid(toString(new_map))
    
    # Function used to flip the Grid vertically and return a new flipped Grid		
    def flipVertical(self):
        new_map = self.copyMap()
        for i in range(self.size / 2):
            temp = new_map[i]
            new_map[i] = new_map[-(i+1)]
            new_map[-(i+1)] = temp
        return Grid(toString(new_map))
	
    # Function used to rotate the Grid clockwise and return the new rotated Grid
    def rotateClockwise(self):
        new_map = self.copyMap()
        rows = []
        for i in range(self.size):
            temp = []
            for j in range(self.size):
                temp.append(new_map[i][j])
            rows.append(temp)
        for i in range(self.size):
            for j in range(self.size):
                new_map[j][i] = rows[self.size - i - 1][j]
        return Grid(toString(new_map))
	
    # Function used to create and return the gridstring representation of the Grid
    def toString(self):
        returning = ""
        for m in range(self.size):
            for n in range(self.size):
                returning += self.map[m][n]
            if m != self.size - 1:
                returning += "/"
        return returning
	
    # Helper Function to divide the map from start_x - start_x + size, start_y - start_y + size grid
    def divideMap(self, start_x, start_y, size):
        returning_map = []
        for i in range(start_x, start_x+size):
            column = []
            for j in range(start_y, start_y+size):
                column.append(self.map[i][j])
            returning_map.append(column)
        return toString(returning_map)
    
    # Function that divides the grid according to the ruleset and return the gridstring of each division in a list[columns] format
    def divideGrid(self):
        divided_grids = []
        division_num = 3
        if self.size % 2 == 0:
            division_num = 2
            
        tracker_y = 0
        while (tracker_y < self.size):
            addition = []
            tracker_x = 0
            while (tracker_x < self.size):
                addition.append(self.divideMap(tracker_x, tracker_y, division_num))
                tracker_x += division_num
            divided_grids.append(addition)
            tracker_y += division_num 
        return divided_grids;      

    # Function used to print the Grid as a Map
    def printMap(self):
        for i in range(self.size):
            temp = ""
            for j in range(self.size):
                temp += self.map[i][j]
            print temp
        print
    
    # Function used to count and return the number of pixels that are on
    def getNumOn(self):
        count = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.map[i][j] == "#":
                    count += 1
        return count
        
# Function to return the gridstring representation of a grid Map
def toString(new_map):
    returning = ""
    for m in range(len(new_map)):
        for n in range(len(new_map)):
            returning += new_map[m][n]
        if m != len(new_map) - 1:
            returning += "/"
    return returning
        
# Function used to read the input file and get all the image creation rules
def readFileAndGetRules(file_name):
    rules = dict([])
    for line in open(file_name, 'r'):
        line_splitted = line.strip().split(" => ")
        rules[line_splitted[0]] = line_splitted[1]
    return rules

# Function that returns a list of possible grid transformations of a Grid    
def getCombinationGrids(grid):
    combin_grids = []
    for i in range(4):
        combin_grids.append(grid)
        combin_grids.append(grid.flipHorizontal())
        combin_grids.append(grid.flipVertical())
        grid = grid.rotateClockwise()
    return combin_grids
	
# Function that translate the list of divided grids based on the given ruleset	
def translateGrids(rules, list_divided_grids):
    for i in range(len(list_divided_grids)):
        for j in range(len(list_divided_grids)):
            grid_rep = getCombinationGrids(Grid(list_divided_grids[i][j]))
            for g in grid_rep:
                try:
                    list_divided_grids[i][j] = rules[g.toString()]
                    break 
                except:
                    continue

# Function that takes a list of divided grids and combines them into a gridstring                        
def combineGrids(list_divided_grids):
    # Initializes the dictionary to get the gridstrings of each row 
    combined_grid = dict([])
    tracker = 1
    for col in list_divided_grids[0]:
        for col_splitted in col.split("/"):
            combined_grid[tracker] = ""
            tracker += 1

    # Get the gridstrings of each row         
    for col in list_divided_grids:
        tracker = 1
        for c in col:
            for c_splitted in c.split("/"):
                combined_grid[tracker] += c_splitted 
                tracker += 1
    
    start = time.time()
    # Return the combined gridstring 
    returning_string = "";
    for cg in range(1, len(combined_grid) + 1):
        returning_string += combined_grid[cg]
        if cg != len(combined_grid):
            returning_string += "/"   
    return returning_string

# Function that takes in the number of iterations and the rule input file and returns the number of lights on in the end image
def runIterations(num_iterations, input_file):
    # Get the rules and initialize the grid 
    rules = readFileAndGetRules(input_file)
    start_grid = Grid()
    
    # Run through division, translation, and combination of grids num_iteration times
    for i in range(num_iterations):
        divided_grids = start_grid.divideGrid()
        translateGrids(rules, divided_grids)
        start_grid = Grid(combineGrids(divided_grids))
        
    # Return the number of lights on in the grid
    return start_grid.getNumOn()    
            
print "Number of lights on after 18 iterations = ", runIterations(18, "Star41_input.txt")
