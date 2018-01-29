
# Function used to generate the initial list of programs
def generatePrograms():
    programs = dict([])
    count = 0
    for l in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]:
        programs[count] = l
        count += 1
    return programs

# Function used to read the input file and get all the respective dance moves	
def readFileandGetDanceMoves(file_name):
    return open(file_name, 'r').readline().split(",")

# Function used to operate the spin command    
def spin(programs, num_spin):
    # Stores the new result of the programs 
    returning_programs = dict([])
    # If num_spin goes through entire program, only operate on the true movement
    if num_spin > len(programs):
        num_spin = num_spin % len(programs)
    # Go through each program and get the new index, return the resulting programs
    for i in range(len(programs)):
        if i+num_spin > len(programs) - 1:
            returning_programs[i+num_spin - len(programs)] = programs[i]
        else:
            returning_programs[i+num_spin] = programs[i]
    return returning_programs

# Exchanges the programs at index pos_a and pos_b    
def exchange(programs, pos_a, pos_b):
    temp = programs[pos_a]
    programs[pos_a] = programs[pos_b]
    programs[pos_b] = temp

# Exchanges the programs with names a_name and b_name    
def partner(programs, a_name, b_name):
    pos_a = -1
    pos_b = -1
    # Get the index of a_name and b_name and then call exchange()
    for p_index in programs.keys():
        if pos_a != -1 and pos_b != -1:
            break
        if programs[p_index] == a_name:
            pos_a = p_index
        elif programs[p_index] == b_name:
            pos_b = p_index
    exchange(programs, pos_a, pos_b)

# Perform the dance of programs given the file name    
def dance(file_name):
    programs = generatePrograms()
    instructions = readFileandGetDanceMoves(file_name)
    for i in instructions:
        if i[0] == "s":
            programs = spin(programs, int(i.replace("s", "", 1)))
        elif i[0] == "x":
            temp = i.replace("x", "").split("/")
            exchange(programs, int(temp[0]), int(temp[1]))
        else:
            temp = i.replace("p", "", 1).split("/")
            partner(programs, temp[0], temp[1])
    return programs

# Function to print the programs two different ways (regular or debugging)    
def printPrograms(programs, ordered=False):
	if ordered == False:
		temp = ""
		for k in range(len(programs)):
			temp += programs[k]
		print temp
	else:
		for k in range(len(programs)):
			print"(%i:%s)" %(k, programs[k])
		
programs = dance("star31_input.txt")
printPrograms(programs)