
def get_distance(coordinates, upper_bound):
    mid_coordinate = [upper_bound / 2, upper_bound / 2]
    print abs(coordinates[0] - (upper_bound / 2)) + abs(coordinates[1] - (upper_bound / 2))

def find_coordinate(input, lower_bound, upper_bound):
    if lower_bound == upper_bound:
        print [upper_bound - 1, upper_bound - 1]
        return [upper_bound - 1, upper_bound - 1]
        
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
        
    print coordinate, highest_num - input 
        
    if coordinate == [upper_bound - 1, upper_bound - 1]:
        coordinate[0] = highest_num - input
        print "Got here 1"
    elif coordinate == [0, upper_bound - 1]:
        coordinate[1] = highest_num - input
        print "Got here 2"
    elif coordinate == [0, 0]:
        coordinate[0] = highest_num - input
        print "Got here 3"
    else: 
        coordinate[1] = highest_num - input
        print "Got here 4"

    print coordinate
    return coordinate
    
def get_boundary(input):
    lower_bound = int(input**(1/2.0))
    if lower_bound % 2 == 0:
        lower_bound -= 1
    upper_bound = lower_bound 
    if lower_bound ** 2 != input:
        upper_bound += 2
    print lower_bound 
    print upper_bound 

# Open the file and call the function
print 
get_boundary(1)
get_distance(find_coordinate(1, 1, 1), 1)

print 
get_boundary(12)
get_distance(find_coordinate(12, 3, 5), 5)

print
get_boundary(23)
get_distance(find_coordinate(23, 3, 5), 5)

print 
get_boundary(1024)
get_distance(find_coordinate(1024, 31, 33), 33)

print 
get_boundary(289326)
get_distance(find_coordinate(289326, 537, 539), 539)