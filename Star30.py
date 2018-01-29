
# Function that reads the file and get genA and genB start values as integers
def readFileandGetStartValues(file_name):
	genAStart = 0
	genBStart = 0
	for line in open(file_name, 'r'):
		line_splitted = line.split(" ")
		if (line_splitted[1] == "A"):
			genAStart = int(line_splitted[-1])
		else:
			genBStart = int(line_splitted[-1])
	return (genAStart, genBStart)

# Function that gets the right-most 16 bits (padded or sliced as necessary) of an integer		
def getRightMost16bits(int_value):
	# Get a binary representative of the integer value
    bin_rep = "{0:b}".format(int_value)
	if len(bin_rep) == 16:
		return bin_rep
	# Pad to 16 bits as necessary
    elif len(bin_rep) < 16:
		return "0" * (16 - len(bin_rep)) + bin_rep
	# Only get the right most 16 bits if integer is bigger than 16 bits
    else:
		returning = ""
		for i in range(16):
			returning += bin_rep[-1 * (16 - i)]
		return returning

# Generate the next value of the generator given the required values         
def generateNextValue(prev_value, mul_factor):
	return (prev_value * mul_factor) % 2147483647

# Function that gets the number of pairs matches in num_pairs 
def findNumPairmatches(file_name, num_pairs, a_mul_factor, b_mul_factor):
    genAStart, genBStart = readFileandGetStartValues(file_name)
    count = 0 
    matches = 0
    # List that stores the ordered values of the generators found
    genAValues = [] 
    genBValues = []
    # Go through num_pair iterations
    while count < num_pairs:
        genAValue = generateNextValue(genAStart, a_mul_factor)
        genBValue = generateNextValue(genBStart, b_mul_factor)
        # Add value to list if divisible by 4 for generator A or divisible by 8 for generator B
        if genAValue % 4 == 0:
            genAValues.append(genAValue)
        if genBValue % 8 == 0:
            genBValues.append(genBValue)
        genAStart = genAValue
        genBStart = genBValue
        count += 1
    # Go through the number of (genA, genB) pairs there are and get number of matches
    for i in range(min(len(genAValues), len(genBValues))):
        if getRightMost16bits(genAValues[i]) == getRightMost16bits(genBValues[i]):
            matches += 1
    return matches
  
print "Num pairs that match out of 40 million = ", findNumPairmatches("star29_input.txt", 40000000, 16807, 48271)
