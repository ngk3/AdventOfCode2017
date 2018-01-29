# Class that represents each layer 
class Layer:
	# Initiates the Layer and places the initial scanner
	def __init__(self, l_size):
		self.size = l_size
		self.scanner_loc = 1
		self.moving_down = True
	
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
    
# Function used to run the simulation with the packet moving immediately and returning the total severity
def runSimulationImmediate(layers):
    packet_loc = 0
    max_layer = max(layers.keys())
    severity = 0
    
    while packet_loc <= max_layer:
        if packet_loc in layers.keys() and layers[packet_loc].conflict():
            severity += packet_loc * layers[packet_loc].getRange()
        for l in layers.keys():
            layers[l].move_scanner()
        packet_loc += 1
    return severity
			
layers = readFileandSetUp("star25_input.txt")
print "Severity if immediate leave = ", runSimulationImmediate(layers)