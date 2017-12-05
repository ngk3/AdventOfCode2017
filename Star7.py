
# Function used to read a file and find all valid paraphrases
def find_valid_paraphrases(input_file_name):
    # count tracks the number of valid paraphrases found
    count = 0
    # Read each line of the file and ...
    for line in open(input_file_name):
        # Check if there are any duplicates in the phrase, increasing count if there are none
        splitted = line.strip().split(" ")
        no_duplicates = set(splitted)
        if len(splitted) == len(no_duplicates):
            count += 1
    return count 
    
print find_valid_paraphrases("star7_input.txt")
