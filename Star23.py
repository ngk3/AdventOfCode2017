
# Node class used to store the programs and neighbors
class Node:
    def __init__(self, p_id):
        self.id = p_id
        self.neighbors = set([])
	
    def addNeighbor(self, n):
        self.neighbors.add(n)
        
    def getNeighbors(self):
        return self.neighbors
    
# Function used to read the file and create a dictionary of nodes (node id -> nodes)	
def readFileAndCreateNodes(file_name):
    nodes = dict([])
    node_connections = dict([])
    # Create all the nodes without neighbors and then store the neighbor information
    for line in open(file_name, 'r'):
        line_splitted = line.strip().split(" <-> ")
        nodes[int(line_splitted[0])] = Node(int(line_splitted[0]))
        neighbors_splitted = line_splitted[1].split(", ")
        for ns in range(len(neighbors_splitted)):
            neighbors_splitted[int(ns)] = int(neighbors_splitted[ns])
        node_connections[int(line_splitted[0])] = neighbors_splitted
    
    # Set all the neighbors for the nodes
    for nc in node_connections.keys():
        temp = ""
        for n in node_connections[nc]:
            nodes[nc].addNeighbor(nodes[n])
        
    return nodes

# Function that prints the neighbors of the node node_id
def print_single_node(nodes, node_id):
    printing = str(node_id) + " --> "
    neighbors = nodes[node_id].getNeighbors()
    for n in neighbors:
        printing += str(n.id) + " "
    print printing

# Function that gets a list of all the connections a Node start_node_id has	
def getTotalConnections(nodes, start_node_id):
	# This essentially uses a bfs to get the connections
    visited = []
    queued = []
    queued.append(nodes[start_node_id])
	
    # Get all the connected nodes and return all connected nodes
    while len(queued) > 0:
        current_node = queued.pop()
        if current_node in visited:
            continue
        visited.append(current_node)
        for n in current_node.getNeighbors():
            if n not in visited:
                queued.append(n)
    return visited

# Function that finds the number of groups (Star24)
def getNumGroups(nodes):
    # Gets all the node ids
    queued = nodes.keys()
    
    # Go through all the non-connected group of nodes
    num_groups = 0
    while len(queued) > 0:
        next_node = queued.pop()
        next_visited = getTotalConnections(nodes, next_node)
        for nv in next_visited:
            try:
                queued.remove(nv.id)
            except:
                continue
        num_groups += 1
        
    return num_groups

       
nodes = readFileAndCreateNodes("star23_input.txt")
total_connections_0 = getTotalConnections(nodes, 0)
print "Programs in the group that contains Program ID 0 =", len(total_connections_0)
print "Number of different groups = ", getNumGroups(nodes)
