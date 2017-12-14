
# Function that reads the input file and get the lengths for the hash 
def read_file(file_name):
    line_splitted = open(file_name).readline()
    returning = []
    # Add the ASCII representative number of each character
    for ls in range(len(line_splitted)):
        returning.append(ord(line_splitted[ls]))
    # Add the end numbers
    for i in [17, 31, 73, 47, 23]:
    	returning.append(i)
    return returning
    
# Function that performs the knot hash  
def knot_hash(lengths):
    # Initializes the 0-255 list
    complete_list = []
    for i in range(256):
        complete_list.append(i)
    current_index = 0
    skip_size = 0

    # Repeat the hash 64 times
    for repeat in range(64):
        # Go through every length
        for l in lengths:
            # Get the indices to be used and reverse them 
            reversing = []
            for i in range(l):
                if current_index + i > 255:
                    reversing.append(current_index + i - 256)
                    print current_index + i - 256, current_index, i 
                else:
                    reversing.append(current_index + i)
            reversing.reverse()
            
            # Go through half the indices and switch the values to reverse 
            for i in range(l / 2):
                if current_index + i > 255:
                    temp = complete_list[current_index + i - 256]
                    complete_list[current_index + i - 256] = complete_list[reversing[i]]
                    complete_list[reversing[i]] = temp
                else:
                    temp = complete_list[current_index + i]
                    complete_list[current_index + i] = complete_list[reversing[i]]
                    complete_list[reversing[i]] = temp
            
            current_index += l + skip_size
            # Decrase current_index as necessary
            while current_index > 255:
                current_index -= 256
            skip_size += 1
    return complete_list 

# Function used to get the dense hash from a sparse hash
def get_dense_hash(complete_list):
 	dense_hash = []
 	tracker = 0
    # Go through the list in blocks of 16, XORing and then creating dense_hash
 	while tracker < len(complete_list):
        # Get the block of 16...
 		block = []
 		for b in range(16):
 			block.append(complete_list[tracker + b])
 		current = block[0]
        
        # Perform XOR on all 16 elements and add to dense_hash
 		for b in range(1, 16):
 			current = current ^ block[b]
 		dense_hash.append(current)
 		tracker += 16		
	return dense_hash

# Function used to change a dense_hash into a hexadecimal representation	
def to_hex(dense_hash):
    returning = ""
    for dh in dense_hash:
        hx = hex(dh).replace("0x", "")
        if len(hx) == 1:
            hx = "0" + hx 
        returning += hx
    return returning

lengths = read_file("star19_input.txt")
complete_list = knot_hash(lengths)
dense_hash = get_dense_hash(complete_list)
print to_hex(dense_hash)
