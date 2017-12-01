
# Function used to count all the sequential digits and return the sum
def get_all_sequential_digits(input):
    count = 0
    # Go through the n elements of input and compare n to n+1 element
    for i in range(0, len(input) - 1):
        if input[i] == input[i+1]:
            count += int(input[i])
    
    # Account for the wraparound of the first and the last element
    if input[0] == input[-1]:
        count += int(input[0])
    return count

# Open the file and call the function
f = open("star1_input.txt")
print get_all_sequential_digits(f.readline())