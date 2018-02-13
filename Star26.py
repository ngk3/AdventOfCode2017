# Note: This is done by Brute Force

# Class that represents each layer 
class Layer:
    # Initiates the Layer and places the initial scanner
    def __init__(self, l_size, l_scanner_loc = 1, l_moving_down = True):
        self.size = l_size
        self.scanner_loc = l_scanner_loc
        self.moving_down = l_moving_down
    
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
	
    # Gets the depth of the Layer
    def getRange(self):
        return self.size
        
    def copy(self):
        return Layer(self.size, self.scanner_loc, self.moving_down)

# Function that reads the file and sets up all the layers        
def readFileandSetUp(file_name):
	layers = dict([])
	for line in open(file_name, 'r'):
		line_splitted = line.split(": ")
		layers[int(line_splitted[0])] = Layer(int(line_splitted[1]))
	return layers           
    
# Function used to run the simulation with the packet moving immediately and returning the total severity
def runSimulationImmediate(layers):
    packet_loc = 0
    max_layer = max(layers.keys())
    severity = 0
    
    while packet_loc <= max_layer:
        if packet_loc in layers.keys() and layers[packet_loc].conflict():
            return 1
        for l in layers.keys():
            if l < packet_loc:
                continue
            layers[l].move_scanner()
        packet_loc += 1
    return severity

# Function that copys the layers
def copyLayers(layers):
    copy_layers = dict([])
    for l in layers.keys():
        copy_layers[l] = layers[l].copy()
    return copy_layers       

# Function to find the delay    
def findDelay(layers):
    delay = 0
    test_layers = dict([])
    while True:
        delay += 1
        for l in layers.keys():
            layers[l].move_scanner()
        copy_layer = copyLayers(layers)
        severity = runSimulationImmediate(copy_layer)
        print severity
        if severity == 0:
            break 
    return delay
 
 
layers = readFileandSetUp("star25_input.txt")
print "Delay needed for 0 severity = ", findDelay(layers)