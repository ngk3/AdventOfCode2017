
# Function used to open the file and find the sum of the range of each line of input
def get_range(file_name):
    count = 0
    f = open(file_name)
    
    # Go through each line in the file 
    for line in f:
        values = []
        # Split the string up and add into values as an int 
        for temp in line.split():
           values.append(int(temp))
        
        # Sort the list and add the range into count 
        values = sorted(values)
        count += (values[-1] - values[0])
    
    # Print the sum of all the range
    print count

some_function("star3_input.txt")