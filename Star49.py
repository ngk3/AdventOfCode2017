class State:
	def __init__(self, s_name, s_state_0, s_state_1):
		self.name = s_name
		self.state_0 = s_state_0
		self.state_1 = s_state_1
	
	def getZeroState(self):
		return self.state_0
				
	def getOneState(self):
		return self.state_1
	
def readFileAndGetInfo(file_name):
    begin_state = ""
    checksum = 0
    states = dict([])
	
    file = open(file_name, 'r')
    line = None
		
    while True:
        line = file.readline()
        if line == "":
            break
        line = line.strip()
        if begin_state == "":
            begin_state = line.split(" ")[-1].replace(".","")
        elif checksum == 0:
            checksum = int(line.split(" ")[-2])
        elif len(line) == 0:
            continue
        else:
            state = line.split(" ")[-1].replace(":","")
            state_0 = []
            line = file.readline().strip()
            line = file.readline().strip()
            state_0.append(int(line.split(" ")[-1].replace(".","")))
            line = file.readline().strip()
            state_0.append(line.split(" ")[-1].replace(".",""))
            line = file.readline().strip()
            state_0.append(line.split(" ")[-1].replace(".",""))
			
            state_1 = []
            line = file.readline().strip()
            line = file.readline().strip()
            state_1.append(int(line.split(" ")[-1].replace(".","")))
            line = file.readline().strip()
            state_1.append(line.split(" ")[-1].replace(".",""))
            line = file.readline().strip()
            state_1.append(line.split(" ")[-1].replace(".",""))
			
            states[state] = State(state, state_0, state_1)
    return begin_state, checksum, states
		
	
def runTuringMachine(file_name):
    state_tracker, checksum, states = readFileAndGetInfo(file_name)
    tracker = checksum
    tape = dict([])
    tape[tracker] = 0
	
    count_itr = 0
    count_ones = 0
	
    while count_itr < checksum:
        if count_itr % 1000000 == 0:
            print count_itr
        if tracker not in tape.keys():
            tape[tracker] = 0
        if tape[tracker] == 0:
            execution = states[state_tracker].getZeroState()
            if execution[0] == 1:
                tape[tracker] = execution[0]
                count_ones += 1
            if execution[1] == "left":
                tracker -= 1
            else:
                tracker += 1
            state_tracker = execution[2]
        else:
            execution = states[state_tracker].getOneState()
            if execution[0] == 0:
                tape[tracker] = execution[0]
                count_ones -= 1
            if execution[1] == "left":
                tracker -= 1
            else:
                tracker += 1
            state_tracker = execution[2]
        count_itr += 1
    return count_ones
			
print "Diagnostic checksum = ", runTuringMachine("Star49_input.txt")
