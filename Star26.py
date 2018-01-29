# Class that represents each layer 
class Layer:
	# Initiates the Layer and places the initial scanner
    def __init__(self, l_size, l_scanner = 1, l_md = True):
        self.size = l_size
        self.scanner_loc = l_scanner
        self.moving_down = l_md
    
    # Function to move the scanner in the layer
    def move_scanner(self):
        if self.scanner_loc == self.size:
            self.moving_down = False
            self.scanner_loc -= 1
        elif self.scanner_loc == 1:
            self.moving_down = True
            self.scanner_loc += 1
        elif self.moving_down == True:
            self.scanner_loc += 1
        else:
            self.scanner_loc -= 1
	
    # Function to check if the scanner is on the first level of the layer
    def conflict(self):
        if self.scanner_loc == 1:
            return True
        return False
	
    # Function that gets the depth of the Layer
    def getRange(self):
        return self.size
    
    # Function that checks if the Layer's scanner is moving down
    def getMovementDirection(self):
        return self.moving_down
        
    def copy(self):
        return Layer(self.size, self.scanner_loc, self.moving_down)

# Function that reads the file and sets up all the layers        
def readFileandSetUp(file_name):
	layers = dict([])
	for line in open(file_name, 'r'):
		line_splitted = line.split(": ")
		layers[int(line_splitted[0])] = Layer(int(line_splitted[1]))
	return layers           

# Function to print the layers for debugging
def printLayers(layers):
    for l in layers.keys():
        print l, layers[l].scanner_loc
    
def checkZeroSeverity(layers):
    packet_loc = -1
    severity = 0
    
    while packet_loc <= max(layers.keys()):
        packet_loc += 1
        if packet_loc in layers.keys() and layers[packet_loc].conflict():
            severity += 1
        for l in layers.keys():
            layers[l].move_scanner()
    return severity

def checkInitialLayer(layers):
    for l in layers:
        if not(layers[l].conflict() and not layers[l].getMovementDirection()):
            return False
    return True

"""
def moveWithNoSeverity(file_name):
    delay = 0
    while True:
        new_layers = readFileandSetUp(file_name)
        for i in range(delay):
            for l in new_layers:
                new_layers[l].move_scanner()
        if checkZeroSeverity(new_layers) == 0:
            return delay
        delay += 1


"""	

def copy(layers):
    copy_layers = dict([])
    for l in layers.keys():
        copy_layers[l] = layers[l].copy()
    return copy_layers
    
def moveWithNoSeverity(file_name):
    delay = 1
    all_layers = [readFileandSetUp(file_name)]
    while True:
        new_layers = copy(all_layers[-1])
        for l in new_layers.keys():
            new_layers[l].move_scanner()
        if checkInitialLayer(new_layers):
            break
        all_layers.append(new_layers)
        delay += 1

    for al in range(len(all_layers)):
        if checkZeroSeverity(all_layers[al]) == 0:
            return al  

            
#print "Delay needed to pass through = ", moveWithNoSeverity("testing.txt")
print "Delay needed to pass through = ", moveWithNoSeverity("Star25_input.txt")