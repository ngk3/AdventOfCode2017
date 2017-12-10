
# Class used to represent a Tree
class Tree:
    # all_nodes will store all the nodes, root is the bottom program, 
    # weights stores the total weights of each node 
    all_nodes = []
    root = None
    weights = {}
    
    # Function used to create a node and insert into all_nodes
    def create_node_no_children(self, info):
        info_splitted = info.split(" ")
        self.all_nodes.append(Node(info_splitted[0], int(info_splitted[1])))

    # Function used to connect parent-children relationships of nodes 
    def create_node_parents(self, info, children):
        # Get the indices of the parent and children nodes in all_nodes
        node_index = -1
        children_index = []
        node_name = info.split(" ")[0]
        children_name = children.split(", ")
        for an in range(len(self.all_nodes)):
            if self.all_nodes[an].name == node_name:
                node_index = an 
            elif self.all_nodes[an].name in children_name:
                children_index.append(an)
        # Set the children and parent accordingly
        for ci in children_index:
            self.all_nodes[node_index].children.append(self.all_nodes[ci])
            self.all_nodes[ci].parent = self.all_nodes[node_index]
    
    # Function that reads an input file and create the nodes and the node relationships
    def read_file_and_get_nodes(self, file_name):
        # Read the file and create the nodes 
        node_relationships = {}
        for line in open(file_name):
            splitted = line.strip().split(" -> ")
            splitted[0] = splitted[0].replace("(", "").replace(")", "")
            self.create_node_no_children(splitted[0])
            if len(splitted) == 2:
                node_relationships[splitted[0]] = splitted[1]
        
        # Set the relationships of the nodes
        for node_info in node_relationships.keys():
            self.create_node_parents(node_info, node_relationships[node_info])
    
    # Function used to get and set the root node 
    def get_parent(self):
        index = 0
        self.root = self.all_nodes[0]
        while (self.root.parent != None):
            self.root = self.root.parent
        return self.root 
        
    # Function used to print the tree information 
    def print_node_info(self):
        for n in self.all_nodes:
            s = n.name + " " + str(n.weight)
            if len(n.children) > 0:
                s += " -> "
            for c in n.children:
                s += c.name + " " 
            if n.parent != None:
                s += "(Parent = " + n.parent.name + ")"
            print s.strip()

    # Function used to calculate and set the combined weights of each node 
    def get_weights(self, start):
        # Recursively find the combined weights of each node starting from the root and going up
        if len(start.children) == 0:
            self.weights[start.name] = start.weight
            return start.weight 
        if start.name in self.weights.keys():
            return self.weights[start.name]
        w = 0
        for c in start.children:
            w += self.get_weights(c)
        w += start.weight
        self.weights[start.name] = w
        return w 
    
    # Function used to find the one incorrect weight and return the change needed to balance the programs 
    def find_incorrect_weight_and_return_balanced_weight(self):
        # Find the parent of the incorrect weight 
        visited = []
        visited.append(self.root)
        current_node = None 
        found_node = None 
        while len(visited) > 0: 
            c_weights = set()
            current_node = visited.pop(0)
            for c in current_node.children:
                c_weights.add(self.weights[c.name])
                visited.append(c)
            if len(c_weights) == 2:
                found_node = current_node
        # Get the new weight needed to balance the tower
        frequency = {}
        for c in found_node.children:
            if self.weights[c.name] in frequency.keys():
                frequency[self.weights[c.name]] += 1
            else:
                frequency[self.weights[c.name]] = 1
        different_value = 0
        same_values = 0
        for f in frequency.keys():
            if frequency[f] == 1:
                different_value = f
            else:
                same_values = f
        for c in found_node.children:
            if self.weights[c.name] == different_value:
                return c.weight + (same_values - different_value)

# The Node class used to store information of each program            
class Node:
    name = ""
    weight = -1
    
    def __init__(self, n, w):
        self.name = n 
        self.weight = w
        self.children = []
        self.parent = None
    

    

t = Tree()
t.read_file_and_get_nodes("star13_input.txt")

n = t.get_parent()
print "PART 1: ", n.name
t.get_weights(n)
print "PART 2: ",   t.find_incorrect_weight_and_return_balanced_weight()