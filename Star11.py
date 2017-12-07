
# Function used to turn the banks into a String representation
def banks_to_string(banks):
	returning = ""
	for i in banks:
		returning += str(i) + " "
	return returning.strip()
	
# Function used to redistribute the banks based on the given position and the highest value found
def redistribute(banks, position, highest_value):
    # Reset the highest bank to 0 and start index on bank after position bank
	banks[position] = 0
	tracker = position + 1
    # Redistribute all of position bank, wraparound until finished
	while highest_value > 0:
		if tracker == len(banks):
			tracker = 0
		banks[tracker] += 1
		highest_value -= 1
		tracker += 1
		
# Function that performs all needed redistribution on the banks until the infinite cycle is found
def perform_redistribution(banks):
    # visited stores all visited String representation of the banks
	visited = set()
	visited.add(banks_to_string(banks))
	
    # Continue until the cycle is found
	count = 0
	while True:
		position = 0
		highest_value = 0
		
        # Find the bank with the highest value 
		for i in range(len(banks)):
			if banks[i] > highest_value:
				position = i
				highest_value = banks[i]
				
        # Redistribute the highest bank and increase cycle count
		redistribute(banks, position, highest_value)
		
		count += 1
		new_banks = banks_to_string(banks)
        # If the current bank has been seen before, return the cycle count. Otherwise, add the new bank into visited
		if new_banks in visited:
			break
		visited.add(new_banks)
	return count 

# Function used to read a file and get the cycle counts based on redistribution	
def read_file_and_get_redistribution(file_name):
	banks = []
	for line in open(file_name):
		for s in line.split("\t"):
			banks.append(int(s))
	return perform_redistribution(banks)

print read_file_and_get_redistribution("star11_input.txt")