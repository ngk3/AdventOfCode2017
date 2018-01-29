def readFileandGetInstructions(file_name):
	instructions = []
	for line in open(file_name, 'r'):
		instructions.append(line.split(" "))
	return instructions
			
def runInstructions(file_name):
	instructions = readFileandGetInstructions(file_name)
	registers = dict([])
	played_freq = 0
	for i in instructions:
		if i[1].isalpha():
			registers[i[1]] = 0
		if i[0] == "snd" or i[0] == "rcv":
			continue
		if i[2].isalpha():
			registers[i[2]] = 0
	
	instruction_count = 0
	while instruction_count < len(instructions):
		if i[0] == "snd":
			played_freq = registers[i[1]]
		elif i[0] == "set":
			if i[2].isalpha():
				registers[i[1]] = registers[i[2]]
			else:
				registers[i[1]] = int(i[2])	
		elif i[0] == "add":
			if i[2].isalpha():
				registers[i[1]] += registers[i[2]]
			else:
				registers[i[1]] += int(i[2])	
		elif i[0] == "mul":
			if i[2].isalpha():
				registers[i[1]] *= registers[i[2]]
			else:
				registers[i[1]] *= int(i[2])		
		elif i[0] == "mod":
			if i[2].isalpha():
				registers[i[1]] %= registers[i[2]]
			else:
				registers[i[1]] %= int(i[2])	
		elif i[0] == "rcv":
			if int(i[1]) == 0:
				continue
			if i[1].isalpha():
				if registers[i[1]] == 0:
					continue
				return played_freq		
		else:
			if i[1].isalpha():
				if registers[i[1]] <= 0:
					continue
				instruction_count += registers[i[1]]
				continue
			else:
				if int(i[1]) <= 0:
					continue
				instruction_count += int(i[1])
				continue
		instruction_count += 1
		
print "Value of the recovered frequency = ", runInstructions("star35_input.txt")
#print "Value of the recovered frequency = ", runInstructions("testing.txt")