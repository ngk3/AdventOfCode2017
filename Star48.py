
# Class representing each port-bridge
class Port:
    def __init__(self, port1, port2):
        self.port1 = port1 
        self.port2 = port2 
        
    def getPorts(self):
        return [self.port1, self.port2]
        
    def copy(self):
        return Port(self.port1, self.port2)
        
    def equals(self, port2):
        port2_ports = port2.getPorts()
        return self.port1 == port2_ports[0] and self.port2 == port2_ports[1]

# Function that copies the ports except for remove_port and returns the new copy
def copyPortsExcept(remove_port, ports):
    copy = set([])
    found = False 
    for p in ports:
        if p.equals(remove_port) and not found:
            found = True
            continue
        copy.add(p.copy())
    return copy
        
# Function to read the input file and get all the useable ports
def readFileAndGetPorts(file_name):
    ports = set([])
    for line in open(file_name, 'r'):
        line_splitted = line.split("/")
        ports.add(Port(int(line_splitted[0]), int(line_splitted[1])))
    return ports

# Function used to get the possible starting ports    
def getStarts(ports):
    starts = set([])
    removing = set([])
    
    # Get the port number other than the 0 that is used to start the bridge 
    for p in ports:
        connections = p.getPorts()
        if connections[0] == 0 and connections[1] == 0:
            continue
        if connections[0] == 0:
            starts.add(connections[1])
            removing.add(p)
        elif connections[1] == 0:
            starts.add(connections[0])
            removing.add(p)
            
    # Remove the starts from the ports 
    for r in removing:
        ports.remove(r)
    return starts

# Function used to get all the valid port-nodes given a specific port
def getValidPorts(node_connection, ports):
    valid_ports = set([])
    for p in ports:
        if node_connection in p.getPorts():
            valid_ports.add(p.copy())
    return valid_ports

# What is the strength of the longest bridge you can make? 
# If you can make multiple bridges of the longest length, pick the strongest one.    

def getMaxLength(length, start, ports):
    # Get the valid ports that connects to start and return max if no valid ports are found
    valid_ports = getValidPorts(start, ports)
    if len(valid_ports) == 0:
        return length
    new_length = length
    
    # Find the maximum strength bridge that connects to start
    for vp in valid_ports:
        copy_ports = copyPortsExcept(vp, ports)
        vp_ports = vp.getPorts()
        returning_length = 0
        if vp_ports[0] == start:
            returning_length = getMaxLength(length + 1, vp_ports[1], copy_ports)
        else:
            returning_length = getMaxLength(length + 1, vp_ports[0], copy_ports)
        if returning_length > new_length:
            new_length = returning_length
    return new_length

def findMaxLengthBridge(input_file):
    # Get the ports and starts
    ports = readFileAndGetPorts(input_file)
    starts = getStarts(ports)
    
    # Get the maximum length bridge able to be created with each start port
    max = 0
    for s in starts:
        s_max = getMaxLength(1, s, ports)
        if s_max > max:
            max = s_max 
    return max   

def getMaxStrengthLength(max_length, max_strength, current_length, start, ports):
    # Get the valid ports that connects to start and return max if no valid ports are found
    valid_ports = getValidPorts(start, ports)
    if len(valid_ports) == 0:
        if current_length == max_length:
            return max_strength 
        else:
            return 0 
    new_max = max_strength
    
     # Find the maximum strength bridge that connects to start
    for vp in valid_ports:
        copy_ports = copyPortsExcept(vp, ports)
        vp_ports = vp.getPorts()
        returning_max = 0
        if vp_ports[0] == start:
            returning_max = getMaxStrengthLength(max_length, max_strength + vp_ports[1] + vp_ports[0], current_length + 1, vp_ports[1], copy_ports)
        else:
            returning_max = getMaxStrengthLength(max_length, max_strength + vp_ports[0] + vp_ports[1], current_length + 1, vp_ports[0], copy_ports)
        if returning_max > new_max:
            new_max = returning_max
    return new_max

# Function that finds the maximum bridge strength given an input file of ports          
def findMaxStrengthBridge(input_file):
    # Get the ports and starts
    ports = readFileAndGetPorts(input_file)
    starts = getStarts(ports)
    
    max_length = findMaxLengthBridge(input_file)
    
    # Get the maximum strength bridge able to be created with each start port
    max = 0
    for s in starts:
        s_max = getMaxStrengthLength(max_length, s, 1, s, ports)
        if s_max > max:
            max = s_max 
    return max
    
# Recursive function used to get the max strength of a bridge given an initial start port    
def getMaxStrength(max, start, ports):
    # Get the valid ports that connects to start and return max if no valid ports are found
    valid_ports = getValidPorts(start, ports)
    if len(valid_ports) == 0:
        return max
    new_max = max
    
    # Find the maximum strength bridge that connects to start
    for vp in valid_ports:
        copy_ports = copyPortsExcept(vp, ports)
        vp_ports = vp.getPorts()
        returning_max = 0
        if vp_ports[0] == start:
            returning_max = getMaxStrength(max + vp_ports[1] + vp_ports[0], vp_ports[1], copy_ports)
        else:
            returning_max = getMaxStrength(max + vp_ports[0] + vp_ports[1], vp_ports[0], copy_ports)
        if returning_max > new_max:
            new_max = returning_max
    return new_max
        
# Function that finds the maximum bridge strength given an input file of ports          
def findMaxBridge(input_file):
    # Get the ports and starts
    ports = readFileAndGetPorts(input_file)
    starts = getStarts(ports)
    
    # Get the maximum strength bridge able to be created with each start port
    max = 0
    for s in starts:
        s_max = getMaxStrength(s, s, ports)
        if s_max > max:
            max = s_max 
    return max
          
print findMaxStrengthBridge("Star47_input.txt")