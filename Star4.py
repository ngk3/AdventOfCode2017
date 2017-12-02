
# Function used to open the file and find the sum the even divisible values in the file 
def get_even_divisible(file_name):
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
        
        # Go through values 
        for i in range(len(values)):
            # Check for evenly divisible of each value to every other value, stopping when values[j] is more
            # than half the value of values[i] (impossible to be evenly divisble)
            for j in range(len(values)):
                if values[j] > (values[-(i + 1)] / 2):
                    break 
                # If evenly divisble, add into count and exit loop
                if check_evenly_divisible(values[j], values[-(i+1)]):
                    count += (values[-(i+1)] / values[j])
                    break
    print count

# Helper Function that checks if dividing / divisor is evenly divisible 
def check_evenly_divisible(divisor, dividing):
    return (dividing % divisor) == 0
    
# Open the file and call the function
get_even_divisible("star3_input.txt")