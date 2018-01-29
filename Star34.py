# Function to spin the buffer and get the value after 0 with 50000000 values inserted
def spin(num_spins):
    size = 2
    current_pos = 1
    current_one = 1
    for i in range(2, 50000000):
        current_pos = (current_pos + num_spins) % size + 1
        if current_pos == 1:
            current_one = i
        size += 1
    return current_one
	
print "Value after 1: ", spin(329)