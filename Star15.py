import operator

# Global variables
# registers stores the register values, ops keeps the operations to be used
registers = {}
ops = { "==" : operator.__eq__,
        "!=" : operator.__ne__,
        ">=" : operator.__ge__,
        ">"  : operator.__gt__,
        "<=" : operator.__le__,
        "<"  : operator.__lt__,
        "inc" : operator.add,
        "dec" : operator.sub}
# Used for Part 2 (Star16)
highest_ever = 0
highest_ever_reg = ""

# Function to check the conditional given by the instruction 
def check_if(cond):
    cond_splitted = cond.split(" ")
    if not cond_splitted[0] in registers.keys():
        registers[cond_splitted[0]] = 0
    return ops[cond_splitted[1]](registers[cond_splitted[0]], int(cond_splitted[2]))

# Function to modify the registers as necessary and check highest_ever for Star 16
def change_value(modify):
    modify_splitted = modify.split(" ")
    if not modify_splitted[0] in registers.keys():
        registers[modify_splitted[0]] = 0
    registers[modify_splitted[0]] = ops[modify_splitted[1]](registers[modify_splitted[0]], int(modify_splitted[2]))
    global highest_ever
    global highest_ever_reg
    # Star16 Implementation
    if registers[modify_splitted[0]] > highest_ever:
        highest_ever = registers[modify_splitted[0]]
        highest_ever_reg = modify_splitted[0]
    
# Function to read the file and set all the registers 
def read_file(file_name):
    for line in open(file_name):
        instruction = line.split(" if ")
        if check_if(instruction[1]):
            change_value(instruction[0])

# Function used to get the highest end value of a register        
def get_largest_value_in_register():
    highest = 0
    highest_reg = ""
    for k in registers.keys():
        if registers[k] > highest:
            highest = registers[k]
            highest_reg = k 
    return highest_reg, highest     
    
read_file("star15_input.txt")
print "PART 1: ", get_largest_value_in_register()
print "PART 2: ", highest_ever_reg, highest_ever