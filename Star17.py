
# Function used to get the total_score from a string of groupings (garbage is erased)
def get_total_score(group_string):
    # total_count tracks the total score, count tracks the current grouping score 
    total_score = 0
    count = 0
    # Go through each character in the string 
    for gs in group_string:
        # If a new group is found, increase the current grouping score and total_score 
        if gs == "{":
            count += 1
            total_score += count 
        # If a group is found to be closed, decrease the current grouping score 
        elif gs == "}":
            count -= 1
    return total_score

# Function used to read the input file and erase all the garbage 
def read_file(file_name):
    # non_garbage is the input without any garbage to be returned,
    # garbage_count tracks the number of non-canceled characters that are within garbage,
    non_garbage = ""
    garbage_count = 0
    line = open(file_name).readline()
    current_index = 0
    in_garbage = False
    # Go through the string 
    while current_index < len(line):
        # If canceling characters, skip the next character 
        if line[current_index] == "!":
            current_index += 1 
        # If '<' and not in garbage, string is in garbage currently 
        elif line[current_index] == "<" and not in_garbage:
            in_garbage = True 
        # If '>' is found and in garbage, string exists garbage 
        elif line[current_index] == ">" and in_garbage:
            in_garbage = False
        # Otherwise, if not in garbage, add the character to non_garbage 
        elif not in_garbage:
            non_garbage += line[current_index] 
        else:
            garbage_count += 1
        current_index += 1
    return [non_garbage, garbage_count]

non_garbage_stream = read_file("star17_input.txt")
print non_garbage_stream[0]
print "Total Score:", get_total_score(non_garbage_stream[0]) 
print "Non-canceled in Garbage:", non_garbage_stream[1]

testing_stuffs = read_file("testing.txt")
print testing_stuffs[0]
print "Total Score:", get_total_score(testing_stuffs[0]) 
print "Non-canceled in Garbage:", testing_stuffs[1]
