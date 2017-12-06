
# Global list of instructions
jump_instructions = []

# Function that reads the input file and store the instructions as an integer into jump_instructions
def read_file_and_store(file_name):
	for line in open(file_name):
		jump_instructions.append(int(line))

# Function that goes through the instructions until the maze is exit and return number of steps taken		
def go_through_instructions():
	position = 0
	steps = 0
	# Iterate until exit is achieved
	while position < len(jump_instructions):
		# Add one to the offset when leaving and move to new position, incrementing steps taken
		jump_instructions[position] += 1
		position += jump_instructions[position] - 1
		steps += 1
	return steps
		
read_file_and_store("star9_input.txt")
print go_through_instructions()