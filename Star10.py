
# Global list of instructions
jump_instructions = []

# Function that reads the input file and store the instructions as an integer into jump_instructions
def read_file_and_store(file_name):
	for line in open(file_name):
		jump_instructions.append(int(line))

# Function that goes through the instructions until the maze is exit and return number of steps taken
def go_through_instructions():
	position = 0
	count = 0
	# Iterate until exit is achieved
	while position < len(jump_instructions):
		# If the offset is 3 or more, decrease by one when leaving and move to new position
		if jump_instructions[position] > 2:
			jump_instructions[position] -= 1
			position += jump_instructions[position] + 1
		# Otherwise, add one to the offset when leaving and move to new position
		else:
			jump_instructions[position] += 1
			position += jump_instructions[position] - 1
		# Increment steps taken
		count += 1
	return count
    
read_file_and_store("star9_input.txt")
print go_through_instructions()