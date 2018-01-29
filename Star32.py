
# Function used to generate the initial list of programs
def generatePrograms():
    return ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]
    
# Function used to read the input file and get all the respective dance moves	
def readFileandGetDanceMoves(file_name):
    return open(file_name, 'r').readline().split(",")

# Function used to operate the spin command    
def spin(programs, num_spin):
    # Change the num_spin to get absolute num_spin result
    if num_spin > len(programs):
        num_spin = num_spin % len(programs)
    return programs[len(programs) - num_spin:len(programs)] + programs[0:len(programs) - num_spin]

# Exchanges the programs at index pos_a and pos_b    
def exchange(programs, pos_a, pos_b):
    temp = programs[pos_a]
    programs[pos_a] = programs[pos_b]
    programs[pos_b] = temp

# Exchanges the programs with names a_name and b_name    
def partner(programs, a_name, b_name):
    pos_a = programs.index(a_name)
    pos_b = programs.index(b_name)
    exchange(programs, pos_a, pos_b)

# Perform the dance of programs given the file name    
def dance(file_name):
    programs = generatePrograms()
    # Get the instructions and set up the values to run through more efficiently
    instructions = readFileandGetDanceMoves(file_name)
    for i in range(len(instructions)):
        if instructions[i][0] == "s":
            instructions[i] = ["s", int(instructions[i].replace("s", "", 1))]
        elif instructions[i][0] == "x":
            instructions[i] = instructions[i].replace("x", "", 1).split("/")
            instructions[i].insert(0, "x")
        else:
            instructions[i] = instructions[i].replace("p", "", 1).split("/")
            instructions[i].insert(0, "p")
    
    # The programs will cycle at some point; Get all the program cycles and store in program_permutations
    program_permutations = []
    while True:
        # Break when cycle is found
        if printPrograms(programs) in program_permutations:
            break
        program_permutations.append(printPrograms(programs))
        # Go through the instructions
        for i in instructions:
            if i[0] == "s":
                programs = spin(programs, i[1])
            elif i[0] == "x":
                exchange(programs, int(i[1]), int(i[2]))
            else:
                partner(programs, i[1], i[2])
    # Get the 1 billion result of the program            
    return program_permutations[1000000000 % len(program_permutations)]

# Function to print the programs two different ways (regular or debugging)    
def printPrograms(programs):
	temp = ""
	for k in range(len(programs)):
		temp += programs[k]
	return temp
		
programs = dance("Star31_input.txt")
print programs
