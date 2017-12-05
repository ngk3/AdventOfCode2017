
# Function used to read a file and find all valid paraphrases
def find_valid_paraphrases(input_file_name):
    # count tracks the number of valid paraphrases found
    count = 0
    # Read each line of the file and ...
    for line in open(input_file_name):
        # Check if there are any duplicates in the phrase, increasing count if there are none
        splitted = line.strip().split(" ")
        no_duplicates = set()
        for s in splitted:
            no_duplicates.add(sort_string(s))
        if len(splitted) == len(no_duplicates):
            count += 1 
    return count 
    
# Helper Function used to sort a strong to be in alphabetical order
def sort_string(s):
    # Get a list of letters, sort, and return the string build from the sorted list
    letters = []
    for i in s:
        letters.append(i)
    letters = sorted(letters)
    returning = ""
    for l in letters:
        returning += l 
    return returning 
    
print find_valid_paraphrases("star7_input.txt")
