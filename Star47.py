# Function to read the input file and get all the useable ports
def readFileAndGetPorts(file_name):
	ports = []
	for line in open(file_name, 'r'):
		ports.append(line.split("/"))
		ports[-1][0] = int(ports[-1][0])
		ports[-1][1] = int(ports[-1][1])
	return ports

# Function used to get the possible starting ports    
def getStarts(ports):
	starts = []
	for p in range(len(ports)):
		if ports[p][0] == 0 or ports[p][1] == 0:
			starts.append(ports[p])
	for s in starts:
		ports.remove(s)
	return starts

# Function used to get all the valid port-nodes given a specific port
def getValidPorts(node, ports):
	valid_ports = []
	valid_nums = []
	if node[-1][0] in node[-2]:
		valid_nums.append(node[-1][1])
	if node[-1][1] in node[-1]:
		valid_nums.append(node[-1][0])
	for p in ports:
		if p[0] in valid_nums or p[1] in valid_nums:
			valid_ports.append(p)
	return valid_ports
		
			
def findMaxPath(nodes, ports):
	new_path = []
	max = 0
	if len(nodes) == 1:
		for p in ports:
			if p[0] == nodes[0][0] + nodes[0][1] or p[1] == nodes[0][0] + nodes[0][1]:
				nodes_copy = nodes.copy()
				nodes_copy.append(p)
				ports_copy = ports_copy()
				ports_copy.remove(p)
				temp = countPath(findMaxPath(nodes_copy, ports_copy))
				if temp > max:
					new_path = temp
					max = countPath(new_path)
		return new_path
	else:
		valid_ports = getValidPorts(nodes, ports)
		if len(valid_ports) == 0:
			return nodes
		for vp in valid_ports:
			nodes_copy = nodes.copy()
			nodes_copy.append(vp)
			valid_ports_copy = valid_ports_copy()
			valid_ports_copy.remove(vp)
			temp = countPath(findMaxPath(nodes_copy, valid_ports_copy))
			if temp > max:
				new_path = temp
				max = countPath(new_path)
		return new_path
			
		
			
def findMaxBridge(file_name):
	ports = readFileAndGetPorts(file_name)
	starts = getStarts(ports)
	max = 0
	for s in starts:
		s_max = findMaxPath([s], ports)
		if countPath(s_max) > max:
			max = countPath(s_max)
	return max
    
ports = readFileAndGetPorts("Star47_input.txt")
starts = getStarts(ports)
print starts[0]
for v in getValidPorts(starts[0], ports):
    print v
    