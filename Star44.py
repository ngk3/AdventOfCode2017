
# Function that reads the file and generates the map in the file, returning the size of the map
def readFileandGenerateMap(file_name):
    map = dict([])
    x = 1
    y = 1
    for line in open(file_name, 'r'):
        x = 1
        for l in line.strip():
            map[str(x) + "," + str(y)] = l
            x += 1
        y += 1
    return x-1, y-1, map

# Function that determines the new direction of the virus carrier
def changeDirection(direction, turning):
	if turning == "L":
		if direction == "N":
			return "W"
		elif direction == "W":
			return "S"
		elif direction == "S":
			return "E"
		else:
			return "N"
	else:
		if direction == "N":
			return "E"
		elif direction == "E":
			return "S"
		elif direction == "S":
			return "W"
		else:
			return "N"

# Function that determines the new coordinates of the virus carrier            
def moveForward(x_coord, y_coord, direction):
	new_x_coord = x_coord
	new_y_coord = y_coord
	if direction == "N":
		new_y_coord -= 1
	elif direction == "E":
		new_x_coord += 1
	elif direction == "S":
		new_y_coord += 1
	else:
		new_x_coord -= 1		
	return new_x_coord, new_y_coord
		
#Function used to simulate the effects of a burst from the virus carrier given its coordinates and direction					
def burst(map, x_coord, y_coord, direction):
    key = str(x_coord) + "," + str(y_coord)
    # If the coordinates are not already in the map, initialize them to be clean
    # Changed this to a try/except block to increase efficiency
    try:
        temp = map[key]
    except:
        map[key] = "."
        
          
    # Get the new direction of the virus carrier
    if map[key] == "#":
        direction = changeDirection(direction, "R")
    elif map[key] == ".":
        direction = changeDirection(direction, "L")
    elif map[key] == "F":
        direction = changeDirection(direction, "L")
        direction = changeDirection(direction, "L")
    
    # Change the coordinate accordingly and return if this burst infected a node
    change_infected = False
    if map[key] == "#":
        map[key] = "F"
    elif map[key] == "W":
        map[key] = "#"
        change_infected = True
    elif map[key] == "F":
        map[key] = "."
    else:
        map[key] = "W"
    
    new_x, new_y = moveForward(x_coord, y_coord, direction)
    return new_x, new_y, direction, change_infected

# Function used to run num_burst number of bursts and get the number of bursts that have caused an infection    
def runBursts(file_name, num_bursts):
    # Generate the map and get the start coordinates
    size_x, size_y, map = readFileandGenerateMap(file_name)
    start_x = size_x / 2 + 1
    start_y = size_y / 2 + 1
    
    # Run the number of bursts and return the number of burst infections found
    start_dir = "N"
    count_infection_burst = 0
    for i in range(num_bursts):
        start_x, start_y, start_dir, infected = burst(map, start_x, start_y, start_dir)
        if infected:
            count_infection_burst += 1
    return count_infection_burst
			
print "Number of bursts that cause a node to become infected = ", runBursts("Star43_input.txt", 10000000)