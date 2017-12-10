
class Tree:
    all_nodes = []
    root = None
    weights = {}
    
    def create_node_no_children(self, info):
        info_splitted = info.split(" ")
        self.all_nodes.append(Node(info_splitted[0], int(info_splitted[1])))

    def create_node_parents(self, info, children):
        node_index = -1
        children_index = []
        node_name = info.split(" ")[0]
        children_name = children.split(", ")
        for an in range(len(self.all_nodes)):
            if self.all_nodes[an].name == node_name:
                node_index = an 
            elif self.all_nodes[an].name in children_name:
                children_index.append(an)
        for ci in children_index:
            self.all_nodes[node_index].children.append(self.all_nodes[ci])
            self.all_nodes[ci].parent = self.all_nodes[node_index]
    
    def read_file_and_get_nodes(self, file_name):
        node_relationships = {}
        for line in open(file_name):
            splitted = line.strip().split(" -> ")
            splitted[0] = splitted[0].replace("(", "").replace(")", "")
            self.create_node_no_children(splitted[0])
            if len(splitted) == 2:
                node_relationships[splitted[0]] = splitted[1]
        
        for node_info in node_relationships.keys():
            self.create_node_parents(node_info, node_relationships[node_info])
        
    def get_parent(self):
        index = 0
        self.root = self.all_nodes[0]
        while (self.root.parent != None):
            self.root = self.root.parent
        return self.root 
        
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

    def get_weights(self, start):
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
    
    def find_incorrect_weight_and_return_balanced_weight(self):
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
        for c in found_node.children:
            print c.name, c.weight,": " + str(self.weights[c.name])
            
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
#t.print_node_info()

n = t.get_parent()
print n.name
t.get_weights(n)
print t.weights
t.find_incorrect_weight_and_return_balanced_weight()