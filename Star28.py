import binascii
# Code has been imported from Star20.py

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
            # Decease current_index as necessary
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

# Function that gets all the hashed rows
def getAllrows():
    all_rows_hashing = []
    
    for i in range(128):
        returning = []
        # Add the ASCII representative number of each character
        for ls in "ljoxqyyw-":
            returning.append(ord(ls))
        for j in str(i):
            returning.append(ord(j))
        # Add the end numbers
        for j in [17, 31, 73, 47, 23]:
            returning.append(j)
        all_rows_hashing.append(returning)
        
    bit_rows = []
    for arh in all_rows_hashing:
        bit_rows.append(to_hex(get_dense_hash(knot_hash(arh))))
    return bit_rows

# Function that gets all the used square coordinates 
def getUsedSquareCoordinates(bit_rows):
    bin_coord = []
    # Go through each hash
    for br in bit_rows:
        add_bin_coord = ""
        # Go through each character
        for b in br:
            # Get the binary representative
            bin_rep = bin(int(b, 16)).replace("0b", "")
            while len(bin_rep) < 4:
                bin_rep = "0" + bin_rep
            add_bin_coord += bin_rep
        bin_coord.append(add_bin_coord)
    
    # Get all the coordinates that are 1 
    coordinates = []
    for row in range(128):
        for col in range(128):
            if bin_coord[row][col] == "1":
                coordinates.append(str(row) + "," + str(col))

    return coordinates

# Function that gets the number of regions that the map has
def getNumRegions(coordinates):
    # Essentially perform a bfs with each group and remove from coordinates until all group has been found
    num_groups = 0
    queue = []
    while len(coordinates) > 0:
        queue.append(coordinates[0])
        while len(queue) > 0:
            popped = queue.pop(0)
            if popped in coordinates:
                coordinates.remove(popped)
            else:
                continue
            
            popped_splitted = popped.split(",")
            popped_x = int(popped_splitted[0])
            popped_y = int(popped_splitted[1])
            if (str(popped_x + 1) + "," + str(popped_y))in coordinates:
                queue.append((str(popped_x + 1) + "," + str(popped_y)))
            if (str(popped_x - 1) + "," + str(popped_y))in coordinates:
                queue.append((str(popped_x - 1) + "," + str(popped_y)))
                
            if (str(popped_x) + "," + str(popped_y + 1))in coordinates:
                queue.append((str(popped_x) + "," + str(popped_y + 1)))
            if (str(popped_x) + "," + str(popped_y - 1))in coordinates:
                queue.append((str(popped_x) + "," + str(popped_y - 1)))
        num_groups += 1
    return num_groups
    
usedSquareCoordinates = getUsedSquareCoordinates(getAllrows())
print "Number of regions = ", getNumRegions(usedSquareCoordinates)
