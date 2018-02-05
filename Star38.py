
# Function that takes an input file and builds the map 	
def build_map(file_name):
    # Build the map 
	map = []
	for line in open(file_name, 'r'):
		temp = []
		for l in line:
			temp.append(l)
		map.append(temp)
    
    # Find the starting position of the map
	start = None
	for i in range(len(map[0])):
		if map[0][i] == "|":
			start = i
			break
	return map, (0, int(start))

# Function that gets the possible moves that the packet can move to if not forward
def getPossibleMoves(map, current_direction, coord):
    # Get the directions that the packet can turn to or continue in 
    possible_moves = dict([]) 
    if current_direction == "N" or current_direction == "S":
        possible_moves["E"] = None
        possible_moves["W"] = None
    else:  
        possible_moves["N"] = None 
        possible_moves["S"] = None
    
    # Check if the move is valid, otherwise delete the dictionary entry
    for dir in possible_moves.keys():
        if checkMovingForward(map, coord, dir):
            possible_moves[dir] = move(coord, dir, map)
        else:
            del possible_moves[dir]
    return possible_moves

# Function that checks to see if the next coordinate in the direction is valid	
def checkMovingForward(map, coord, direction):
	new_coord = move(coord, direction, map)
	if new_coord == (-1,-1):
		return False
	if map[new_coord[0]][new_coord[1]] != " ":
		return True
	return False

# Helper function that checks if coordinates are out of bounds
def checkOutofBounds(coord, map):
	if coord[0] < 0 or coord[1] < 0 or coord[0] >= len(map[0]) or coord[1] >= len(map):
		return True
	return False

# Function that returns the new coordinates of the packet given the direction and a valid movement    
def move(coord, direction, map):
	new_coord = [coord[0], coord[1]]
	if direction == "S":
		new_coord[1] += 1
	elif direction == "N":
		new_coord[1] -= 1
	elif direction == "W":
		new_coord[0] -= 1
	else:
		new_coord[0] += 1
	if checkOutofBounds(coord, map):
		return (-1,-1)
	return (new_coord[0], new_coord[1])

# Function that runs the packet through the routing diagram and returns the letters visited after completion    
def runPath(map, start):
    # Track the current coordinates, begin the direction going South
    coord = start
    direction = "S"
    
    # Tracks the steps taken
    count = 0
    
    # Continue until there are no more possible moves
    while True:
        count += 1
        # See if the packet can continue in the same direction 
        if checkMovingForward(map, coord, direction):
            coord = move(coord, direction, map)
        else:
            # Otherwise, get all the possible moves the packet can do
            possible_moves = getPossibleMoves(map, direction, coord)
            if len(possible_moves) == 0:
                break		
            
            # Get the possible direction 
            for dir in possible_moves.keys():
                coord = possible_moves[dir]
                direction = dir
                break
    return count
			
map, start = build_map("star37_input.txt")
numSteps = runPath(map, start)
print "Number of steps taken by the packet = ", numSteps