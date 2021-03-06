
# Function that reads the file and get the end coordinates of the child
def readFileAndGetEndDestination(file_name):
    x = 0
    y = 0
    z = 0
    for l in open(file_name, "r").readline().split(","):
        if l == "n":
            y += 1
            z -= 1
        elif l == "s":
            y -= 1
            z += 1
        elif l == "ne":
            x += 1
            z -= 1
        elif l == "nw":
            x -= 1
            y += 1
        elif l == "se":
            x += 1
            y -= 1
        elif l == "sw":
            x -= 1
            z += 1
    return [x, y, z]
        
# Actual distance to get to the child is (|x| + |y| + |z|) / 2
end_coords = readFileAndGetEndDestination("star21_input.txt")
print "Number of steps needed to reach child = ", (abs(end_coords[0]) + abs(end_coords[1]) + abs(end_coords[2])) / 2