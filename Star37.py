# Need to check if this even works...	
def build_map(file_name):
	map = []
	for line in open(file_name, 'r'):
		temp = []
		for l in line:
			temp.append(l)
		map.append(temp)
	start = None
	for i in range(map[0]):
		if map[0][i] == "|":
			start = i
			break
	return map, (0, int(start))

# Can only turn left or right...need to put that in...
def getPossibleMoves(map, coord, visited_coord):
	possible_moves = dict([])
	if checkMovingForward(map, coord, visited_coord, "N"):
		possible_moves["N"] = move(coord, "N", map)
	if checkMovingForward(map, coord, visited_coord, "E"):
		possible_moves["E"] = move(coord, "E", map)
	if checkMovingForward(map, coord, visited_coord, "S"):
		possible_moves["S"] = move(coord, "S", map)
	if checkMovingForward(map, coord, visited_coord, "W"):
		possible_moves["W"] = move(coord, "W", map)
	return possible_moves

	
def checkMovingForward(map, coord, visited_coord, direction):
	new_coord = move(coord, direction, map)
	if new_coord == (-1,-1)
		return False
	if map[new_coord[0]][new_coord[1]] != " " and new_coord not in visited_coord:
		return True
	return False

def checkOutofBounds(coord, map):
	if coord[0] < 0 || coord[1] < 0 || coord[0] >= len(map[0]) || coord[1] >= len(map):
		return True
	return False
			
def move(coord, direction, map):
	new_coord = coord
	if direction == "S":
		new_coord[1] += 1
	elif direction == "N"
		new_cord[1] -= 1
	elif direction == "W"
		new_coord[0] -= 1
	else:
		new_coord[0] += 1
	if checkOutofBounds(coord, map):
		return (-1,-1)
	return new_coord

def printMap(map):
	for y in range(len(map)):
		printing = ""
		for x in range(len(map[y])):
			printing += map[y][x]
		print printing
			
def runPath(map, start):
	visited_coord = set([])
	letters_visited = ""
	coord = start
	direction = "S"
	visited_coord.add(coord)
	while True:
		possible_moves = getPossibleMoves(map, coord, visited_coord)
		if len(possible_moves) == 0:
			break		
		if checkMovingForward(map, visited_coord, direction, coord):
			coord = move(coord, direction, map)
		else:
			for dir in possible_moves:
				coord = possible_moves[dir]
				direction = dir
				break
		if isalpha(map[coord[0], coord[1]]):
			letters_visited += map[coord[0], coord[1]]
		visited_coord.add(coord)
	return letters_visited
			
map, start = build_map("star37_input.txt")
letters = runPath(map, start)
print letters