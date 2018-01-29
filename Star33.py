# Function used to spin the buffer of numbers and return the resulting buffer
def spin(num_spins):
    # Will always be in this order, so start at number 2
    circular_buffer = [0, 1]
    current_pos = 1
    # Get the new position and insert after that index 
    for i in range(2, 2018):
        current_pos = (current_pos + num_spins) % len(circular_buffer) + 1
        circular_buffer.insert(current_pos, i)
    return circular_buffer

# Function to get the value after 2017    
def getValueAfter2017(circular_buffer):
    for i in range(2018):
        if circular_buffer[i] == 2017:
            if i == 2017:
                return circular_buffer[0]
            else:
                return circular_buffer[i+1]
	
print "Value after 2017: ", getValueAfter2017(spin(329))	
