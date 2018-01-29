import math

# Function used to see if n is prime
def prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

# Function used to get register H after executing the instructions
def getHAfterInstructions():
    # Initialize the registers
    registers = dict([])
    registers["a"] = 1
    for letter in ["b","c","d","e","f","g","h"]:
        registers[letter] = 0
        
    # Initialize b and c 
    registers["b"] = 57 * 100 + 100000
    registers["c"] = registers["b"] + 17000
    
    # Optimizes to only go through c-b / 17 iterations
    for b in range(registers["b"], registers["c"] + 1, 17):
        # h is only increased if prime from the cycling pattern
        if not prime(b):
            registers["h"] += 1
    
    return registers["h"]
    
print getHAfterInstructions()