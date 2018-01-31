
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
			
def getMaxStrength(max, start, ports):
    print max, start, len(ports)
    valid_ports = getValidPorts(start, ports)
    if len(valid_ports) == 0:
        return max
    new_max = max
    for vp in valid_ports:
        copy_ports = copyPortsExcept(vp, ports)
        vp_ports = vp.getPorts()
        returning_max = 0
        if vp_ports[0] == start:
            returning_max = getMaxStrength(max + vp_ports[1], vp_ports[1], copy_ports)
        else:
            returning_max = getMaxStrength(max + vp_ports[0], vp_ports[0], copy_ports)
        if returning_max > new_max:
            new_max = returning_max
        print new_max
    return new_max
        
          
def findMaxBridge(input_file):
    ports = readFileAndGetPorts("Star47_input.txt")
    starts = getStarts(ports)
    max = 0
    for s in starts:
        s_max = getMaxStrength(s, s, ports)
        if s_max > max:
            max = s_max 
    return max
          
print findMaxBridge("Star47_input.txt")