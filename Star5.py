# Looking at this problem with the idea that the (0, 0) starts in the top left corner

# Function used to get the distance from the coordinate to the middle initial starting point 
def get_distance(coordinates, upper_bound):
    mid_coordinate = [upper_bound / 2, upper_bound / 2]
    print abs(coordinates[0] - (upper_bound / 2)) + abs(coordinates[1] - (upper_bound / 2))

# Function used to find the end coordinates of the input 
def find_coordinate(input, lower_bound, upper_bound):
    # This means that the input is in the bottom right corner 
    if lower_bound == upper_bound:
        return [upper_bound - 1, upper_bound - 1]
        
    # Move the coordinates backwards until the right corner is found
    coordinate = [upper_bound - 1, upper_bound - 1]
    highest_num = upper_bound**2
    if highest_num - (upper_bound - 1) > input:
        coordinate = [0, upper_bound - 1]
        highest_num -= (upper_bound - 1)
    if highest_num - (upper_bound - 1) > input:
        coordinate = [0, 0]
        highest_num -= (upper_bound - 1)
    if highest_num - (upper_bound - 1) > input:
        coordinate = [upper_bound - 1, 0]
        highest_num -= (upper_bound - 1)
    
    # Move the coordinates backwards until the right number is found and return the coordinates
    if coordinate == [upper_bound - 1, upper_bound - 1]:
        coordinate[0] = highest_num - input
    elif coordinate == [0, upper_bound - 1]:
        coordinate[1] = highest_num - input
    elif coordinate == [0, 0]:
        coordinate[0] = highest_num - input
    else: 
        coordinate[1] = highest_num - input
    return coordinate
    
# Function that finds the upper and lower boundary of the input
# This takes advantage of the pattern that each wraparound spiral is in the pattern 1, 9, 25, ...
# OR (1^2), (3^2), (5^2), ...
def get_boundary(input):
    lower_bound = int(input**(1/2.0))
    if lower_bound % 2 == 0:
        lower_bound -= 1
    upper_bound = lower_bound 
    if lower_bound ** 2 != input:
        upper_bound += 2
    return lower_bound, upper_bound 

# Open the file and call the function
bounds = get_boundary(289326)
get_distance(find_coordinate(289326, bounds[0], bounds[1]), bounds[1])   