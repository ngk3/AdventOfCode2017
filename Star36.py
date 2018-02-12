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
    registers_pgm0 = dict([])
    registers_pgm1 = dict([])
    for letter in string.ascii_lowercase:
        registers_pgm0[letter] = 0
        registers_pgm1[letter] = 0
    registers_pgm1["p"] = 1
       
    # Track the instruction location, sending, and receiving      
    instruction_count_pgm0 = 0
    instruction_count_pgm1 = 0
    track_pgm1send = 0
    pgm0_status = "None"
    
    # Tracks the list of items pgm0 is sending and what to assign when pgm0 is receiving
    pgm0_sending = []
    pgm0_receive = ""
    
    # Go through all the instructions
    while instruction_count_pgm0 < len(instructions) or instruction_count_pgm1 < len(instructions):
        # Keep going through pgm0 until a rec command is seen
        if pgm0_status != "Receive":
            i = instructions[instruction_count_pgm0]
            if i[0] == "snd":
                try:
                    pgm0_sending.append(registers_pgm0[i[1]])
                except:
                    pgm0_sending.append(int(i[1]))
            elif i[0] == "set":
                try:
                    registers_pgm0[i[1]] = registers_pgm0[i[2]]
                except:
                    registers_pgm0[i[1]] = int(i[2])	
            elif i[0] == "add":
                try:
                    registers_pgm0[i[1]] += registers_pgm0[i[2]]
                except:
                    registers_pgm0[i[1]] += int(i[2])	
            elif i[0] == "mul":
                try:
                    registers_pgm0[i[1]] *= registers_pgm0[i[2]]
                except:
                    registers_pgm0[i[1]] *= int(i[2])		
            elif i[0] == "mod":
                try:
                    registers_pgm0[i[1]] %= registers_pgm0[i[2]]
                except:
                    registers_pgm0[i[1]] %= int(i[2])	
            elif i[0] == "rcv":
                pgm0_receive = i[1]
                pgm0_status = "Receive"
            else:
                if i[1].isalpha():
                    if registers_pgm0[i[1]] <= 0:
                        instruction_count_pgm0 += 1
                        continue
                    try:
                        instruction_count_pgm0 += int(i[2])
                    except:
                        instruction_count_pgm0 += registers_pgm0[i[2]]
                    continue
                else:
                    if int(i[1]) <= 0:
                        instruction_count_pgm0 += 1
                        continue 
                    try:
                        instruction_count_pgm0 += int(i[2])
                    except:
                        instruction_count_pgm0 += registers_pgm0[i[2]]
                    continue
            instruction_count_pgm0 += 1
        else:
            i = instructions[instruction_count_pgm1]
            if i[0] == "snd":
                try:
                    registers_pgm0[pgm0_receive] = registers_pgm1[i[1]]
                except:
                    registers_pgm0[pgm0_receive] = int(i[1])
                pgm0_status = "None"
                track_pgm1send += 1
            elif i[0] == "set":
                try:
                    registers_pgm1[i[1]] = registers_pgm1[i[2]]
                except:
                    registers_pgm1[i[1]] = int(i[2])	
            elif i[0] == "add":
                try:
                    registers_pgm1[i[1]] += registers_pgm1[i[2]]
                except:
                    registers_pgm1[i[1]] += int(i[2])	
            elif i[0] == "mul":
                try:
                    registers_pgm1[i[1]] *= registers_pgm1[i[2]]
                except:
                    registers_pgm1[i[1]] *= int(i[2])		
            elif i[0] == "mod":
                try:
                    registers_pgm1[i[1]] %= registers_pgm1[i[2]]
                except:
                    registers_pgm1[i[1]] %= int(i[2])	
            elif i[0] == "rcv":
                if len(pgm0_sending) == 0:
                    break
                registers_pgm1[i[1]] = pgm0_sending.pop(0)		
            else:
                if i[1].isalpha():
                    if registers_pgm1[i[1]] <= 0:
                        instruction_count_pgm1 += 1
                        continue
                    try:
                        instruction_count_pgm1 += int(i[2])
                    except:
                        instruction_count_pgm1 += registers_pgm1[i[2]]
                    continue
                else:
                    if int(i[1]) <= 0:
                        instruction_count_pgm1 += 1
                        continue 
                    try:
                        instruction_count_pgm1 += int(i[2])
                    except:
                        instruction_count_pgm1 += registers_pgm1[i[2]]
                    continue
            instruction_count_pgm1 += 1
    return track_pgm1send    
		
print "Number of times program 1 sent a value = ", runInstructions("Star35_input.txt")
