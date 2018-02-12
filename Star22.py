
# Function that reads the file and get the max distance of the child
def readFileAndGetMaxDestination(file_name):
    x = 0
    y = 0
    z = 0
    max = 0
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
        if ((abs(x) + abs(y) + abs(z)) / 2) > max:
            max = (abs(x) + abs(y) + abs(z)) / 2
    return max
        
print "Furthest away the child is in steps = ", readFileAndGetMaxDestination("star21_input.txt")