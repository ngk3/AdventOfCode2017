import string

# Function that reads the file and get the instructions
def readFileandGetInstructions(file_name):
    instructions = []
    for line in open(file_name, 'r'):
        instructions.append(line.strip().split(" "))
    return instructions

# Function that runs the instructions and     
def runInstructions(file_name):
    # Get the instructions and initialize the registers
    instructions = readFileandGetInstructions(file_name)
    registers = dict([])
    played_freq = 0
    for letter in string.ascii_lowercase:
        registers[letter] = 0
        
    # Track the instruction location and they played frequencies     
    instruction_count = 0
    played_freq = 0
    first_received = None
    
    # Go through all the instructions
    while instruction_count < len(instructions):
        i = instructions[instruction_count]
        if i[0] == "snd":
            played_freq = registers[i[1]]
        elif i[0] == "set":
            try:
                registers[i[1]] = registers[i[2]]
            except:
                registers[i[1]] = int(i[2])	
        elif i[0] == "add":
            try:
                registers[i[1]] += registers[i[2]]
            except:
                registers[i[1]] += int(i[2])	
        elif i[0] == "mul":
            try:
                registers[i[1]] *= registers[i[2]]
            except:
                registers[i[1]] *= int(i[2])		
        elif i[0] == "mod":
            try:
                registers[i[1]] %= registers[i[2]]
            except:
                registers[i[1]] %= int(i[2])	
        elif i[0] == "rcv":
            if registers[i[1]] == 0:
                instruction_count += 1
                continue
            return played_freq		
        else:
            if i[1].isalpha():
                if registers[i[1]] <= 0:
                    instruction_count += 1
                    continue
                instruction_count += int(i[2])
                continue
            else:
                if int(i[1]) <= 0:
                    instruction_count += 1
                    continue 
                instruction_count += int(i[2])
                continue
        instruction_count += 1
		
print "Value of the recovered frequency = ", runInstructions("star35_input.txt")
