
# Function to read the file and get the instructions to be run through
def readFileAndGetInstructions(file_name):
	instructions = []
	for line in open(file_name, 'r'):
		instructions.append(line.strip().split(" "))
	return instructions

# Function used for the set instruction
def set(x, y, registers, loc):
    # Check if y is referring to a register and act accordingly
	if y.isalpha():
		registers[x] = registers[y]
	else:
		registers[x] = int(y)	
	return loc + 1

# Function used for the sub instruction	
def sub(x, y, registers, loc):
    # Check if y is referring to a register and act accordingly
	if y.isalpha():
		registers[x] -= registers[y]
	else:
		registers[x] -= int(y)		
	return loc + 1

# Function used for the mul instruction    
def mul(x, y, registers, loc):
    # Check if y is referring to a register and act accordingly
	if y.isalpha():
		registers[x] *= registers[y]
	else:
		registers[x] *= int(y)		
	return loc + 1

# Function used for the jnz instruction	
def jnz(x, y, registers, loc):
    # If x is 0, jnz instruction does not move the loc
	if x == 0 or (x in registers and registers[x] == 0):
		return loc + 1
    # Otherwise, move the loc
	if loc + int(y) < 0:
		return 0
	else:
		return loc + int(y)

# Function used to run the instructions in the input file and count the number of mul instructions executed        
def runInstructionsAndCountMul(file_name):
    # Initialize the registers with a value of 0
	registers = dict([])
	for letter in ["a","b","c","d","e","f","g","h"]:
		registers[letter] = 0
	
    # Used to associate the instruction to the function call
	commands = {"set" : set,
				"sub" : sub,
				"mul" : mul,
				"jnz" : jnz,
	}
	
    # Run through the instructions and get the number of mul instructions called
	instructions = readFileAndGetInstructions(file_name)
    # Every instruction call returns the new loc
	loc = 0
	count_mul = 0
	while loc < len(instructions):
		if instructions[loc][0] == "mul":
			count_mul += 1
		loc = commands[instructions[loc][0]](instructions[loc][1], instructions[loc][2], registers, loc)
	return count_mul
			
print "Number of times mul instruction is invoked = ", runInstructionsAndCountMul("Star45_input.txt")